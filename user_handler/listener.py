from global_handler.exist import *
from users.functions import get_user, create_user, save_user

async def private_start_command_response(app, message):
    """Says hello to our new user and saves his data to database"""

    userid = await get_userid(message)
    username = await get_username(message)
    groupid = await get_groupid(message)
    text = await get_text(message)

    if not username:
        username = ''
    await app.send_message(userid, text='hello my friend')

    user = await get_user(userid)
    if not user:
        user = await create_user(userid, username)
        await save_user(user)
        await app.send_message(userid, text='saved to database')