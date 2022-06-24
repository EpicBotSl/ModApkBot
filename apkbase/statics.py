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

@Client.on_message(filters.regex(pattern="📊 Statistics"))   
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
    count = await bot.get_chat_members_count(-1001210985373)
    counta = await bot.get_chat_members_count(-1001759991131)
    text=f"""**Bot Advanced Statistics 📊**
** 👥Members Counts in Our channel:**
◉──────────────────────────────────◉
 **MemeHub Telegram 🇱🇰  Users** : `{count}`
 **⚜️MemeHub Family⚜️ (Admins)**   : `{counta}`
 **ᴍᴇᴍᴇʜᴜʙ ᴏᴍғғɪᴄɪᴀʟ ʙᴏᴍᴛ 『🇱🇰』 Users** : `{countb}`
◉──────────────────────────────────◉
