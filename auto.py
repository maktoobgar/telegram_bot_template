import os
import sys
import random
import shutil
from commands.config import main as config
from commands.mysql_config import main as mysql_config
from commands.security import main as security


def main():
    
    if len(sys.argv) == 1:

        os.system('cls')

        if os.path.isdir('./env'):
            try:
                shutil.rmtree('./env')
            except:
                print("\nplease first remove env folder and then try again\n")
                return

        # Chcking if some packages are installed
        print("Checking if python is installed\n")
        os.system("python --version")
        print("\nChecking if mysql is installed\n")
        os.system("mysql --version")
        print("\nChecking if pip3 is installed\n")
        os.system("pip --version")

        # Creating a virtual environment
        print("\nCreating a virtual environment\n")
        os.system("python -m venv env")
        print("\n\nIf there is no problem on top log, Run this command: \n\n.\\env\\Scripts\\activate && python auto.py windows")
        return

    elif sys.argv[1] == "windows" or sys.argv[1] == "window":

        os.system('cls')

        # installing requirements
        os.system("pip install wheel && pip install --upgrade setuptools wheel")
        os.system("pip install -r requirements.txt")

        print("\n\nThe installation process is done")
        print("After checking the log, if there is no problem, you can run the bot with \"python main.py\" command")
        print("Press any button to continue to mysql configuration")
        input()

        secret = "SECRET_KEY="
        secret = secret + "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
        
        f = open(".env", "w")
        f.write(secret)
        f.close()

        mysql_config()

        f = open("config.ini", "w")
        f.close()

        security()

        config()

        # Migration database
        print("Database migration")
        os.system("python manage.py makemigrations users groups")
        os.system("python manage.py migrate")

        # Run Bot
        os.system("python main.py")


if __name__ == "__main__":
    main()