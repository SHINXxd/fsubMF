import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "27570599"))
  API_HASH = os.environ.get("API_HASH", "0329a786739cb73a2b1176582c5e8376")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6847882710:AAHDlPscai2YcU_TakwduvljH35IbX2uXTs")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@JirayaSage_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001829601382"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "Nono")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "None")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "5468078784"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://lodukuwaraboy:Qwerty12@cluster0.mfey0ob.mongodb.net/?retryWrites=true&w=majority")
  FORCE_SUB_CHANNELS = [-1001811788351, -1002132279172, -1002127474493, -1002039598333]
  #FORCE_SUB_CHANNELS =[int(x) for x in os.environ.get("UPDATES_CHANNEL", "").split(",") if x]
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001991863694"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/KingVj01)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/KingVj01)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
