import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu
START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('🆘HELP🆘', callback_data="HELP")
                 ],
                 [
                 InlineKeyboardButton(text="</ᴇᴘɪᴄ ʙᴏᴛs <s/ʟ>🇱🇰", url="https://t.me/EpicBotsSl"),
                 InlineKeyboardButton("⛱️SUPPORT ⛱️", url="https://t.me/EpicChats")
                 ],
                 [
                 InlineKeyboardButton("🔥BOT DEVELOPERS🔥", callback_data="DEVS")
                 ]]
                  )

CLOSE_BUTTON = InlineKeyboardMarkup([
[InlineKeyboardButton('Close☄️', callback_data="back_main")]
])

print("Buttons & message py started🔥"),
print("Your Bot Is Running ⚡"),
print("🌟Bot Started Successfully 🌟"),
print("🎀🎀Join For Updates @EpicBotsSl🎀🎀")
