# Getting Started

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img alt="Python" src="https://img.shields.io/static/v1?label=Python&message=v3.8.5&color=blue&logo=python&logoColor=white">
    </a>
    <a href="https://pypi.org/project/Django/3.1.6/">
        <img alt="Django" src="https://img.shields.io/pypi/v/django/3.1.6?color=blue&label=Django&logo=django">
    </a>
    <a href="https://pypi.org/project/djangorestframework/3.12.2/">
        <img alt="DjangoRestFramework" src="https://img.shields.io/pypi/v/djangorestframework/3.12.2?color=blue&label=DjangoRestFramework&logo=django">
    </a>
    <a href="https://pypi.org/project/Pyrogram/1.1.13/">
        <img alt="Pyrogram" src="https://img.shields.io/pypi/v/pyrogram/1.1.13?color=blue&label=Pyrogram&logo=telegram">
    </a>
    <a href="https://www.mysql.com/downloads/">
        <img alt="mysql" src="https://img.shields.io/github/v/tag/mysql/mysql-server?label=mysql&logo=mysql&logoColor=white">
    </a>
    <a href="LICENSE">
        <img alt="MIT LICENSE" src="https://img.shields.io/badge/License-MIT-green">
    </a>
</p>

Just move step by step and everything should work so good.

## Installation

Before using the bot, you need to install some dependencies that the project works with them but don't worry, there is an automation shell script for that.\
Dependencies:
1. Python3
2. Python3-pip (pip3)
    * django
    * djangoRestFramework
    * pyrogram
    * mysqlclient
    * wheel
    * tgcrypto
    * json (built-in)
3. Python3-venv (Python Virtual Environment)
4. MySQL

### Linux (Debian and Ubuntu base)

Open up your terminal, Go to the main project directory and just run:
```
source ./commands/install
# some steps need to be done manually in previous command
# pay attention to them, Those will be asked in the process
python3 manage.py makemigrations users
python3 manage.py migrate
```
All of the top Dependencies should be installed on your system already and if you finished the first installation command process successfully, you do not need to do the [MySQL](#MySQL) chapter in [Configuration](#configuration) section.

### Windows

Install [Git](https://git-scm.com/download/win), [Microsoft Visual C++ 2015](https://www.microsoft.com/en-us/download/details.aspx?id=52685), [Python](https://www.python.org/downloads/), [MySQL](https://www.mysql.com/downloads/) and Microsoft Visual C++ v14 (read down for installation instructions) individually. (I can't automate that process, sorry)\
⚠️ Note: for installing "Microsoft Visual C++ v14" you need to use [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). So start Microsoft C++ Build Tools, let it download, get to **Indivisual Components** section and search "C++" and choose down selected item/items or a higher version of that and click install.\
![](./pics/build-tools.png)
⚠️ Note: If you had any error in down up comming instructions from wheel installation(an error for mysql) like this one picture down below, download highest version of mysqlclient from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient) and install it by pip like `pip3 install mysqlclient-1.4.6-cp39-cp39-win_amd64.whl` and you should have no other problems.
![](./pics/wheel-error.png)

Open up **git bash** (windows cmd or powershell will not work), Go to the main project directory and run:
```
source ./win_commands/install
# some steps need to be done manually in previous command
# pay attention to them, Those will be asked in the process
python3 manage.py makemigrations users
python3 manage.py migrate
```
All of the top Dependencies should be installed on your system already and if you finished the first installation command process successfully, you do not need to do the [MySQL](#MySQL) chapter in [Configuration](#configuration) section.

## Configuration

Attention: if you already successfully installed all of the dependencies and you completely finished asked manual configuration in installation process, skip [MySQL](#mysql) chapter.

### MySQL

In MySQL create a user called "__bot__" with "**Bot_123456**" password and then give it right privileges and create a database called "**group_manager_db**".\
If you don't know how to do that, here they are:
```
CREATE USER 'bot'@'%' IDENTIFIED BY 'Bot_123456';
GRANT ALL PRIVILEGES ON *.* TO 'bot'@'%';
CREATE DATABASE group_manager_db DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;
DEFAULT COLLATE utf8mb4_general_ci;
```

### config.ini

At the end, change the information in "[config.ini](config.ini)" file with your __Telegram ID__, your __Hash Code__ and your __Bot Token__.

### main<span>.</span>py

Set the blank guided with comment data on "[main<span>.</span>py](main.py)" file with your __Bot Name__, your __Username__ or __ID__ and __Bot Username__.\
All done.\
Now lets use it.

## Usage

All you need to do is `python3 main.py` but i automated that in one single word:

### __Linux__:

Everytime that you open up the project directory with a new terminal, inside main project directory, do:
```
source ./commands/shortcuts
```
and after that use `run` to start bot.

### __Windows__:

Everytime that you open up the project directory with a new terminal, inside main project directory, do:
```
source ./win_commands/shortcuts
```
and after that use `run` to start bot.