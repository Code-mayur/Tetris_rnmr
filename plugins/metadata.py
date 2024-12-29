from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

# Dummy metadata storage
dummy_metadata_mode = {}
dummy_metadata_code = {}

# Button layouts
TRUE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ ✅', callback_data='metadata_1')],
        [InlineKeyboardButton('sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

FALSE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏғғ ❌', callback_data='metadata_0')],
         [InlineKeyboardButton('sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    """Handle the /metadata command."""
    user_id = message.from_user.id
    current_mode = dummy_metadata_mode.get(user_id, False)
    current_metadata = dummy_metadata_code.get(user_id, "No Metadata Set")
    
    button_layout = InlineKeyboardMarkup(TRUE if current_mode else FALSE)
    await message.reply_text(f"Your Current Metadata:-\n\n➜ `{current_metadata}`", reply_markup=button_layout)

@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    """Handle metadata toggle and custom metadata input."""
    user_id = query.from_user.id
    data = query.data

    if data.startswith('metadata_'):
        # Toggle metadata mode
        is_metadata_on = data.split('_')[1] == "1"
        dummy_metadata_mode[user_id] = not is_metadata_on
        
        # Get current metadata and update button layout
        current_metadata = dummy_metadata_code.get(user_id, "No Metadata Set")
        button_layout = InlineKeyboardMarkup(TRUE if dummy_metadata_mode[user_id] else FALSE)
        
        await query.message.edit(f"Your Current Metadata:-\n\n➜ `{current_metadata}`", reply_markup=button_layout)

    elif data == 'custom_metadata':
        await query.message.delete()
        try:
            # Prompt user to send custom metadata
            metadata = await bot.ask(
                text="**Send your custom metadata code:**", 
                chat_id=user_id, 
                filters=filters.text, 
                timeout=30
            )
            # Save the custom metadata
            dummy_metadata_code[user_id] = metadata.text
            await bot.send_message(user_id, "✅ **Custom metadata set successfully!**")
        except ListenerTimeout:
            await bot.send_message(user_id, "⚠️ **Request timed out. Please try again by sending** /metadata.")
        except Exception as e:
            await bot.send_message(user_id, f"⚠️ **Error:** {str(e)}")
                 
