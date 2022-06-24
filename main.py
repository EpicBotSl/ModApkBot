#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from config import *
from buttons_mg import *
from database.db import Database
from asyncio import *
import heroku3
import requests
from helper.heroku_helper import HerokuHelper
import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

#=•=•=•=•=•=•=•=•=Mongo DB•=•=•=•=•=•=•=•=•=•=#

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"

#=•=•=•=•=•=•=•=•=•=Db End Point•=•=•=•=•=•=•=•=•=•#
epicbot = Client(
    "Epic Mod Apk Bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
#=•=•=•Db=•=•=#
DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "epic_bot")

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Risived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#=•=•=•=Def Start=•=•=•=#

@epicbot.on_message(filters.command("start"))
async def startprivate(epicbot, message):
    #return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await epicbot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if -1001645328504:
            await epicbot.send_message(
                -1001645328504,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    file_id = "CAACAgUAAxkBAAEFHD5itTEihLwB5gABPP58guE5OLp9JRoAArQFAAIiWKlVyHUsM5q363opBA"
    await epicbot.send_sticker(message.chat.id, file_id)
    text = f"Hi 🌹{message.from_user.mention}, 🌱Welcome to **Epic Mod Apk Bot⚡**"
    reply_markup = START_BUTTON
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
@epicbot.on_message(filters.command("stable"))
async def giblog(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    process = await message.reply_text( "`Trying To Fetch Logs....`")
    herokuHelper = HerokuHelper(HEROKU_APP_NAME, HEROKU_API_KEY)
    logz = herokuHelper.getLog()
    with open("logs.txt", "w") as log:
        log.write(logz)
    await process.delete()
    await bot.send_document(
        message.chat.id, "logs.txt", caption=f"**Logs Of {HEROKU_APP_NAME}**"
    )
    os.remove("logs.txt")

@epicbot.on_message(filters.private & filters.chat(LOG_CHANNEL) & filters.command("status"), group=5)
async def status(bot, update):
    if update.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    if not await db.is_user_exist(update.from_user.id):
         await db.add_user(update.from_user.id)
         
    await bot.send_sticker(update.chat.id, random.choice(STAT_STICKER))
    total_users = await db.total_users_count()
    text = "**Bot Advanced Statistics 📊**\n"
    text += f"\n**Total Users:** `{total_users}`"
    await update.reply_text(
        text=text,
        quote=True,
        disable_web_page_preview=True
    )

#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
@epicbot.on_message(filters.command("send"))
async def status(bot, message):
    if message.from_user.id not in AUTH_USERS:
        await message.delete()
        return
    mesg=message.reply_to_message
    f= message.text
    s=f.replace('/send ' ,'')
    fid=s.replace('%20', ' ')
    await send_msg(user_id=fid, message=mesg)
    await message.delete()
    await bot.send_message(message.chat.id, text=f"Ur Msg Sent To [User](tg://user?id={fid})", reply_markup=CLOSE_BUTTON)
    await bot.send_message(PRIVATE_LOG,text=f"""#SEND_LOG
• **Send By:** {message.from_user.mention} [`{message.from_user.id}`]
• **Send To:** [User](tg://user?id={fid}) [`{fid}`]
• **Message:-**
""")
    await send_msg(PRIVATE_LOG, message=mesg)
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

@epicbot.on_callback_query(filters.regex("DEVS"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(DEVS_MG, reply_markup = DEVS_BTN)

print("Epic Main.Py Started 🌹")
epicbot.run()
