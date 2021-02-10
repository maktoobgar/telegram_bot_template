import sys
import os
import django

# Django ORM Setup
sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()