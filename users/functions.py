from users.models import User
from asgiref.sync import sync_to_async
from django.db.models import Q


def new(userid="", username="", first_name="", last_name="") -> User:
    return User(
        userid=userid,
        username=username,
        first_name=first_name,
        last_name=last_name,
    )

new_user = sync_to_async(new, thread_sensitive=True)
"""how to use:
create_user(userid: int or str, username: str, first_name: str, last_name: str, trader: bool, api_key: str, secret_key: str)
returns a User object or will break the code with an error"""

def save(user) -> None:
    user.save()

save_user = sync_to_async(save, thread_sensitive=True)
"""how to use:
save_user(user: a User object)
returns None
"""

def get(id) -> User:
    try:
        user = User.objects.get(id=id)
        return user
    except:
        return None

get_user = sync_to_async(get, thread_sensitive=True)
"""how to use:
get_user(userid: int or str)
returns User object or None"""

def get_by_username(username) -> User:
    try:
        user = User.objects.get(username=username)
        return user
    except:
        return None

get_user_by_username = sync_to_async(get_by_username, thread_sensitive=True)

def get_property(user: User, property: str) -> any:
    try:
        if property == "userid":
            return user.userid
        elif property == "username":
            return user.username
        elif property == "first_name":
            return user.first_name
        elif property == "last_name":
            return user.last_name
        return None
    except:
        return None

get_user_property = sync_to_async(get_property, thread_sensitive=True)
"""how to use:
get_user_property(user: a User object, property: str(acceptable values: 'userid', 'username', 'first_name', 'last_name', 'trader', 'api_key', 'secret_key'))
returns the property(it depends on type of the property in db) or None"""

def set_property(user: User, property: str, value: any) -> User:
    try:
        if property == "userid":
            user.userid = value
        elif property == "username":
            user.username = value
        elif property == "first_name":
            user.first_name = value
        elif property == "last_name":
            user.last_name = value
        return user
    except:
        return user

set_user_property = sync_to_async(set_property, thread_sensitive=True)
"""how to use:
set_user_property(user: a User object, property: str(acceptable values: 'userid', 'username', 'first_name', 'last_name', 'trader', 'api_key', 'secret_key'), value: the actual value in any type('it depends'))
returns the User object anyway(even if there is an error)"""

def filter(value: str, buts: list[User]) -> list[User]:
    users: list[User] = list(User.objects.filter(Q(userid__contains=value) | 
        Q(username__contains=value) | Q(first_name__contains=value) |
        Q(last_name__contains=value)).distinct())

    removes: list[User] = []
    for user in users:
        for but in buts:
            if user.id == but.id:
                removes.append(user)

    for rem in removes:
        users.remove(rem)

    return users

filter_users = sync_to_async(filter, thread_sensitive=True)

def delete(user: User) -> None:
    user.delete()

delete_user = sync_to_async(delete, thread_sensitive=True)