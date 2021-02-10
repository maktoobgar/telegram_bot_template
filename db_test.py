import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from users.models import *


print("Now you have the power of Django's ORM at your fingertips!")
print("The sample output below is printing usernames from the User model.")

for u in User.objects.all():
	print("ID: " + str(u.id) + "\tUsername: " + u.name)