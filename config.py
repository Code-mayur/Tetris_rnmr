

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
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/06_.jpg")
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

    ABOUT_TXT = """**ᴄʜᴏᴏsᴇ  ᴀ  ᴘʟᴀɴ  ғʀᴏᴍ  👇🏻ʙᴇʟᴏᴡ  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ʙᴜʏ,  ᴘʟᴀɴ  ᴅᴇᴛᴀɪʟs  ɢɪᴠᴇɴ  ɪɴ  ɴᴇxᴛ  ᴘᴀɢᴇ**

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

🎉Offer -  first  time  buyers  gets  extra  days

**ᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ  ᴛᴏ  ʙᴜʏ  ᴘʀᴇᴍɪᴜᴍ  ᴘʟᴀɴ**
    """
    
    FIF = """
**🏷️ ʏᴏᴜʀ  sᴇʟᴇᴄᴛᴇᴅ  ᴘʟᴀɴ -  ᴘʀᴇᴍɪᴜᴍ
🏷️ sᴇʟᴇᴄᴛᴇᴅ  ᴠᴀʟɪᴅɪᴛʏ** -  15 **ᴅᴀʏs
🏷️ ᴛᴏᴛᴀʟ  ᴄᴏsᴛ** - 3️⃣9️⃣₹ (0.6$)

**🪧ʙᴇɴᴇғɪᴛs -
     ~ [ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ᴛᴏ  ᴋɴᴏᴡ](https://telegra.ph/Utxgucyifoy-09-17)
     ᴏʀ ~ ᴄʜᴇᴄᴋ  ᴀʙᴏᴠᴇ  ᴘɪᴄᴛᴜʀᴇ

ɴᴏᴡ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ  ʙʏ  ᴄʟɪᴄᴋɪɴɢ  ʙᴇʟᴏᴡ .  ᴀɴᴅ  ᴀғᴛᴇʀ  ᴄᴏᴍᴘʟᴇᴛɪɴɢ  ᴘᴀʏᴍᴇɴᴛ   ᴄʟɪᴄᴋ   "ᴘᴀɪᴅ✅"  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ᴄᴏɴғɪʀᴍ  ᴘᴜʀᴄʜᴀsᴇ** \nany  payment  related  issue  contact  [admin](https://t.me/tetris_admino_bot)  for  help
"""

    MON = """
**🏷️ ʏᴏᴜʀ  sᴇʟᴇᴄᴛᴇᴅ  ᴘʟᴀɴ -  ᴘʀᴇᴍɪᴜᴍ
🏷️ sᴇʟᴇᴄᴛᴇᴅ  ᴠᴀʟɪᴅɪᴛʏ** -  1 **ᴍᴏɴᴛʜ
🏷️ ᴛᴏᴛᴀʟ  ᴄᴏsᴛ** - 5️⃣9️⃣₹ (1$)

**🪧ʙᴇɴᴇғɪᴛs -
     ~ [ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ᴛᴏ  ᴋɴᴏᴡ](https://telegra.ph/Utxgucyifoy-09-17)
     ᴏʀ  ~ ᴄʜᴇᴄᴋ  ᴀʙᴏᴠᴇ  ᴘɪᴄᴛᴜʀᴇ

ɴᴏᴡ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ  ʙʏ  ᴄʟɪᴄᴋɪɴɢ  ʙᴇʟᴏᴡ .   ᴀɴᴅ  ᴀғᴛᴇʀ  ᴄᴏᴍᴘʟᴇᴛɪɴɢ  ᴘᴀʏᴍᴇɴᴛ   ᴄʟɪᴄᴋ   "ᴘᴀɪᴅ✅"  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ᴄᴏɴғɪʀᴍ  ᴘᴜʀᴄʜᴀsᴇ** \nany  payment  related  issue  contact  [admin](https://t.me/tetris_admino_bot)  for  help
"""

    TMON = """
**🏷️ ʏᴏᴜʀ  sᴇʟᴇᴄᴛᴇᴅ  ᴘʟᴀɴ -  ᴘʀᴇᴍɪᴜᴍ
🏷️ sᴇʟᴇᴄᴛᴇᴅ  ᴠᴀʟɪᴅɪᴛʏ** -  3 **ᴍᴏɴᴛʜ
🏷️ ᴛᴏᴛᴀʟ  ᴄᴏsᴛ** - 1️⃣5️⃣9️⃣₹ (2.5$)

**🪧ʙᴇɴᴇғɪᴛs -
     ~ [ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ᴛᴏ  ᴋɴᴏᴡ](https://telegra.ph/Utxgucyifoy-09-17)
     ᴏʀ  ~ ᴄʜᴇᴄᴋ  ᴀʙᴏᴠᴇ  ᴘɪᴄᴛᴜʀᴇ

ɴᴏᴡ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ  ʙʏ  ᴄʟɪᴄᴋɪɴɢ  ʙᴇʟᴏᴡ .   ᴀɴᴅ  ᴀғᴛᴇʀ  ᴄᴏᴍᴘʟᴇᴛɪɴɢ  ᴘᴀʏᴍᴇɴᴛ   ᴄʟɪᴄᴋ   "ᴘᴀɪᴅ✅"  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ᴄᴏɴғɪʀᴍ  ᴘᴜʀᴄʜᴀsᴇ** \nany  payment  related  issue  contact  [admin](https://t.me/tetris_admino_bot)  for  help
"""

    TIF = """
**🏷️ ʏᴏᴜʀ  sᴇʟᴇᴄᴛᴇᴅ  ᴘʟᴀɴ -  ʙᴜɴᴅʟᴇ
🏷️ sᴇʟᴇᴄᴛᴇᴅ  ᴠᴀʟɪᴅɪᴛʏ** -  2 **ᴍᴏɴᴛʜ
🏷️ ᴛᴏᴛᴀʟ  ᴄᴏsᴛ** - 1️⃣3️⃣9️⃣₹ (2$)

**🪧ʙᴇɴᴇғɪᴛs -
     ~ ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ  ᴘʀᴇᴍɪᴜᴍ  ᴀᴄᴄᴇss
                   +
     ~ ғɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ʙᴏᴛ  ᴀᴄᴄᴇss  
     ~[ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ᴛᴏ  ᴋɴᴏᴡ  ᴍᴏʀᴇ](https://telegra.ph/bundle-plan-features-09-18)

ɴᴏᴡ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ  ʙʏ  ᴄʟɪᴄᴋɪɴɢ  ʙᴇʟᴏᴡ .   ᴀɴᴅ  ᴀғᴛᴇʀ  ᴄᴏᴍᴘʟᴇᴛɪɴɢ  ᴘᴀʏᴍᴇɴᴛ   ᴄʟɪᴄᴋ   "ᴘᴀɪᴅ✅"  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ᴄᴏɴғɪʀᴍ  ᴘᴜʀᴄʜᴀsᴇ** \nany  payment  related  issue  contact  [admin](https://t.me/tetris_admino_bot)  for  help
"""

    FMON = """
**🏷️ ʏᴏᴜʀ  sᴇʟᴇᴄᴛᴇᴅ  ᴘʟᴀɴ -  ʙᴜɴᴅʟᴇ
🏷️ sᴇʟᴇᴄᴛᴇᴅ  ᴠᴀʟɪᴅɪᴛʏ** -  4 **ᴍᴏɴᴛʜ
🏷️ ᴛᴏᴛᴀʟ  ᴄᴏsᴛ** -  2️⃣4️⃣9️⃣₹ (3.7$)

**🪧ʙᴇɴᴇғɪᴛs -
     ~ ʀᴇɴᴀᴍᴇʀ  ʙᴏᴛ  ᴘʀᴇᴍɪᴜᴍ  ᴀᴄᴄᴇss
                   +
     ~ ғɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ʙᴏᴛ  ᴀᴄᴄᴇss  
     ~[ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ᴛᴏ  ᴋɴᴏᴡ  ᴍᴏʀᴇ](https://telegra.ph/bundle-plan-features-09-18)

ɴᴏᴡ  ᴍᴀᴋᴇ  ᴘᴀʏᴍᴇɴᴛ  ʙʏ  ᴄʟɪᴄᴋɪɴɢ  ʙᴇʟᴏᴡ .   ᴀɴᴅ  ᴀғᴛᴇʀ  ᴄᴏᴍᴘʟᴇᴛɪɴɢ  ᴘᴀʏᴍᴇɴᴛ   ᴄʟɪᴄᴋ   "ᴘᴀɪᴅ✅"  ʙᴜᴛᴛᴏɴ  ᴛᴏ  ᴄᴏɴғɪʀᴍ  ᴘᴜʀᴄʜᴀsᴇ** \nany  payment  related  issue  contact  [admin](https://t.me/tetris_admino_bot)  for  help
"""
    
    TIME = """
**ᴄʜᴏᴏsᴇ  ᴠᴀʟɪᴅɪᴛʏ  ғᴏʀ  ʏᴏᴜʀ  ᴘʟᴀɴ  ғʀᴏᴍ  ʙᴇʟᴏᴡ👇  ʙᴜᴛᴛᴏɴ,  ᴘʟᴀɴ  ᴅᴇᴛᴀɪʟs  ᴀʙᴏᴠᴇ**☝🏻

note-  automated  payment  interface  is  active
"""
    BTIME = """
**ɴᴏᴛ  ᴀᴠᴀɪʟᴀʙʟᴇ  ʀɪɢʜᴛ  ɴᴏᴡ,  ᴄᴏᴍᴍɪɴɢ  sᴏᴏɴ....**☝🏻

note-  dont  subscribe  this, way  back  to  home 
"""
    BOT_STATUS = """
**ʙᴏᴛ  ᴇɴɢᴀɢᴇᴍᴇɴᴛ  ᴅᴀᴛᴀ** v-4.5.7

- version cheked `{}` ago
- `{}` users started the bot till now
- `{}` users active live now
- avrg 346 regular users
- `{}` spaces held in bot
- `{}` cache ready to clear

**ᴅᴀᴛᴀs  ᴀʀᴇ  ʀᴇᴀʟ  ᴛɪᴍᴇ  ᴜᴘᴅᴀᴛᴇᴅ**
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
    # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️

    

    BOTS = """
**ᴛʀʏ  ᴛʜᴇsᴇ  ᴜsᴇғᴜʟʟ  ʙᴏᴛs,  ᴅᴇᴛᴀɪʟs  ʜᴇʀᴇ**

⭕️**ɪɴsᴛᴀ  ᴅᴏᴡɴʟᴏᴀᴅᴇʀ  ʙᴏᴛ** 
- download  instagram  post , reel , story 
- just  send  public  account  link

⭕️**ᴍᴏʀᴇ  ᴄᴏᴍᴍɪɴɢ  sᴏᴏɴ**
- bla  bla  bla  bla  bla  bla  bla
- aah raha  hai  jaldi

**ᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ  ᴛᴏ  ᴇxᴘʟᴏʀᴇ  ᴛʜᴏsᴇ  ʙᴏᴛs**
"""
    
    RKN_PROGRESS = """<b>\n
[🧨](https://telegra.ph/file/a10607f63654828a06194.mp4)**sᴘᴇᴇᴅ-** {3}/s                    [unlock 2x speed](https://telegra.ph/How-to-increase-speed-08-28)
📦**ꜱɪᴢᴇ-**  {1} of {2}
⏳**ᴇᴛᴀ-**  {4}"""

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
