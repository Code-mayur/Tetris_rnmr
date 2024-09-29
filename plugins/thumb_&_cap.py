

from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    if len(message.command) == 1:
       return await rkn.edit("**sᴇɴᴅ  ᴛᴇxᴛ  ᴛᴏ  sᴇᴛ  ᴀs  ᴀ  ᴄᴀᴘᴛɪᴏɴ**\n\n**ᴇxᴀᴍᴩʟᴇ**:- `/set_caption {filename}\n\n**sɪᴢᴇ**: {filesize}\n\n**ᴅᴜʀᴀᴛɪᴏɴ**: {duration}`\n\n#ad\nreserve for ad")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await rkn.edit("**ᴛʜɪs  ᴛᴇxᴛ  ɪs  sᴀᴠᴇᴅ  ᴀs  ᴀ  ᴄᴀᴘᴛɪᴏɴ** ☑️\n\n#ad\nreserve for ad")
   
@Client.on_message(filters.private & filters.command(['del_caption', 'delete_caption', 'delcaption']))
async def delete_caption(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await rkn.edit("**✖️ɴᴏ  ᴄᴀᴘᴛɪᴏɴ  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  ᴄᴀᴘᴛɪᴏɴ**\n\n#ad\nreserve for ad")
    await db.set_caption(message.from_user.id, caption=None)
    await rkn.edit("**ᴄᴀᴘᴛɪᴏɴ  ᴅᴇʟᴇᴛᴇᴅ🚫,  sᴇᴛ  ᴀ  ɴᴇᴡ  ᴏɴᴇ**\n\n#ad\nreserve for ad")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await rkn.edit(f"**ᴄᴜʀʀᴇɴᴛ ᴄᴀᴩᴛɪᴏɴ:-**\n\n`{caption}` \n\n#ad\nreserve for ad")
    else:
       await rkn.edit("**✖️ɴᴏ  ᴄᴀᴘᴛɪᴏɴ  sᴀᴠᴇᴅ, ғɪʀsᴛ  sᴇᴛ  ᴀ  ᴄᴀᴘᴛɪᴏɴ**\n\n#ad\nreserve for ad")

@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await client.send_photo(chat_id=message.chat.id, photo=thumb)
        await rkn.delete()
    else:
        await rkn.edit("**✖️ɴᴏ  ᴛʜᴜᴍʙɴᴀɪʟ  sᴀᴠᴇᴅ, sᴇɴᴅ  ᴀ  ᴘɪᴄᴛᴜʀᴇ**\n\n#ad\nreserve for ad") 
		
@Client.on_message(filters.private & filters.command(['del_thumb', 'delete_thumb', 'delthumb']))
async def removethumb(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await db.set_thumbnail(message.from_user.id, file_id=None)
        await rkn.edit("**ᴛʜᴜᴍʙɴᴀɪʟ  ᴅᴇʟᴇᴛᴇᴅ🚫,  sᴇᴛ  ᴀ  ɴᴇᴡ  ᴏɴᴇ**\n\n#ad\nreserve for ad")
        return
    await rkn.edit("**✖️ɴᴏ  ᴛʜᴜᴍʙɴᴀɪʟ  sᴀᴠᴇᴅ, sᴇɴᴅ  ᴀ  ᴘɪᴄᴛᴜʀᴇ**\n\n#ad\nreserve for ad**")


@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    rkn = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ......**")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await rkn.edit("**ᴛʜɪs  ᴘʜᴏᴛᴏ  ɪs  sᴀᴠᴇᴅ  ᴀs  ᴀ  ᴛʜᴜᴍʙɴᴀɪʟ** <blockquote expandable>ugxicutxutciycigchichivigviyviyciycyucyucyuvuycyucigcgicgivhivyivyivgvyicyicugcucugcgucugcuyvigcgucugcugcugcugcutctucugcutcugcugcutcutcugcugcugcucucugcuggccjg</blockquote> ☑️\n\n#ad\nreserve for ad")


