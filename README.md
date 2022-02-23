# Getting Started

<p align="center">
    <a href="https://www.python.org/downloads/">
        <img alt="Python" src="https://img.shields.io/static/v1?label=Python&message=v3.8.5&color=blue&logo=python&logoColor=white">
    </a>
    <a href="https://pypi.org/project/Django/3.1.6/">
        <img alt="Django" src="https://img.shields.io/pypi/v/django/3.1.6?color=blue&label=Django&logo=django">
    </a>
    <a href="https://pypi.org/project/Pyrogram/1.1.13/">
        <img alt="Pyrogram" src="https://img.shields.io/pypi/v/pyrogram/1.1.13?color=blue&label=Pyrogram&logo=telegram">
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
4. Postgres Server

### Linux

Open up your terminal, Go to the main project directory and just run:
```
source ./commands/deploy
```
And answer the asked configurations on the way of installation.
**Note**: This is kinda deprecated but still works.

## Configuration

During running the installation automation, the automation will ask you some questions and you just give him the right answer.\
That's it.\
Configurations will generate automat and There are no other configurations to do.

## Usage

Now that all of the top Dependencies should be installed on your system already configurations should be done, if you finished all top installation process successfully, you are ready to run the bot with:
```
python3 main.py
```