async def get_userid(message_callback):
    if not 'from_user' in dir(message_callback):
        return ""
    if not 'id' in dir(message_callback.from_user):
        return ""
    return message_callback.from_user.id

async def get_text(message):
    if 'text' in dir(message):
        if len(message.text) > 0:
            return message.text
    if 'caption' in dir(message):
        if len(message.caption) > 0:
            return message.caption
    return ""

async def get_username(message_callback):
    if not 'from_user' in dir(message_callback):
        return ""
    if not 'username' in dir(message_callback.from_user):
        return ""
    return message_callback.from_user.username.lower()

async def get_groupid(message_callback):
    if 'chat' in dir(message_callback):
        return message_callback.chat.id
    if 'message' in dir(message_callback):
        if 'chat' in dir(message_callback.message):
            return message_callback.message.chat.id
    return ""

async def get_status(chatmember):
    if 'status' not in dir(chatmember):
        return ""
    return chatmember.status

async def get_messageid(message_callback):
    if 'message_id' in dir(message_callback):
        return message_callback.message_id
    if 'message' not in dir(message_callback):
        return ""
    if 'message_id' not in dir(message_callback.message):
        return ""
    return message_callback.message.message_id

async def get_first_name(message_callback):
    if 'from_user' not in dir(message_callback):
        return ""
    return message_callback.from_user.first_name

async def get_reply_userid(message):
    if 'reply_to_message' in dir(message):
        if 'from_user' in  dir(message.reply_to_message):
            return message.reply_to_message.from_user.id
    return ""

async def get_reply_messageid(message):
    if 'reply_to_message' in dir(message):
        if 'message_id' in dir(message.reply_to_message):
            return message.reply_to_message.message_id
    return ""

async def get_reply_first_name(message):
    if 'reply_to_message' in dir(message):
        if 'from_user' in dir(message.reply_to_message):
            if 'first_name' in dir(message.reply_to_message.from_user):
                return message.reply_to_message.from_user.first_name
    return ""