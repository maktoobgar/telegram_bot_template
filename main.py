import config.config
import django
from users.models import *
from pyrogram import Client, idle


# Bot
app              = Client("")   # Bot Name
creator          = ""           # Creator id or creator username
                                # this username has to start the bot, otherwise
                                # the account can not receive any messages from bot
bot              = ""           # Bot Username
creator_message  = "The Server Is Up And Running"
app.start()

@app.on_message()
async def my_handler(client, message):
    pass

@app.on_disconnect()
async def disconnect(client):
    pass

def hello_creator():
    if creator:
        app.send_message(creator, creator_message)

hello_creator()
idle()