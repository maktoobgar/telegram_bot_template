from django.conf import settings
from pyrogram import Client
from gui.utilities import get_gui, get_custom_gui, get_text
from gui.functionalities import manager
from gui.states import NEXT_STATES, MANAGER_MENU
from users.models import User

async def gui_sender(groupid: str, data: dict):
    app: Client = getattr(settings, "app")

    await app.send_message(
        chat_id=groupid,
        text=await get_text(data['goto']),
        reply_markup=await get_gui(data['goto'])
    )

async def gui_custom_sender(userid: str, groupid: str, data: dict, users: list[User]):
    app: Client = getattr(settings, "app")
    next_goto = await gui_get_next_special_state(userid, groupid)

    await app.send_message(
        chat_id=groupid,
        text=await get_text(data['goto']),
        reply_markup=await get_custom_gui(data['goto'], next_goto, users)
    )

async def gui_get_next_special_state(userid: str, groupid: str) -> str:
    special = await manager.get_special(userid, groupid)
    if not special:
        return MANAGER_MENU
    return NEXT_STATES[special.state]

async def gui_get_special_state(userid: str, groupid: str) -> str:
    special = await manager.get_special(userid, groupid)
    if not special:
        return MANAGER_MENU
    return special.state
