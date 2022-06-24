#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu

import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *


HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
API_ID = int(os.getenv("API_ID"))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH")  # from https://my.telegram.org/apps
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1884885842 5115331277 5025877489 1202064253 1120271521").split())
MONGO_URI = os.getenv("MONGO_URI")

#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu
START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🍁 Owner 🍁', user_id="@N_Abeysinghe_2001")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp"),
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/TeamAlphaTg/MemehubtgSl_Bot")
                 ],
                 [
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ➕", switch_inline_query="share"),
                 InlineKeyboardButton("➕ sʜᴀʀᴇ ᴄʜɴʟ ➕", switch_inline_query="cshare")
                 ]]
                  )


