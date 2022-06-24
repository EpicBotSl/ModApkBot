import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

@app.on_callback_query(filters.regex("HELP_CALLBACK"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(DEVS_MG,reply_markup=InlineKeyboardMarkup(DEVS_BTN))

print("Callback.py Started🌹")
