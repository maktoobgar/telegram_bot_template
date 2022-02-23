import json, time
from threading import Thread
from pyrogram import Client
from django.conf import settings


async def get_json(message):
    try:
        return json.loads(message.data.replace('\'', '\"'))
    except:
        return None

async def remove_after(after: int, groupid: int, messageid: int) -> None:
    t = Thread(target=remover, args=(after, groupid, messageid))
    t.start()

def remover(after: int, groupid, messageid: int) -> None:
    time.sleep(after)
    try:
        app: Client = getattr(settings, 'app')
        app.delete_messages(
            groupid,
            messageid
        )
    except:
        pass
