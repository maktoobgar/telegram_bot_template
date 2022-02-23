from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from users.models import User
import json

f = open("./gui/gui.json", 'r')

data: dict = json.load(f)
f.close()


async def get_gui(key: str) -> InlineKeyboardMarkup:
    if key not in data:
        return []

    arr = []
    for r in data[key]["reply_markup"]:
        row = []
        for item in r:
            row.append(
                InlineKeyboardButton(
                    item["text"] if "text" in item else "",
                    callback_data=str(item["callback"]) if "callback" in item else "{}",
                    url=item["url"] if "url" in item else ""
                )
            )
        arr.append(row)

    return InlineKeyboardMarkup(arr)

async def get_custom_gui(state: str, goto: str, users: list[User]) -> InlineKeyboardMarkup:
    li = []

    if type(users) == list:
        for user in users[:10 if len(users) >= 10 else len(users)]:
            li.append([
                InlineKeyboardButton(
                    f"{user}",
                    callback_data=str({"s": state, "a": state, "g": goto, "v": str(user.id)}),
                    url=""
                )
            ])

    for keyboard in (await get_gui(state)).inline_keyboard:
        li.append(keyboard)

    return InlineKeyboardMarkup(li)

async def get_text(state: str) -> str:
    if state not in data or "text" not in data[state]:
        return ""

    return data[state]["text"]