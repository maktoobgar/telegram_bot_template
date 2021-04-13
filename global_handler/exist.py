async def get_userid(message):
    if not 'from_user' in dir(message):
        return None
    if not 'id' in dir(message.from_user):
        return None
    return message.from_user.id

async def get_text(message):
    if 'text' in dir(message):
        if len(message.text) > 0:
            return message.text
    if 'caption' in dir(message):
        if len(message.caption) > 0:
            return message.caption
    return None

async def get_username(message):
    if not 'from_user' in dir(message):
        return None
    if not 'username' in dir(message.from_user):
        return None
    return message.from_user.username

async def get_groupid(message):
    if 'chat' in dir(message):
        return message.chat.id
    if 'message' in dir(message):
        if 'chat' in dir(message.message):
            return message.message.chat.id
    return None

async def get_status(chatmember):
    if 'status' not in dir(chatmember):
        return None
    return chatmember.status

async def get_messageid(message):
    if 'message_id' in dir(message):
        return message.message_id
    if 'message' not in dir(message):
        return None
    if 'message_id' not in dir(message.message):
        return None
    return message.message.message_id

async def get_first_name(message):
    if 'from_user' not in dir(message):
        return None
    return message.from_user.first_name

async def get_reply_userid(message):
    if 'reply_to_message' in dir(message):
        if 'from_user' in  dir(message.reply_to_message):
            return message.reply_to_message.from_user.id
    return None

async def get_reply_messageid(message):
    if 'reply_to_message' in dir(message):
        if 'message_id' in dir(message.reply_to_message):
            return message.reply_to_message.message_id
    return None

async def get_reply_first_name(message):
    if 'reply_to_message' in dir(message):
        if 'from_user' in dir(message.reply_to_message):
            if 'first_name' in dir(message.reply_to_message.from_user):
                return message.reply_to_message.from_user.first_name
    return None