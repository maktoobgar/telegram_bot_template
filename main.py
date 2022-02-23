from pyrogram.types import Message
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

# Set settings variables
setattr(settings, "app", app)
setattr(settings, "managers", [manager.lower() for manager in config("MANAGERS", default=[], cast=lambda v: [s.strip() for s in v.split(',')])])

# Get bots identifications
ID               = (app.get_me()).id
USERNAME         = (app.get_me()).username

@app.on_message(filters.private & cfilters.is_in_special_state)
async def private_special_state(client: Client, message: Message):
    await private_special_state_response(client, message)
    
@app.on_message(filters.private & filters.command('start'))
async def private_start_command(client: Client, message: Message):
    await private_start_command_response(client, message)

@app.on_callback_query(cfilters.callback_has_goto_step)
async def goto_next_state(client: Client, callback_query: CallbackQuery):
    await goto_next_state_response(client, callback_query)

@app.on_disconnect()
async def disconnect(client):
    pass

def hello_creator():
    for creator in creators:
        app.send_message(creator, creator_message)

hello_creator()
idle()