import random, asyncio, datetime, pytz, time, psutil, shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, InputMediaPhoto
from helper.database import db
from config import Config, rkn
from helper.utils import humanbytes, handle_banned_user_status

# Inline keyboard buttons
upgrade_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('🎟️ᴄʟɪᴄᴋ  ᴛᴏ  ʙᴜʏ  ᴘʀᴇᴍɪᴜᴍ', callback_data='about')],
    [InlineKeyboardButton("📦ɢɪᴠᴇᴡᴀʏ", callback_data='source_code'),
     InlineKeyboardButton("◀️ɢᴏ ʙᴀᴄᴋ", callback_data="start")]
])

start_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('ᴄʜᴇᴄᴋ  ᴍᴏʀᴇ  ᴜsᴇғᴜʟʟ  ʙᴏᴛs🤖', callback_data='bots')],
    [InlineKeyboardButton('🪧ᴀᴅᴠᴇʀᴛɪsɪɴɢ', callback_data='source_code'),
     InlineKeyboardButton('ʜᴏᴡ  ᴛᴏ  ᴇᴅɪᴛ📐', callback_data='help')],
    [InlineKeyboardButton('ᴜᴘɢʀᴀᴅᴇ  ᴛᴏ  ᴘʀᴇᴍɪᴜᴍ🎟️', callback_data='upgrade')]
])

# Ban check handler
@Client.on_message(filters.private)
async def check_ban_status(bot, message):
    ban_status = await db.get_ban_status(message.from_user.id)
    if ban_status["is_banned"]:
        print(f'You are banned, {message.from_user.first_name}')
    await handle_banned_user_status(bot, message)

# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message) 
    caption = rkn.START_TXT.format(user.mention)
    
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=caption, reply_markup=start_button)       
    else:
        await message.reply_text(text=caption, reply_markup=start_button, disable_web_page_preview=True)

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
            f"#ad\nreserve for ad"
        )

# Plans command handler
@Client.on_message(filters.private & filters.command(["premium","upgrade",]))
async def plans(client, message):
    user = message.from_user
    free_trial_status = await db.get_free_trial_status(user.id)
    image_url = "https://envs.sh/wMW.jpg"
    
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
        new_image_path = "https://envs.sh/wMW.jpg"  # Replace this with the actual path to the new image
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
                "#ad\nreserve for ad"
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
                InlineKeyboardButton("ɪɴsᴛᴀ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ  ʙᴏᴛ🤍", url= "https://t.me/instagram_dload_bot")
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
                InlineKeyboardButton("👑 ᴘʀᴇᴍɪᴜᴍ", callback_data="ptime")],
                [InlineKeyboardButton("📦 ʙᴜɴᴅʟᴇ", callback_data="btime")
            ]])
        )

    elif data == "ptime":
        await query.message.edit_text(
            text=rkn.TIME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("15  Days  -  39₹", callback_data="fif")],
                [InlineKeyboardButton("1  Month  -  59₹", callback_data="mon")],
                [InlineKeyboardButton("3  Month  -  159₹", callback_data="tmon")
            ]])
        )

    elif data == "btime":
        await query.message.edit_text(
            text=rkn.BTIME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("comming  soon", callback_data="tif")],
                [InlineKeyboardButton("◀️back", callback_data="about")
            ]])
        )
    

    elif data == "fif":
        await query.message.edit_text(
            text=rkn.FIF,
            disable_web_page_preview=False,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴘᴀʏᴍᴇɴᴛ💰", callback_data = "fif2")
            ],[
                InlineKeyboardButton("ᴅᴏᴜʙᴛ", url="https://t.me/tetris_admino_bot"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade")
            ]])
        ) 

    elif data == "mon":
        await query.message.edit_text(
            text=rkn.MON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴘᴀʏᴍᴇɴᴛ💰", callback_data = "mon2")
            ],[
                InlineKeyboardButton("ᴅᴏᴜʙᴛ", url="https://t.me/tetris_admino_bot"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade")
             ]])          
        ) 

    elif data == "tmon":
        await query.message.edit_text(
            text=rkn.TMON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴘᴀʏᴍᴇɴᴛ💰", url="https://your-payment-link.com")
            ],[
                InlineKeyboardButton("ᴅᴏᴜʙᴛ", url="https://t.me/Tetris_admino_bot"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "retry_payment")
            ]])
        )

    # Wait for 30 seconds before updating the button
        await sleep(30)
    
    # Update the buttons after 30 seconds
        await query.message.edit_text(
            text=rkn.TMON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ  ᴘᴀɪᴅ ✅", callback_data="paid_confirmed")
            ],[
                InlineKeyboardButton("ʀᴇᴛʀʏ ᴘᴀʏᴍᴇɴᴛ", callback_data="retry_payment"),
                InlineKeyboardButton("ᴀᴅᴍɪɴ", url="retry_payment")
            ]])
        )


    elif data == "tif":
        await query.message.edit_text(
            text=rkn.TIF,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴘᴀʏᴍᴇɴᴛ💰", callback_data = "tif2")
            ],[
                InlineKeyboardButton("ᴅᴏᴜʙᴛ", url="https://t.me/Tetris_admino_bot"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade")
             ]])
        )

    elif data == "fmon":
        await query.message.edit_text(
            text=rkn.FMON,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴘʀᴏᴄᴇᴇᴅ ᴛᴏ ᴘᴀʏᴍᴇɴᴛ💰", callback_data = "fmon2")
            ],[
                InlineKeyboardButton("ᴅᴏᴜʙᴛ", url="https://t.me/Tetris_admino_bot"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "upgrade")
             ]])
        )

    elif data == "fif2":
        new_image_path = "https://telegra.ph/file/4a0a3ac73658ff4c68dff.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.FIFT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 

      
    elif data == "mon2":
        new_image_path = "https://telegra.ph/file/4a0a3ac73658ff4c68dff.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.MONT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 


    elif data == "tmon2":
        new_image_path = "https://telegra.ph/file/4a0a3ac73658ff4c68dff.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.TMONT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 

    elif data == "tif2":
        new_image_path = "https://telegra.ph/file/4a0a3ac73658ff4c68dff.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.TIFT),
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("ᴀᴍᴏᴜɴᴛ ᴘᴀɪᴅ✅", callback_data = "final")]])) 

  

    elif data == "fmon2":
        new_image_path = "https://telegra.ph/file/4a0a3ac73658ff4c68dff.jpg"
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.FMONT),
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

    elif data == "status":
    # Fetching bot status data
        total_users = await db.total_users_count()
        uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        free_space = humanbytes(shutil.disk_usage(".").free)
        random_number = random.randint(5, 15)

        await query.message.edit_text(
            text=rkn.BOT_STATUS.format(uptime, total_users, random_number, free_space, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data="source_code")
            ]])
        )
        
    elif data == "source_code":  # This corresponds to the "Advertise with Us" button
        # Changing to the specific advertisement image
        new_image_path = "https://telegra.ph/file/0c41ddb3e7d3fafca59bc.jpg"  # Replace this with the actual path to the new image
        await query.message.edit_media(
            media=InputMediaPhoto(new_image_path, caption=rkn.DEV_TXT),  # Assuming rkn.ADVERTISE_CAPTION holds your caption text
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ  ᴀᴅᴍɪɴ", url="https://t.me/Tetris_admino_bot")
            ],[
                InlineKeyboardButton("ʙᴏᴛ  ᴇɴɢᴀɢᴇᴍᴇɴᴛ", callback_data = "status"),
                InlineKeyboardButton("◀️ʙᴀᴄᴋ", callback_data = "start")
                 ]])          
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
                f"Admin  will  verify  your  transaction  and  activate  premium  shortly.  You  will  be  notified  when  your  transaction  passes  the  verification  process\n\n"
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
