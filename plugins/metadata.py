from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

# Dummy metadata storage
dummy_metadata_mode = {}
dummy_metadata_code = {}

# Default metadata template
DEFAULT_METADATA = """-map 0 -c:s copy -c:a copy -c:v copy \
-metadata title="Powered By:- @Tetris_botz" \
-metadata author="@tetris_admino_bot" \
-metadata:s:s title="Subtitled By :- @Tetris_Botz" \
-metadata:s:a title="By :- @tetris_admino_bot" \
-metadata:s:v title="By:- @Tetris_Botz\""""

# Button layouts
TRUE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏɴ ✅', callback_data='metadata_1')],
        [InlineKeyboardButton('sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

FALSE = [[InlineKeyboardButton('ᴍᴇᴛᴀᴅᴀᴛᴀ ᴏғғ ❌', callback_data='metadata_0')],
         [InlineKeyboardButton('sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ', callback_data='custom_metadata')]]

def validate_metadata(input_text: str) -> bool:
    """Validate metadata structure."""
    required_parts = [
        "-map 0", "-c:s copy", "-c:a copy", "-c:v copy",
        "-metadata title=", "-metadata author=", "-metadata:s:s title=",
        "-metadata:s:a title=", "-metadata:s:v title="
    ]
    return all(part in input_text for part in required_parts)

def update_usernames(template: str, usernames: dict) -> str:
    """Update usernames in the default metadata template."""
    return (
        template.replace("@Tetris_botz", usernames.get("bot", "@Tetris_botz"))
        .replace("@tetris_admino_bot", usernames.get("admin", "@tetris_admino_bot"))
    )

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    """Handle the /metadata command."""
    user_id = message.from_user.id
    current_mode = dummy_metadata_mode.get(user_id, False)
    current_metadata = dummy_metadata_code.get(user_id, DEFAULT_METADATA)

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
        current_metadata = dummy_metadata_code.get(user_id, DEFAULT_METADATA)
        button_layout = InlineKeyboardMarkup(TRUE if dummy_metadata_mode[user_id] else FALSE)
        
        await query.message.edit(f"Your Current Metadata:-\n\n➜ `{current_metadata}`", reply_markup=button_layout)

    elif data == 'custom_metadata':
        await query.message.delete()
        try:
            # Prompt user to send custom metadata
            metadata = await bot.ask(
                text="**Send your custom metadata code (only update the @usernames):**", 
                chat_id=user_id, 
                filters=filters.text, 
                timeout=30
            )
            if not validate_metadata(metadata.text):
                raise ValueError("Invalid metadata structure")
            
            # Extract usernames from the input and update the template
            usernames = {
                "bot": metadata.text.split("@")[1].split(" ")[0],  # First username
                "admin": metadata.text.split("@")[2].split(" ")[0],  # Second username
            }
            updated_metadata = update_usernames(DEFAULT_METADATA, usernames)
            
            # Save the custom metadata
            dummy_metadata_code[user_id] = updated_metadata
            await bot.send_message(user_id, "✅ **Custom metadata set successfully!**")
        except ListenerTimeout:
            await bot.send_message(user_id, "⚠️ **Request timed out. Please try again by sending** /metadata.")
        except ValueError as ve:
            await bot.send_message(user_id, f"⚠️ **Error:** {str(ve)}\n\nPlease follow the correct metadata format.")
        except Exception as e:
            await bot.send_message(user_id, f"⚠️ **Unexpected Error:** {str(e)}")
                
