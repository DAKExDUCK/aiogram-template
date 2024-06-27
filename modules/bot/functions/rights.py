from functools import wraps
from typing import Any, Awaitable, Callable, Optional, TypeVar

from aiogram import types
from aiogram.filters.base import Filter


admin_list = (1072746639, "1072746639")
T = TypeVar("T")


def is_Admin(func: Callable[[Any], Awaitable[T]]) -> Callable[[Any], Awaitable[Optional[T]]]:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> T | None:
        message: types.Message = args[0]
        if message.from_user is None:
            return
        if message.from_user.id in admin_list:
            return await func(*args, **kwargs)

    return wrapper


def is_admin(user_id: int | str) -> bool:
    return user_id in admin_list


class IsAdmin(Filter):
    key = "is_admin"

    async def __call__(self, *args) -> bool:
        message: types.Message = args[0]
        if message.from_user is None:
            return False
        return message.from_user.id in admin_list
