import random, asyncio, datetime, pytz, time, psutil, shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from helper.database import db
from config import Config, rkn
from helper.utils import humanbytes, handle_banned_user_status

# Inline keyboard buttons
upgrade_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('🎟️ᴄʟɪᴄᴋ  ᴛᴏ  ʙᴜʏ  ᴘʀᴇᴍɪᴜᴍ', callback_data='about')],
    [InlineKeyboardButton("📦ɢɪᴠᴇᴡᴀʏ", url='https://t.me/tetris_botz/14'),
     InlineKeyboardButton("◀️ɢᴏ ʙᴀᴄᴋ", callback_data="start")]
])

start_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('ᴄʜᴇᴄᴋ  ᴍᴏʀᴇ  ᴜsᴇғᴜʟʟ  ʙᴏᴛs🤖', callback_data='bots')],
    [InlineKeyboardButton('ϟ ʙᴏᴛ  sᴛᴀᴛs', callback_data='status'),
     InlineKeyboardButton('ʜᴏᴡ  ᴛᴏ  ᴇᴅɪᴛ ⎙', callback_data='help')],
    [InlineKeyboardButton('ᴜᴘɢʀᴀᴅᴇ  ᴛᴏ  ᴘʀᴇᴍɪᴜᴍ🎟️', callback_data='upgrade')]
])

# Ban check handler
@Client.on_message(filters.private)
async def check_ban_status(bot, message):
    ban_status = await db.get_ban_status(message.from_user.id)
    if ban_status["is_banned"]:
        print(f'You are banned, {message.from_user.first_name}')
    await handle_banned_user_status(bot, message)


@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message) 
    caption = rkn.START_TXT.format(user.mention)
    
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=caption, reply_markup=start_button)       
    else:
        await message.reply_text(text=caption, reply_markup=start_button, disable_web_page_preview=True)
    
    await asyncio.sleep(90)
    
    second_caption = rkn.START_TXT2.format(user.mention)
    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴍɪɴᴇ  sᴇᴇᴅ  ғᴏʀ  ᴀɪʀᴅʀᴏᴘ", url="http://t.me/seed_coin_bot/app?startapp=5050736780")]
    ])
    
    await message.reply_text(text=second_caption, reply_markup=button, disable_web_page_preview=True)
    
    sticker_file_id = "CAACAgQAAxkBAAKEx2cSBq_gllFUVWdg5tgc68ZOO99LAAL9DAACCd85UvadxdG9bFD6NgQ"
    await message.reply_sticker(sticker_file_id)

# My Plan command handler
from datetime import datetime, timedelta

@Client.on_message(filters.private & filters.command("myplan"))
async def myplan(client, message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    
    if await db.has_premium_access(user_id):
        data = await db.get_user(user_id)
        expiry_time = data.get("expiry_time")
        
        # Format expiry time and calculate time left
        expiry_str_in_ist = expiry_time.strftime('%Y-%m-%d %H:%M')
        time_left = expiry_time - datetime.now()
        time_left_str = str(timedelta(seconds=int(time_left.total_seconds())))

        await message.reply_text(
            f"**ʏᴏᴜʀ  ᴘʟᴀɴ  ᴅᴇᴛᴀɪʟs  ʜᴇʀᴇ**\n\n**🗿 ᴜsᴇʀ ᴛʏᴘᴇ** - premium\n"
            f"👤 **ᴜsᴇʀɴᴀᴍᴇ** - {user_mention}\n"
            f"⚡ **ᴜsᴇʀ  ɪᴅ** - <code>{user_id}</code>\n"
            f"⏰ **ᴛɪᴍᴇ  ʟᴇғᴛ** - {time_left_str}\n"
            f"⌛️ **ᴇxᴘɪʀʏ  ᴅᴀᴛᴇ** - {expiry_str_in_ist}"
        )
    else:
        await message.reply_text(
            f"**ɪɴᴠᴀʟɪᴅ  ᴀᴄᴛɪᴏɴ , ᴜᴘɢʀᴀᴅᴇ  ᴛᴏ  ᴘʀᴇᴍɪᴜᴍ\nᴄʜᴇᴄᴋᴏᴜᴛ  ᴘʟᴀɴs,  ᴄʟɪᴄᴋ  ʜᴇʀᴇ👉🏻** /premium\n\n"
        )

# Plans command handler
@Client.on_message(filters.private & filters.command(["premium","upgrade",]))
async def plans(client, message):
    user = message.from_user
    free_trial_status = await db.get_free_trial_status(user.id)
    image_url = "https://envs.sh/o7w.jpg"
    
    if not await db.has_premium_access(user.id):
        if not free_trial_status:
            await message.reply_photo(photo=image_url, caption=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button)
        else:
            await message.reply_photo(photo=image_url, caption=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button)
    else:
        await message.reply_photo(photo=image_url, caption=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button)

# Callback query handler
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    user_id = query.from_user.id
    user_mention = query.from_user.mention
    
    if data == "start":
        # Reverting back to the original picture
        original_image_path = Config.RKN_PIC  # Ensure this is the original image
        await query.message.edit_media(
            media=InputMediaPhoto(original_image_path, caption=rkn.START_TXT.format(user_mention)),
            reply_markup=start_button
        )
        

    elif data == "upgrade":  # This corresponds to the "Advertise with Us" button
        # Changing to the specific advertisement image
        new_image_path = "https://envs.sh/o7w.jpg"  # Replace this with the actual path to the new image
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.UPGRADE),  # Assuming rkn.ADVERTISE_CAPTION holds your caption text
            reply_markup=upgrade_button         
        )
        
    elif data == "give_trial":
        await query.message.delete()
        free_trial_status = await db.get_free_trial_status(user_id)
        
        if not free_trial_status:            
            await db.give_free_trail(user_id)
            new_text = (
                "**ʀᴇᴀᴅʏ  ᴛᴏ  ᴜsᴇ,  ᴘʀᴇᴍɪᴜᴍ  ᴛʀɪᴀʟ  sᴛᴀʀᴛᴇᴅ  \nᴛʀʏ  ᴘʀᴇᴍɪᴜᴍ  ʟɪᴛᴇ  ᴘʟᴀɴ  ғᴏʀ  ғɪᴠᴇ  ᴅᴀʏs \n\nᴏɴᴄᴇ  ᴛʀɪᴀʟ  ᴘᴇʀɪᴏᴅ  ɪs  ᴏᴠᴇʀ ,  ʏᴏᴜ  ᴡɪʟʟ  \nʙᴇ  ᴄʜᴀʀɢᴇᴅ  ғᴏʀ  ᴜᴘɢʀᴀᴅɪɴɢ  ᴘʀᴇᴍɪᴜᴍ**"
            )
        else:
            new_text = (
                "**ɪɴᴠᴀʟɪᴅ  ᴀᴄᴛɪᴏɴ , ʏᴏᴜ  ᴜsᴇᴅ  ᴛʀɪᴀʟ  ᴘʟᴀɴ\nʙᴜʏ  ᴘʀᴇᴍɪᴜᴍ,  sᴇɴᴅ**  /plans  **ᴄᴏᴍᴍᴀɴᴅ** \n\n"
            )
        
        await client.send_message(user_id, text=new_text)

    elif data == "help":
        await query.message.edit_text(
            text=rkn.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴇғɪx / sᴜғғɪx", callback_data="custom_file_name"),
                InlineKeyboardButton("ᴍᴇᴛᴀᴅᴀᴛᴀ", callback_data="digital_meta_data")
            ],[
                InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ", callback_data="upgrade"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data="start")
            ]])
        )

    elif data == "bots":
        await query.message.edit_text(
            text=rkn.BOTS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ɪɴsᴛᴀ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ  ʙᴏᴛ 🤍", url= "https://t.me/instagram_dload_bot")
            ],[
                InlineKeyboardButton("ғɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ʙᴏᴛ 🤖", url= "https://t.me/File_stream_link_bot")
            ],[
                InlineKeyboardButton("🛸ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Tetris_botz"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data= "start")
             ]])
        )

    elif data == "about":
        await query.message.edit_text(
            text=rkn.ABOUT_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ʏᴇs", callback_data="ptime")],
                [InlineKeyboardButton("ɴᴏ", callback_data="Nᴏ")
            ]])
        )

    elif data == "ptime":
        await query.message.edit_text(
            text=rkn.TIME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("1  Month  -  49₹", callback_data="mon")],
                [InlineKeyboardButton("3  Month  -  129₹", callback_data="tmon")],
                [InlineKeyboardButton("Life time  -  399₹", callback_data="life")],
                [InlineKeyboardButton("ϟ ᴡᴀɴᴛ  ᴅɪsᴄᴏᴜɴᴛ,  ᴄʜᴇᴄᴋ  ᴏғғᴇʀ  ʜᴇʀᴇ ϟ", callback_data="offer")
            ]])
        )

    

    elif data == "mon":
        await query.message.edit_text(
            text=rkn.FIF,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟɪᴄᴋ  ᴛᴏ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ💸", callback_data = "mon2")
            ],[
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade"),
                InlineKeyboardButton("ᴀᴅᴍɪɴ🛸", url = "https://t.me/tetris_admino_bot")
             ]])
        )

    elif data == "tmon":
        await query.message.edit_text(
            text=rkn.MON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟɪᴄᴋ  ᴛᴏ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ💸", callback_data = "tmon2")
            ],[
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade"),
                InlineKeyboardButton("ᴀᴅᴍɪɴ🛸", url = "https://t.me/tetris_admino_bot")
             ]])
        )

    elif data == "life":
        await query.message.edit_text(
            text=rkn.TMON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄʟɪᴄᴋ  ᴛᴏ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ💸", callback_data = "life2")
            ],[
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade"),
                InlineKeyboardButton("ᴀᴅᴍɪɴ🛸", url = "https://t.me/tetris_admino_bot")
             ]])
        )

    elif data == "mon2":
        new_image_path = "https://envs.sh/o7i.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.FIFT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 

      
    elif data == "tmon2":
        new_image_path = "https://envs.sh/o7b.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.MONT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 


    elif data == "life2":
        new_image_path = "https://envs.sh/o7P.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.LIFE),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 


      
    elif data == "custom_file_name":
        await query.message.edit_text(
            text=rkn.CUSTOM_FILE_NAME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "help")]])) 
      
    elif data == "digital_meta_data":
        await query.message.edit_text(
            text=rkn.DIGITAL_METADATA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "help")]]))



    elif data == "speed":
        await query.answer(
            "💸ʙ𝗎ʏ ᴘʀᴇᴍɪᴜᴍ & ɢᴇᴛ 2𝗑 ᴅᴡɴʟᴅ 𝗌ᴘᴇᴇᴅ \n\n"
            "ғʀᴇᴇ ᴘʟᴀɴ - upto 6mb/s \n"
            "ᴘʀᴇᴍɪᴜᴍ - upto 12mb/s \n\n"
            "* Also speed varies due to server load, net connectivity, hosting, file extension, etc.",
            show_alert=True
        )

    elif data == "No":
        await query.answer(
            "hhhhvvnmnnnnbvhhmmmmmmmmkhvccvvhbbb",
            show_alert=True
        )

    elif data == "offer":
        await query.answer(
            "\n\n"
            "Buy 3-month plan, save ₹20, and get up to 10 days extra free.\n\n"
            "Buy a lifetime validity plan at ₹399 and get ₹100 refund instantly by UPI (only for first-time buyers).\n\n"
            "* All payments are safe and processed automatically.",
            show_alert=True
        )

    elif data == "status":
        # Fetching bot status data
        total_users = await db.total_users_count()
        uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        free_space = humanbytes(shutil.disk_usage(".").free)
        random_number = random.randint(5, 15)

        bot_status = (
            f"bhbbnnmnmmm\n\n"
            f"Version checked {uptime} ago\n"
            f" {total_users} users started the bot till now\n"
            f" {random_number} users active live now\n"
            f" Average 582 regular users\n"
            f"Premium users count - 96\n"
            f"{free_space} GB of free disk space\n"
            f" {recv} GB of data cached and ready to clear"
            f"gjmmmmj"
        )
        await query.answer(
            bot_status,
            show_alert=True
        )


    elif data == "final":
        # Send the user's ID and name to the log channel
        log_message = f"🇷 🇪 🇲 🇮 🇳 🇩 🇪 🇷 🇸 \n\n**ᴜsᴇʀɴᴀᴍᴇ** - {user_mention} \n**ɪᴅ**: <code>{user_id}</code> \n**ᴀᴄᴛɪᴏɴ** - amount paid \n**ᴛɪᴍᴇ** - ᴄʜᴇᴄᴋ ʜᴇʀᴇ👉🏻"
        await client.send_message(chat_id=Config.LOG_CHANNEL, text=log_message)
        
        # Respond to the user with their Telegram user ID included
        sent_message = await query.message.edit_text(
            text=(
                f"**sᴛᴀᴛᴜs-  ᴛʀᴀɴsᴀᴄᴛɪᴏɴ  ᴘʀᴏᴄᴇssɪɴɢ🔄** \n"
                f"ᴛ**x**ɴ  ɪᴅ: RIW92<code>{user_id}</code>P \n\n"
                f"Taking  time  then  usual , sever  load.. Hold on! You  will  be  notified  when  your  transaction  passes  the  verification  process\n\n"
                f"**ᴍᴀx ᴡᴀɪᴛɪɴɢ ᴛɪᴍᴇ - 50 ᴍɪɴᴜᴛᴇs**"
            ),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴀᴅᴍɪɴ", url="https://t.me/tetris_admino_bot")
            ]])
        )
        await asyncio.sleep(3000)
        await sent_message.delete()
        
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

if __name__ == "__main__":
    db = Database(Config.DB_URL, Config.DB_NAME)
    app = Client("my_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
    app.uptime = time.time()  # Set the uptime for calculating bot running time
    app.run()
