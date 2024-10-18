

from pyrogram import Client, filters, enums
from helper.database import db

# prefix commond ✨
@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_prefix(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**sᴇɴᴅ  ᴛᴇxᴛ  ᴛᴏ  sᴇᴛ  ᴀs  ᴘʀᴇғғɪx\n\nᴇxᴀᴍᴩʟᴇ**:- `/set_prefix @usernams`")
    prefix = message.text.split(" ", 1)[1]
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ.....**", reply_to_message_id=message.id)
    await db.set_prefix(message.from_user.id, prefix)
    await RknDev.edit("**ᴘʀᴇғғɪx  sᴀᴠᴇᴅ, ᴇᴅɪᴛ  ᴀ  ғɪʟᴇ  ᴛᴏ  sᴇᴇ** ☑️")

@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ.....**", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await RknDev.edit("**✖️ɴᴏ  ᴘʀᴇғғɪx  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  ᴘʀᴇғɪx**")
    await db.set_prefix(message.from_user.id, None)
    await RknDev.edit("**ᴘʀᴇғғɪx  ᴅᴇʟᴇᴛᴇᴅ🚫, sᴇᴛ  ᴀ  ɴᴇᴡ  ᴏɴᴇ**")

@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_prefix(client, message):
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ.....**", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await RknDev.edit(f"**ʏᴏᴜʀ ᴘʀᴇꜰɪx:-**\n\n`{prefix}`")
    else:
        await RknDev.edit("**✖️ɴᴏ  ᴘʀᴇғғɪx  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  ᴘʀᴇғɪx**")

# SUFFIX COMMOND ✨
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_suffix(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**sᴇɴᴅ  ᴛᴇxᴛ  ᴛᴏ  sᴇᴛ  ᴀs  sᴜғғɪx**\n\n**ᴇxᴀᴍᴩʟᴇ**:- `/set_suffix @channel_username`")
    suffix = message.text.split(" ", 1)[1]
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ.....**", reply_to_message_id=message.id)
    await db.set_suffix(message.from_user.id, suffix)
    await RknDev.edit("**sᴜғғɪx  sᴀᴠᴇᴅ, ᴇᴅɪᴛ  ᴀ  ғɪʟᴇ  ᴛᴏ  sᴇᴇ** ☑️")

@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if not suffix:
        return await RknDev.edit("**✖️ɴᴏ  sᴜғғɪx  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  sᴜғғɪx**")
    await db.set_suffix(message.from_user.id, None)
    await RknDev.edit("**sᴜғғɪx  ᴅᴇʟᴇᴛᴇᴅ🚫, sᴇᴛ  ᴀ  ɴᴇᴡ  ᴏɴᴇ**")

@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_suffix(client, message):
    RknDev = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**", reply_to_message_id=message.id)
    suffix = await db.get_suffix(message.from_user.id)
    if suffix:
        await RknDev.edit(f"**ᴄᴜʀʀᴇɴᴛ  ꜱᴜꜰꜰɪx:-**\n\n`{suffix}`")
    else:
        await RknDev.edit("**✖️ɴᴏ  sᴜғғɪx  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  sᴜғғɪx**")

