from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

# Dummy metadata settings
dummy_metadata_mode = {}
dummy_metadata_code = {}

TRUE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ', callback_data='metadata_1'),
         InlineKeyboardButton('✅', callback_data='metadata_1')
         ], [
         InlineKeyboardButton('sᴇᴛ  ᴄᴜsᴛᴏᴍ  ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

FALSE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏғғ', callback_data='metadata_0'),
          InlineKeyboardButton('❌', callback_data='metadata_0')
         ], [
         InlineKeyboardButton('sᴇᴛ  ᴄᴜsᴛᴏᴍ  ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    user_id = message.from_user.id
    await message.reply_text("**ᴀᴄᴄᴇssɪɴɢ......**", reply_to_message_id=message.id)
    
    # Use dummy data
    bool_metadata = dummy_metadata_mode.get(user_id, False)
    user_metadata = dummy_metadata_code.get(user_id, "No Metadata Set")
    
    if bool_metadata:
        return await message.reply_text(f"Your Current Metadata:-\n\n➜ `{user_metadata}`", 
                                        reply_markup=InlineKeyboardMarkup(TRUE))
    return await message.reply_text(f"Your Current Metadata:-\n\n➜ `{user_metadata}`", 
                                    reply_markup=InlineKeyboardMarkup(FALSE))

@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    data = query.data
    user_id = query.from_user.id
    
    # Toggle metadata mode
    if data.startswith('metadata_'):
        _bool = data.split('_')[1]
        dummy_metadata_mode[user_id] = bool(eval(_bool))
        user_metadata = dummy_metadata_code.get(user_id, "No Metadata Set")
        
        if dummy_metadata_mode[user_id]:
            await query.message.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}`", 
                                     reply_markup=InlineKeyboardMarkup(TRUE))
        else:
            await query.message.edit(f"Your Current Metadata:-\n\n➜ `{user_metadata}`", 
                                     reply_markup=InlineKeyboardMarkup(FALSE))

    # Set custom metadata
    elif data == 'custom_metadata':
        await query.message.delete()
        try:
            try:
                metadata = await bot.ask(
                    text="**sᴇɴᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ:**", 
                    chat_id=user_id, 
                    filters=filters.text, 
                    timeout=30, 
                    disable_web_page_preview=True)
            except ListenerTimeout:
                return await bot.send_message(user_id, "⚠️ **ʀᴇǫᴜᴇsᴛ  ᴛɪᴍᴇ  ᴏᴜᴛ**\n\nʀᴇsᴛᴀʀᴛ ʙʏ sᴇɴᴅɪɴɢ /metadata")

            # Save dummy metadata
            dummy_metadata_code[user_id] = metadata.text
            await bot.send_message(user_id, "✅ **ᴍᴇᴛᴀᴅᴀᴛᴀ ᴄᴏᴅᴇ sᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!**")
        except Exception as e:
            await bot.send_message(user_id, f"⚠️ **ᴇʀʀᴏʀ:** {str(e)}")
               
