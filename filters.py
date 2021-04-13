from threading import Thread
from pyrogram import filters
from global_handler.easy import get_json
from global_handler.exist import get_userid, get_groupid
import time
special = {}
groups_users = []


async def set_special(userid, groupid, messageid, state):
    if userid not in dir(special):
        special[userid] = {'groupid': groupid, 'messageid': messageid, 'state': state}

async def special_exist(userid, groupid):
    if not userid or not groupid:
        return False
    if userid in special:
        if special[userid]['groupid'] == groupid:
            return True
    return False

async def get_special(userid):
    return special[userid]

async def pop_special(userid):
    if userid in special:
        return special.pop(userid)
    return None

async def add_group(id):
    groups_users.append(id)
    th = Thread(target=remove_after, args=(id,))
    th.start()

def remove_after(id):
    time.sleep(30)
    groups_users.remove(id)

# region callback include an string
def callback_name_filter(data):
    """Filter callback messages that contain an specific data."""
    
    async def func(flt, _, query):
        return flt.data in query.data

    return filters.create(func, data=data)
# endregion
    
# region next callback
async def callback_has_goto_step_filter(_, __, m):
    data = await get_json(m)
    if data:
        return 'goto' in data
    return False

callback_has_goto_step = filters.create(callback_has_goto_step_filter)
"""Filter callback data's that contain an "next" key."""
# endregion

# region callback include an string
def is_admin(data):
    """Filters admins."""
    
    async def func(flt, _, query):
        app = flt.data
        userid = await get_userid(query)
        groupid = await get_groupid(query)
        admins = await app.get_chat_members(groupid, filter="administrators")
        for admin in admins:
            if admin.user.id == userid:
                return True
        return False

    return filters.create(func, data=data)
# endregion

# region message include an string
def message_content_contains_filter(data):
    """Filter messages that contain an specific data."""
    
    async def func(flt, _, query):
        text = query.text
        for t in flt.data:
            out = True
            for i in range(len(t)):
                if t[i] != text[i]:
                    out = False
                    break
            if out:
                return True
        return False

    return filters.create(func, data=data)
# endregion

# region message is an specific string
def message_content_filter(data):
    """Filter messages that are an specific data."""
    
    async def func(flt, _, query):
        text = (query.text).lower()
        for t in flt.data:
            if t == text:
                return True
        return False

    return filters.create(func, data=data)
# endregion

# region in special state
async def is_in_special_state_filter(_, __, m):
    return await special_exist(await get_userid(m), await get_groupid(m))

is_in_special_state = filters.create(is_in_special_state_filter)
"""Filter special state users."""
# endregion