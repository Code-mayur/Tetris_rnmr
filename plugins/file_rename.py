from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.utils import progress_for_pyrogram, convert, humanbytes, add_prefix_suffix
from helper.database import db
from asyncio import sleep
from PIL import Image
import os, time, asyncio
from config import Config
import time

UPLOAD_TEXT = """**ᴜᴩʟᴏᴀᴅɪɴɢ....**"""
app = Client("4gb_FileRenameBot", api_id=Config.API_ID, api_hash=Config.API_HASH, session_string=Config.STRING_SESSION)

# Dictionary to store last file rename times and file count for users
last_rename_time = {}
user_file_count = {}

# Function to calculate exponential wait time
def get_wait_time(file_count):
    base_time = 3  # 3 minutes
    wait_time = base_time * (3 ** (file_count - 1))  # Exponentially increasing time
    if wait_time > 729:  # Reset after 729 minutes
        wait_time = 3
    return wait_time * 60  # Convert to seconds


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    user_id = message.from_user.id
    current_time = time.time()

    # Check if user has premium access
    has_premium = await db.has_premium_access(user_id)

    # Check if user is spamming (for ordinary users)
    if not has_premium:
        if user_id in last_rename_time:
            elapsed_time = current_time - last_rename_time[user_id]
            file_count = user_file_count.get(user_id, 1)  # Default to 1 if no file count exists
            wait_time = get_wait_time(file_count)

            if elapsed_time < wait_time:
                remaining_time = wait_time - elapsed_time
                await message.reply_text(f"**ᴘʟᴇᴀsᴇ  ᴡᴀɪᴛ🕑** {int(remaining_time // 60)} **ᴍɪɴ.** {int(remaining_time % 60)} **sᴇᴄ.  ʙᴇғᴏʀᴇ  sᴇɴᴅɪɴɢ  ᴀɴᴏᴛʜᴇʀ  ғɪʟᴇ,  sɪɴᴄᴇ  ʏᴏᴜ  ᴀʀᴇ  ᴏɴ  ғʀᴇᴇ  ᴘʟᴀɴ \n\nᴡᴀɴᴛ  ᴛᴏ  ᴀᴠᴏɪᴅ  ᴡᴀɪᴛɪɴɢ  ᴜᴘɢʀᴀᴅᴇ  ᴛᴏ** /premium")
                return
            else:
                # Increment the file count after each file rename
                user_file_count[user_id] = file_count + 1
        else:
            # First file rename, set initial count to 1
            user_file_count[user_id] = 1

        last_rename_time[user_id] = current_time

    file = getattr(message, message.media.value)
    filename = file.file_name

    # Check file size
    if file.file_size > 2000 * 1024 * 1024:  # Above 2GB requires premium
        if not has_premium:
            await message.reply_text(
                f"2ɢʙ+ **ғɪʟᴇ  ɴᴏᴛ  sᴜᴘᴘᴏʀᴛᴇᴅ  ғᴏʀ  ғʀᴇᴇ  ᴜsᴇʀs**\n\n"
                f"**ᴜᴘɢʀᴀᴅᴇ  ᴛᴏ** /premium **ғᴏʀ  ᴇᴅɪᴛɪɴɢ** 2ɢʙ+ **ғɪʟᴇ**"
            )
            return  # Don't proceed further for free users with 2GB+ files

    # Prompt for new filename if file size is valid
    try:
        await message.reply_text(
            text=f"**📜ᴛʏᴘᴇ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴏʀ ᴄᴏᴘʏ ᴘᴀsᴛᴇ ᴏʟᴅ ᴏɴᴇ**\n\n"
                 f"**📜ᴏʟᴅ ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )
        await sleep(30)
    except FloodWait as e:
        await sleep(e.value)
    except Exception as e:
        print(f"Error: {e}")
	    
	    	    
	    

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text 
        await message.delete() 
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton("📁ᴜᴘʟᴏᴀᴅ  ᴀs  ᴅᴏᴄᴜᴍᴇɴᴛ",callback_data = "upload_document")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("💻ᴜᴘʟᴏᴀᴅ  ᴀs  ᴠɪᴅᴇᴏ", callback_data = "upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎷ᴜᴘʟᴏᴀᴅ ᴀs ᴀᴜᴅɪᴏ", callback_data = "upload_audio")])
        await message.reply(
            text=f"**🔍sᴇʟᴇᴄᴛ  ᴛʜᴇ  ᴏᴜᴛᴩᴜᴛ  ғɪʟᴇ  🪧ᴛʏᴩᴇ**\n\n**• ғɪʟᴇ ɴᴀᴍᴇ :-**`{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )




@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):
    # Creating Directory for Metadata
    if not os.path.isdir("Metadata"):
        os.mkdir("Metadata")

    user_id = int(update.message.chat.id) 
    new_name = update.message.text
    new_filename_ = new_name.split(":-")[1]
    try:
        # adding prefix and suffix
        prefix = await db.get_prefix(user_id)
        suffix = await db.get_suffix(user_id)
        new_filename = add_prefix_suffix(new_filename_, prefix, suffix)
    except Exception as e:
        return await update.message.edit(f"⚠️**sᴏᴍᴇᴛʜɪɴɢ  ᴡᴇɴᴛ  ᴡʀᴏɴɢ,  sᴇᴇᴋ  ʜᴇʟᴘ  ғʀᴏᴍ  [ᴀᴅᴍɪɴ](https://t.me/Tetris_admino_bot)\n\nError: {e}")
	    
    file_path = f"downloads/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("`ᴛʀʏɪɴɢ  ᴛᴏ  ᴅᴏᴡɴʟᴏᴀᴅ....`")    
    try:
     	path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram, progress_args=("**ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ....**", ms, time.time()))                    
    except Exception as e:
     	return await ms.edit(e)
     	     
    _bool_metadata = await db.get_metadata_mode(user_id)
    if (_bool_metadata):
	    await bot.send_message(
        chat_id=update.message.chat.id,
        text="**ғɪʟᴇ ɪs ʙᴇɪɴɢ ʀᴇɴᴀᴍᴇᴅ ᴡɪᴛʜ ᴍᴇᴛᴀᴅᴀᴛᴀ.**"
	    )
	    
	await ms.edit("`ᴛʀʏɪɴɢ  ᴛᴏ  ᴜᴩʟᴏᴀᴅɪɴɢ....`")
	    
	    
    duration = 0
    try:
        parser = createParser(file_path)
        metadata = extractMetadata(parser)
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
        parser.close()
    except:
        pass
	    
    ph_path = None
    media = getattr(file, file.media.value)
    c_caption = await db.get_caption(user_id)
    c_thumb = await db.get_thumbnail(user_id)

    if c_caption:
         try:
             caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size), duration=convert(duration))
         except Exception as e:
             return await ms.edit(text=f"**ʏᴏᴜʀ  ᴄᴀᴩᴛɪᴏɴ  ᴇʀʀᴏʀ  ᴇxᴄᴇᴩᴛ  ᴋᴇʏᴡᴏʀᴅ  ᴀʀɢᴜᴍᴇɴᴛ  ●> ({e})")             
    else:
         caption = f"**{new_filename}**"
 
    if (media.thumbs or c_thumb):
         if c_thumb:
             ph_path = await bot.download_media(c_thumb) 
         else:
             ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")

    type = update.data.split("_")[1]
    if media.file_size > 2000 * 1024 * 1024:
        try:
            if type == "document":
                filw = await app.send_document(
                    Config.LOG_CHANNEL,
                    document=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
            elif type == "video":
                filw = await app.send_video(
                    Config.LOG_CHANNEL,
                    video=metadata_path if _bool_metadata else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
            elif type == "audio":
                filw = await app.send_audio(
                    Config.LOG_CHANNEL,
                    audio=metadata_path if _bool_metadata else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                await bot.delete_messages(from_chat, mg_id)
        except Exception as e:
            if file_path:
                os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            if metadata_path:
                os.remove(metadata_path)
            if path:
                os.remove(path)
            return await ms.edit(f" Eʀʀᴏʀ {e}")
    else:
        try:
            if type == "document":
                await bot.send_document(
                    update.message.chat.id,
                    document=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
            elif type == "video":
                await bot.send_video(
                    update.message.chat.id,
                    video=metadata_path if _bool_metadata else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
            elif type == "audio":
                await bot.send_audio(
                    update.message.chat.id,
                    audio=metadata_path if _bool_metadata else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=(UPLOAD_TEXT, ms, time.time()))
        except Exception as e:
            if file_path:
                os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            if metadata_path:
                os.remove(metadata_path)
            if path:
                os.remove(path)
            return await ms.edit(f" Eʀʀᴏʀ {e}")

    await ms.delete()
    if ph_path:
        os.remove(ph_path)
    if file_path:
        os.remove(file_path)
    if metadata_path:
        os.remove(metadata_path)


	    
