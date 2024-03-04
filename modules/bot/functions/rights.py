from functools import wraps

from aiogram import types
from aiogram.dispatcher.filters import Filter


admin_list = [1072746639]


def is_Admin(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        message: types.Message = args[0]
        if message.from_user.id in admin_list:
            return await func(*args, **kwargs)
    return wrapper


def is_admin(user_id):
    return user_id in admin_list


class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, *args):
        message = args[0]
        return message.from_user.id in admin_list
