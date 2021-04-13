import os

def main():

    os.system('cls || clear')

    CREATORS = input('write down your creators ids or usernames (like: Ali, Jafar, Mahmood):')
    if not CREATORS or CREATORS == '\n':
        CREATORS = 'Maktoobgar, Who_has_been_broken'
    SESSION = input('write down your Session name (like: test):')
    if not SESSION or SESSION == '\n':
        SESSION = 'test'

    output = f"""CREATORS={CREATORS}
SESSION={SESSION}"""

    f = open(".env", "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    main()