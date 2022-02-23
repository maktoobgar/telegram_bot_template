from pyrogram.types import Message, CallbackQuery
from pyrogram import Client
from django.conf import settings
from gui.states import *
from global_handler.exist import *
from global_handler.easy import *
from users.functions import get_user, new_user, save_user
from asgiref.sync import sync_to_async
from gui import menu

async def private_start_command_response(client: Client, message: Message) -> None:
    """Says hello to our new user and saves his data to database and passes the menu"""

    userid = await get_userid(message)
    username = await get_username(message)
    groupid = await get_groupid(message)

    user = await get_user(userid)
    user = user if user else await get_user_by_username(username)
    if not user:
        try:
            user = await new_user(userid, username)
            await save_user(user)
        except:
            pass

    await menu.gui_sender(
        groupid,
        {"state": MANAGER_MENU, "goto": MANAGER_MENU}
    )

async def private_special_state_response(client: Client, message: Message) -> None:
    """A special message received from our request so special treatment happens here"""

    text = await get_text(message)
    userid = await get_userid(message)
    groupid = await get_groupid(message)

    state = await menu.gui_get_special_state(userid, groupid)
    goto = await menu.gui_get_next_special_state(userid, groupid)

    result = [True]
    if state and STATES[state] != None:
        result = await STATES[state](userid, groupid, goto, text.lower())
    if not result[-1]:
        return

    if state in CUSTOM_REQUIRED_STATED:
        await menu.gui_custom_sender(
            userid,
            groupid,
            {'state': state, 'goto': goto},
            result[0]
        )
    else:
        await menu.gui_sender(
            groupid,
            {'state': state, 'goto': goto}
        )

async def goto_next_state_response(client: Client, callback_query: CallbackQuery) -> None:
    """Sends user to the next menu or next action"""

    userid = await get_userid(callback_query)
    groupid = await get_groupid(callback_query)

    data = await get_json(callback_query.data)

    result = [True]
    if 'a' in data and data['a'] and STATES[data['a']] != None:
        if 'v' not in data:
            result = await STATES[data['a']](userid, groupid, data['g'], None)
        else:
            result = await STATES[data['a']](userid, groupid, data['g'], data['v'].lower())
    if not result[-1]:
        return

    if 's' in data and  data['s'] in CUSTOM_REQUIRED_STATED:
        await menu.gui_custom_sender(
            userid,
            groupid,
            {'state': data['s'], 'goto': data['g']},
            result[0]
        )
    else:
        await menu.gui_sender(
            groupid,
            {'state': data['s'], 'goto': data['g']}
        )
