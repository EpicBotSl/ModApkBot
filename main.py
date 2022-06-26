#Epic Bots 2022© All Rights Resived Created By Navanjana Sathsindu
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from utils import Media, unpack_new_file_id
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
from pyrogram.types import InlineQueryResultArticle
from pyrogram.types import InputTextMessageContent
from utils import Media, unpack_new_file_id

logger = logging.getLogger(__name__)

@epicbot.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        await message.reply(INVITE_MSG)
    else:
        buttons = [[
            InlineKeyboardButton('Search Here', switch_inline_query_current_chat=''),
            InlineKeyboardButton('Go Inline', switch_inline_query=''),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(START_MSG, reply_markup=reply_markup)

@epicbot.on_message(filters.command('channel') & filters.user(AUTH_USERS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(AUTH_CHANNEL, (int, str)):
        channels = [AUTH_CHANNEL]
    elif isinstance(AUTH_CHANNEL, list):
        channels = AUTH_CHANNEL
    else:
        raise ValueError("Unexpected type of AUTH_CHANNEL")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(AUTH_CHANNEL)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@epicbot.on_message(filters.command('total') & filters.user(AUTH_USERS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@epicbot.on_message(filters.command('logger') & filters.user(AUTH_USERS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@epicbot.on_message(filters.command('delete') & filters.user(AUTH_CHANNEL))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if not (reply and reply.media):
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    msg = await message.reply("Processing...⏳", quote=True)

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    file_id = unpack_new_file_id(media.file_id)[0]
    result = await Media.collection.delete_one({'file_id': file_id})

    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')
                            

#=•=•=•=•=•=•=•=•=•=Db End Point•=•=•=•=•=•=•=•=•=•#
epicbot = Client(
    "Epic Mod Apk Bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)



print("Epic Main.Py Started 🌹")
epicbot.run()
