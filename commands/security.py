import os


def main():
    os.system('cls || clear')

    api_id = input('write down your api_id:')
    if not api_id or api_id == '\n':
        api_id = ''
    api_hash = input('write down your api_hash:')
    if not api_hash or api_hash == '\n':
        api_hash = ''
    bot_token = input('write down your bot_token:')
    if not bot_token or bot_token == '\n':
        bot_token = ''

    output = f"""[pyrogram]
api_id = {api_id}
api_hash = {api_hash}
bot_token = {bot_token}"""

    f = open("config.ini", "w")
    f.write(output)
    f.close()


if __name__ == "__main__":
    main()