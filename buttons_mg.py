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

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

DEVS_BTN = InlineKeyboardMarkup([[
             InlineKeyboardButton('ɴᴀᴠᴀɴᴊᴀɴᴀ', url="https://t.me/NA_VA_N_JA_NA1"),
             InlineKeyboardButton('ᴍᴇᴛʜɪɴᴅᴜ ᴡɪsᴜʟᴀ', url="https://t.me/wisula4")
             ],
             [
             InlineKeyboardButton('🔙', callback_data="Back_M")
             ]])

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#


STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]  

DEVS_MG = "🎀This Is Epic Mod Apk Bot'S Devs🎀"

print("Buttons & message py started🔥"),
print("Your Bot Is Running ⚡"),
print("🌟Bot Started Successfully 🌟"),
print("🎀🎀Join For Updates @EpicBotsSl🎀🎀")
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

