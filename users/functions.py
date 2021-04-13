from users.models import User
from asgiref.sync import sync_to_async


def create(userid, username):
    return User.objects.create(userid=userid, username=username)

create_user = sync_to_async(create, thread_sensitive=True)
"""how to use:
create_user(userid: int or str, username: str)
returns a User object or will break the code with an error"""

def save(user):
    user.save()

save_user = sync_to_async(save, thread_sensitive=True)
"""how to use:
save_user(user: a User object)
returns None
"""

def get(userid):
    try:
        user = User.objects.get(userid=userid)
        return user
    except:
        return None

get_user = sync_to_async(get, thread_sensitive=True)
"""how to use:
get_user(userid: int or str)
returns User object or None"""

def get_property(user, property):
    try:
        if property == "userid":
            return user.userid
        elif property == "username":
            return user.username
        return None
    except:
        return None

get_user_property = sync_to_async(get_property, thread_sensitive=True)
"""how to use:
get_user_property(user: a User object, property: str(acceptable values: 'userid', 'username'))
returns the property(it depends on type of the property in db) or None"""

def set_property(user, property, value):
    try:
        if property == "userid":
            user.userid = value
        elif property == "username":
            user.username = value
        return user
    except:
        return user

set_user_property = sync_to_async(set_property, thread_sensitive=True)
"""how to use:
set_user_property(user: a User object, property: str(acceptable values: 'userid', 'username'), value: the actual value in any type('it depends'))
returns the User object anyway(even if there is an error)"""