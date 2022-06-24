#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from config import *
from script import *
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
    file_id = "CAACAgIAAxkBAAEFHSBitZsmpQpnfJ5XCFRtQ13JT74KLQACTgIAAladvQow_mttgTIDbykE"
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

@epicbot.on_message(filters.incoming & filters.chat(-1001609244993))
async def bchanl(bot, update, broadcast_ids={}): 
    all_users = await db.get_all_users()
    broadcast_msg= update
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await bot.send_message(-1001645328504,f"Ads Broadcast Started! You will be notified with log file when all the users are notified.")
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
        
    async with aiofiles.open('broadcastlog.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
        
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    await asyncio.sleep(3)
    await out.delete()
    
    if failed == 0:
        await bot.send_message(-1001645328504, f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    else:
        await bot.send_document(-1001645328504, 'broadcastlog.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    os.remove('broadcastlog.txt') 
    
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

@epicbot.on_message(filters.command("state"))   
async def startprivate(bot, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(bot.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""**🏅Total Bot Users & Our Chanel State**
╔═══════════════════════════════════╗
  **🎋Mod Apk Bot State🎋** 🏅`{countb}`

  **🌱Epic Developers🌟** 🏅`{count}`
╚═══════════════════════════════════╝ 
"""
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

@epicbot.on_callback_query(filters.regex("DEVS"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(DEVS_MG, reply_markup = DEVS_BTN)

@epicbot.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "add": 
        await update.answer(
             text="♻️Adding Soon......",
        )
    elif update.data == "Back_M":
         await update.message.edit_text(
             text=START_MG,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="👻 ʙᴀᴍᴄᴋ 👻",
         )

print("Epic Main.Py Started 🌹")
epicbot.run()
