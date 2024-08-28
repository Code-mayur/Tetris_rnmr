# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "23223511")
    API_HASH = os.environ.get("API_HASH", "c2207a11155ad050097e981fdd5fd0b1")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Digital")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://accessgithubf9:cgQbxuobUnCbH2F7@cluster0.ym73ib5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/97923b811ead934c30723.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7167553626').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002166385101"))

    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "tetris_botz")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "tetris_botz")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()

class rkn(object):
    # part of text configuration
    START_TXT = """#ad
reserve for ad

**ᴀ  ғᴀsᴛ  ʀᴇɴᴀᴍᴇʀ🛩️  ʙᴏᴛ  ᴡɪᴛʜ  sᴏᴍᴇ  ᴛᴏᴏʟs  ᴛᴏ  ᴇᴅɪᴛ✏️ , ᴄᴏɴᴠᴇʀᴛ  ғɪʟᴇ  ᴛᴏ  ᴠɪᴅᴇᴏ , ᴄʜᴀɴɢᴇ  ᴛʜᴜᴍʙɴᴀɪʟ🖥️ , ᴄᴀᴘᴛɪᴏɴ  ᴏғ  ᴀ  ᴠɪᴅᴇᴏ  ᴏʀ  ᴀᴜᴅɪᴏ  ғɪʟᴇ

✌🏻ʜɪ  {}  sᴇɴᴅ  ғɪʟᴇ  ᴛᴏ  ᴇᴅɪᴛ**"""

    ABOUT_TXT = """**ᴄʜᴏᴏsᴇ  ᴀ  ᴘʟᴀɴ  ғʀᴏᴍ  👇🏻ʙᴇʟᴏᴡ  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ʙᴜʏ,  ᴘʟᴀɴ  ᴅᴇᴛᴀɪʟs  ᴀʀᴇ  ʜᴇʀᴇ☝🏻**

note-  automated  payment  interface  is  active"""

    HELP_TXT = """
**ɴᴏᴛ  ᴀ  ʀᴏᴄᴋᴇᴛ  sᴄɪᴇɴᴄᴇ  , sᴏ  ɴᴏ  ᴛᴜᴛᴏʀɪᴀʟ**  

- just send a video or audio file , bot will ask to type a new name
-choose the output file format , boom now wait 

**ᴀʟsᴏ  ᴜsᴇ  ᴄᴏᴍᴍᴀɴᴅs  ᴀɴᴅ  ᴇxᴘʟᴏʀᴇ  ʜᴇʀᴇ👇🏻**
"""

    UPGRADE= """
**<u>ɢᴇᴛ  ᴘʀᴇᴍɪᴜᴍ  ᴛᴏ  ᴜɴʟᴏᴄᴋ  ғᴇᴀᴛᴜʀᴇs
ᴄʜᴇᴄᴋ  ᴏᴜʀ  ᴀғғᴏʀᴅᴀʙʟᴇ  ᴘʟᴀɴ  ᴀʙᴏᴠᴇ</u>**

try premium lite plan free only for new users

**ᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ  ᴛᴏ  ʙᴜʏ  ᴘʀᴇᴍɪᴜᴍ  ᴘʟᴀɴ**
    """
    THUMBNAIL = """
**ʏᴏᴜʀ  ᴄʜᴏᴏsᴇɴ  ᴘʟᴀɴ - ʟɪᴛᴇ
ᴘʀɪᴄᴇ** - 39₹ (0.7$) / **ᴍᴏɴᴛʜ**

ʙᴇɴᴇғɪᴛs** -
     ~ auto & manual thumbnail 
     ~ upto 2gb file support
     ~ 1x speed
     ~ perform multiple task 
     ~ Daily 30 limited task
     ~ mkv, mp4 optimization
     ~ file to video convert
     ~ caption , metadata support
     ~ prefix , suffix support

**ᴄʟɪᴄᴋ  'ᴘʀᴏᴄᴇᴇᴅ  ᴛᴏ  ᴘᴀʏᴍᴇɴᴛ'  ғᴏʀ  ɴᴇxᴛ**
"""
    CAPTION= """
**ʏᴏᴜʀ  ᴄʜᴏᴏsᴇɴ  ᴘʟᴀɴ - ᴘʀᴏ
ᴘʀɪᴄᴇ -** 69₹ (1.3$)/ **ᴍᴏɴᴛʜ**

**ʙᴇɴᴇғɪᴛs** -
     ~ upto 4gb file support
     ~ 3x speed
     ~ Daily unlimited task
     ~ multiple task simultaneously 
     ~ auto + manual thumbnail 
     ~ mkv, mp4 optimization
     ~ file to video convert
     ~ caption , metadata support
     ~ prefix , suffix support
     ~ pro features

**ᴄʟɪᴄᴋ  'ᴘʀᴏᴄᴇᴇᴅ  ᴛᴏ  ᴘᴀʏᴍᴇɴᴛ'  ғᴏʀ  ɴᴇxᴛ**
"""
    BOT_STATUS = """
**ʙᴏᴛ  ᴇɴɢᴀɢᴇᴍᴇɴᴛ  ᴅᴀᴛᴀ** v-4.3.0

- last updated `{}` ago
- `{}` users started the bot till now
- avrg *** regular users 
- `{}` premium subscribers 
- `{}` spaces held in bot
- `{}` cache ready to clear

ᴅᴀᴛᴀs  ᴀʀᴇ  ʀᴇᴀʟ  ᴛɪᴍᴇ  ᴜᴘᴅᴀᴛᴇᴅ
"""

    DIGITAL_METADATA = """
**ᴍᴇᴛᴀᴅᴀᴛᴀ  sᴇᴛᴛɪɴɢ  ᴛᴜᴛᴏʀɪᴀʟ**

~ use /metadata cmd to change and set metadata of your file

**ғᴏʀ ᴇxᴀᴍᴘʟᴇ**:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @channel_username" -metadata author="@your_username" -metadata:s:s title="Subtitled By :- @channel_username" -metadata:s:a title="By :- @your_username" -metadata:s:v title="By:- @channel" </code>

📥**ғᴏʀ ʜᴇʟᴘ ᴄᴏɴᴛ.** @tetris_botz
"""
    
    CUSTOM_FILE_NAME = """
**ᴄᴜsᴛᴏᴍ  ғɪʟᴇ  ɴᴀᴍᴇ  ᴜsɪɴɢ  ᴘʀᴇғɪx/sᴜғғɪx**

~ use /set_prefix cmd to add a prefix along with your filename
~ use /see_prefix cmd to see current prefix
~ use /del_prefix cmd to delete current prefix
~ use /set_suffix cmd to add a suffix along with your filename
~ use /see_suffix cmd to see current suffix
~ use /del_suffix cmd to delete current suffix

**ᴇxᴀᴍᴩʟᴇ**:- `/set_suffix @channel`
**ᴇxᴀᴍᴩʟᴇ**:- `/set_prefix @channel`
"""
    
    #⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @RknDeveloper🙏🥲
    # ᴡʜᴏᴇᴠᴇʀ ɪs ᴅᴇᴘʟᴏʏɪɴɢ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴡᴀʀɴᴇᴅ ⚠️ ᴅᴏ ɴᴏᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛs ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʀᴇᴘᴏ #ғɪʀsᴛ ᴀɴᴅ ʟᴀsᴛ ᴡᴀʀɴɪɴɢ ⚠️
    DEV_TXT = """use our bot **sᴘᴏᴛ** and  **sᴛᴀʀᴛ  ᴘɪᴄ** to advertise your content 👆🏻**ʟɪᴋᴇ  ᴛʜɪs**

starting at only **7ʀs / ᴅᴀʏ**

contact  **ᴀᴅᴍɪɴ**  for more info and payment

click 👇🏻here to check bot users engagement """
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    PRO = """
Your  choosen  plan -  ᴘʀᴏ
duration - 1 month

**<u>ɴᴏᴡ  sᴄᴀɴ  ʙᴇʟᴏᴡ  ǫʀ  ᴄᴏᴅᴇ  &  ᴘᴀʏ  ᴛʜᴇ  ᴇxᴀᴄᴛ  ᴘʟᴀɴ  ᴀᴍᴏᴜɴᴛ  👇🏻sʜᴏᴡɪɴɢ  ʜᴇʀᴇ</u>

ᴀᴍᴏᴜɴᴛ  ᴛᴏ  ʙᴇ  ᴘᴀɪᴅ** - 6️⃣9️⃣₹ 

🎉**offer**🎉 - pay 207₹ for 3 month validity & get 20 days free

**ᴀғᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ👇🏻  ʙᴜᴛᴛᴏɴ**
"""

    LITE = """
Your  choosen  plan -  ʟɪᴛᴇ
duration - 1 month

**ɴᴏᴡ  sᴄᴀɴ  ʙᴇʟᴏᴡ  ǫʀ  ᴄᴏᴅᴇ  &  ᴘᴀʏ  ᴛʜᴇ  ᴇxᴀᴄᴛ  ᴘʟᴀɴ  ᴀᴍᴏᴜɴᴛ  sʜᴏᴡɪɴɢ  ʜᴇʀᴇ👇🏻

ᴀᴍᴏᴜɴᴛ  ᴛᴏ  ʙᴇ  ᴘᴀɪᴅ** - 3️⃣9️⃣₹ 

🎉**offer**🎉 - pay 234₹ for 6 month validity & get 1 month free

**ᴀғᴛᴇʀ  ᴘᴀʏᴍᴇɴᴛ  ᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ👇🏻  ʙᴜᴛᴛᴏɴ**
"""
    
    RKN_PROGRESS = """<b>\n
🧨**sᴘᴇᴇᴅ-** {3}/s                           unlock 2x speed
📦**ꜱɪᴢᴇ-**  {1} of {2}
[⏳](https://telegra.ph/file/a10607f63654828a06194.mp4)**ᴇᴛᴀ-**  {4}"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
