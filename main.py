from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, idle
from pyrogram import filters
from decouple import config
import config.config as sconfig
import django
import filters as cfilters
from user_handler.listener import *


# Bot
app              = Client(config("SESSION", default="Temp", cast=str))
creators         = config("CREATORS", default="", cast=lambda v: [s.strip() for s in v.split(',')])
bot              = config("BOT", default="test", cast=str)
creator_message  = "The Server Is Up And Running.\n=========================\n\nTest Phase"
app.start()
ID               = (app.get_me()).id
USERNAME         = (app.get_me()).username

@app.on_message(filters.private & filters.command('start'))
async def private_start_command_messages(client, message):
    await private_start_command_response(app, message)

@app.on_disconnect()
async def disconnect(client):
    pass

def hello_creator():
    for creator in creators:
        app.send_message(creator, creator_message)

hello_creator()
idle()