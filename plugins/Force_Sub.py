from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import db

async def not_subscribed(_, client, message):
    await db.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status in {enums.ChatMemberStatus.BANNED, enums.ChatMemberStatus.LEFT}:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [
        [InlineKeyboardButton(text="🛸ᴜᴘᴅᴀᴛᴇ  ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Config.FORCE_SUB}")],
        [InlineKeyboardButton(text="♻️ᴛʀʏ  ᴀɢᴀɪɴ", url="https://t.me/Thumbnail_editor_4gb_bot?start=1234567890")]
    ]
    text = "**ᴛᴏ  ᴘʀᴇᴠᴇɴᴛ  ᴏᴠᴇʀʟᴏᴀᴅ  ᴏɴʟʏ  ᴏᴜʀ  ᴄʜᴀɴɴᴇʟ  ᴜsᴇʀs  ᴄᴀɴ  ᴜsᴇ  ᴛʜɪs  ʙᴏᴛ,  ʙᴜᴛ  ᴜ ʀ  ɴᴏᴛ \n\nᴊᴏɪɴ  ᴏᴜʀ  ᴄʜᴀɴɴᴇʟ  ᴀɴᴅ  ᴄʟɪᴄᴋ  ᴛʀʏ  ᴀɢᴀɪɴ**"
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ")  
        elif user.status == enums.ChatMemberStatus.LEFT:
            return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
