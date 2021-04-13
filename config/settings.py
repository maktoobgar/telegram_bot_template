import os
from decouple import config

# Our database settings
DATABASES = {
    'default': {
        "ENGINE": config("SQL_ENGINE", default="django.db.backends.mysql", cast=str),
        "NAME": config("SQL_DATABASE", default="test_db", cast=str),
        "USER": config("SQL_USER", default="test", cast=str),
        "PASSWORD": config("SQL_PASSWORD", default="!_T123456789T_!", cast=str),
        "HOST": config("SQL_HOST", default="localhost", cast=str),
    }
}

# Our folders knows as apps
INSTALLED_APPS = [
    'rest_framework',
    'users',
]

# The secret key for database connection
# Warnning: Change it when you are in production
SECRET_KEY = config('SECRET_KEY', default='6few3n$i_q_o@lZdlxk81%wcx3!*5r29yu629&d97!hikat9fa', cast=str)

# The field in models to be Primarykey
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
