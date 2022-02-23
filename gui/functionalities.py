from django.conf import settings
from pyrogram import Client
from users.models import User
from users.functions import *
from django.db.models import Q

class Special:
    groupid: str
    user: User

    def __init__(self, groupid: str, state: str):
        self.state = state
        self.groupid = groupid
        self.user = User()

class SpecialManager:
    specials = {}

    async def push_special(self, userid: str, groupid: str, state: str) -> Special:
        if userid not in dir(self.specials):
            self.specials[userid] = Special(groupid, state)
        return self.specials[userid]

    async def special_exist(self, userid: str, groupid: str) -> list:
        if not userid or not groupid:
            return False
        if userid in self.specials:
            if self.specials[userid].groupid == groupid:
                return True
        return False

    async def get_special(self, userid: str, groupid: str) -> Special:
        if not userid or not groupid:
            return None
        if userid in self.specials:
            if self.specials[userid].groupid == groupid:
                return self.specials[userid]
        return None

    async def pop_special(self, userid: str, groupid: str) -> Special:
        if not userid or not groupid:
            return None
        if userid in self.specials:
            if self.specials[userid].groupid == groupid:
                return self.specials.pop(userid)
        return None

manager = SpecialManager()

async def manager_menu(userid: str, groupid: str, state: str, value: str, **kwargs) -> list:
    await manager.push_special(userid, groupid, state)
    return [True]

async def clean(userid: str, groupid: str, state: str, value: str, **kwargs) -> list:
    await manager.pop_special(userid, groupid)
    return [True]
