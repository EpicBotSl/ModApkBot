import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

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


start_menu = ReplyKeyboardMarkup(
      [
            ["🤴 OWNER 🤴"],
            ["💻 Bot Devs 💻", "👮‍♂️ MemeHub Admins 👮‍♂️"],
            ["📊 Statistics"]
           
        ],
        resize_keyboard=True  # Make the keyboard smaller
    )

print("Buttons & message py started🔥")
