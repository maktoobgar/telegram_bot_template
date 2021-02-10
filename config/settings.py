import os

# Our database settings
DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.mysql"),
        "NAME": os.environ.get("SQL_DATABASE", "bot_db"),
        "USER": os.environ.get("SQL_USER", "bot"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "Bot_123456"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
    }
}

# Our folders knows as apps
INSTALLED_APPS = [
    'rest_framework',
    'users',
]

# The secret key for database connection
# Warnning: Change it when you are in production
SECRET_KEY = '6few3n$i_q_o@lZdlxk81%wcx3!*5r29yu629&d97!hikat9fa'