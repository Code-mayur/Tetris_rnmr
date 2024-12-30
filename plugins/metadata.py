from datetime import datetime, timedelta
from pyrogram import Client, filters
from helper.database import db
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
    required_parts = ["-map 0", "-c:s copy", "-c:a copy", "-c:v copy", "-metadata"]
    return all(part in input_text for part in required_parts)

@Client.on_message(filters.private & filters.command('metadata'))
async def handle_metadata(bot: Client, message: Message):
    """Handle the /metadata command."""
    user_id = message.from_user.id
    current_mode = dummy_metadata_mode.get(user_id, False)
    current_metadata = dummy_metadata_code.get(user_id, DEFAULT_METADATA)

    button_layout = InlineKeyboardMarkup(TRUE if current_mode else FALSE)
    await message.reply_text(
        f"**ʏᴏᴜʀ  ᴄᴜʀʀᴇɴᴛ  ᴍᴇᴛᴀᴅᴀᴛᴀ**:-\n\n➜ `{current_metadata}` \n\n**ʀᴇsᴇᴛ  ᴅᴀɪʟʏ  sᴏ  ᴘʟᴇᴀsᴇ  ᴄʜᴇᴄᴋ  ʙᴇғᴏʀᴇ  ᴇᴅɪᴛ**",
        reply_markup=button_layout
    )

@Client.on_callback_query(filters.regex('.*?(custom_metadata|metadata).*?'))
async def query_metadata(bot: Client, query: CallbackQuery):
    """Handle metadata toggle and custom metadata input."""
    user_id = query.from_user.id
    data = query.data

    # Check if the user has premium access
    is_premium = await db.has_premium_access(user_id)

    if data.startswith('metadata_'):
        if not is_premium:
            # Restrict toggle for non-premium users
            await query.answer("❌ Only premium users can use metadata features", show_alert=True)
            return

        # Toggle metadata mode for premium users
        is_metadata_on = data.split('_')[1] == "1"
        dummy_metadata_mode[user_id] = not is_metadata_on

        # Get current metadata and update button layout
        current_metadata = dummy_metadata_code.get(user_id, DEFAULT_METADATA)
        button_layout = InlineKeyboardMarkup(TRUE if dummy_metadata_mode[user_id] else FALSE)

        await query.message.edit(
            f"**ʏᴏᴜʀ  ᴄᴜʀʀᴇɴᴛ  ᴍᴇᴛᴀᴅᴀᴛᴀ:-\n\n➜ `{current_metadata}`  \n\n**ʀᴇsᴇᴛ  ᴅᴀɪʟʏ  sᴏ  ᴘʟᴇᴀsᴇ  ᴄʜᴇᴄᴋ  ʙᴇғᴏʀᴇ  ᴇᴅɪᴛ**",
            reply_markup=button_layout
        )

    elif data == 'custom_metadata':
        if not is_premium:
            # Restrict custom metadata for non-premium users
            await query.answer("❌ Only premium users can set custom metadata.", show_alert=True)
            return

        await query.message.delete()
        try:
            # Prompt user to send custom metadata
            metadata = await bot.ask(
                text=(
                    "**sᴇɴᴅ  ʏᴏᴜʀ  ᴄᴜsᴛᴏᴍ  ᴍᴇᴛᴀᴅᴀᴛᴀ  ᴄᴏᴅᴇ\n\nᴇx -**  `-map 0 -c:s copy -c:a copy -c:v copy -metadata title=Powered By:- @Tetris_botz -metadata author= @tetris_admino_bot -metadata:s:s title= Subtitled By :- @Tetris_Botz -metadata:s:a title= audio By :- @tetris_admino_bot -metadata:s:v title= video by :- @Tetris_Botz`\n\n"
                    "➔ Maintain the required format.\n"
                    "➔ You can customize fields like `title`, `author`, etc."
                ),
                chat_id=user_id,
                filters=filters.text,
                timeout=60
            )
            if not validate_metadata(metadata.text):
                raise ValueError("**❌ ɪɴᴠᴀʟɪᴅ  ᴍᴇᴛᴀᴅᴀᴛᴀ  ᴄᴏᴅᴇ  sᴛʀᴜᴄᴛᴜʀᴇ , ᴘʟᴇᴀsᴇ  ᴅᴏ  ᴛʜᴇ  ᴘʀᴏᴄᴇss  ᴀɢᴀɪɴ**")

            # Save the custom metadata
            dummy_metadata_code[user_id] = metadata.text.strip()
            await bot.send_message(user_id, "✅ **ᴄᴏᴅᴇ  ɪs  ᴅᴇᴛᴇᴄᴛᴇᴅ  ᴀɴᴅ  sᴇᴛ  sᴜᴄᴄᴇssғᴜʟʟʏ**")
        except ListenerTimeout:
            await bot.send_message(user_id, "⚠️ **ʀᴇǫᴜᴇsᴛ  ᴛɪᴍᴇᴅ  ᴏᴜᴛ  ᴘʟᴇᴀsᴇ  ᴅᴏ  ᴛʜᴇ  ᴘʀᴏᴄᴇss  ᴀɢᴀɪɴ  ʙʏ  sᴇɴᴅɪɴɢ** /metadata  **ᴄᴍɴᴅ**")
        except ValueError as ve:
            await bot.send_message(user_id, f"⚠️ **Error:** {str(ve)}\n\nPlease follow the correct metadata format.")
        except Exception as e:
            await bot.send_message(user_id, f"⚠️ **Unexpected Error:** {str(e)}")
                
