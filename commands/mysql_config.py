import os


def main():
    os.system('cls || clear')

    what = input('This is a deployment(d) or development(anything else on keyboard)?')

    SQL_ENGINE = 'django.db.backends.mysql'
    SQL_DATABASE = 'test_db'
    SQL_USER = 'test'
    SQL_PASSWORD = '!_T123456789T_!'
    SQL_HOST = 'localhost'

    if what == 'd':
        SQL_ENGINE = input('write down your SQL_ENGINE(like: django.db.backends.mysql):')
        if not SQL_ENGINE or SQL_ENGINE == '\n':
            SQL_ENGINE = 'django.db.backends.mysql'
        SQL_DATABASE = input('write down your SQL_DATABASE(like: test_db):')
        if not SQL_DATABASE or SQL_DATABASE == '\n':
            SQL_DATABASE = 'test_db'
        SQL_USER = input('write down your SQL_USER(like: test):')
        if not SQL_USER or SQL_USER == '\n':
            SQL_USER = 'test'
        SQL_PASSWORD = input('write down your SQL_PASSWORD:')
        if not SQL_PASSWORD or SQL_PASSWORD == '\n':
            SQL_PASSWORD = '!_T123456789T_!'
        SQL_HOST = input('write down your SQL_HOST(like: localhost or 127.0.0.1):')
        if not SQL_HOST or SQL_HOST == '\n':
            SQL_HOST = 'localhost'


    output = f"""SQL_ENGINE={SQL_ENGINE}
SQL_DATABASE={SQL_DATABASE}
SQL_USER={SQL_USER}
SQL_PASSWORD={SQL_PASSWORD}
SQL_HOST={SQL_HOST}
"""

    f = open(".env", "a")
    f.write(output)
    f.close()

    os.system('cls || clear')

    if SQL_ENGINE == 'django.db.backends.mysql':

        print('run these commands down here:\n')
        print(f"CREATE USER '{SQL_USER}'@'%' IDENTIFIED BY '{SQL_PASSWORD}';")
        print(f"GRANT ALL PRIVILEGES ON *.* TO '{SQL_USER}'@'%';")
        print(f"CREATE DATABASE {SQL_DATABASE} DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;")
        print("exit")
        print("\ndone")

        print("if you see a \"Enter password:\" text down here, enter your mysql password and then copy paste the lines.\n")
        try:
            os.system('mysql -u root || mysql -u root -p')
        except:
            pass


if __name__ == "__main__":
    main()