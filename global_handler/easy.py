import json


async def get_json(message):
    try:
        return json.loads(message.data.replace('\'', '\"'))
    except:
        return None