import json
from functools import wraps
import logging
import logging.config
from typing import Any, Callable, Mapping, Optional, TypeVar
from aiogram import types


T = TypeVar("T")


class Logger:
    _config_loaded: bool = False
    _config: dict[str, Any] = {}
    logger: logging.Logger

    @classmethod
    def load_config(cls) -> None:
        if not cls._config_loaded:
            try:
                with open("logger_config.json", "r", encoding="UTF-8") as config_file:
                    cls._config = json.load(config_file)
                    cls._config_loaded = True
            except FileNotFoundError:
                cls._config = {}
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in config file")
            logging.config.dictConfig(cls._config)
            cls.logger = logging.getLogger("custom")

    @classmethod
    def log_msg(cls, func: Callable[[Any], T]) -> Callable[..., Optional[T]]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T | None:
            arg: types.CallbackQuery | types.Message = args[0]

            if isinstance(arg, types.Message):
                msg = arg
                if msg.from_user is None:
                    cls.info(f"None - {msg.text}")
                    return
                if msg.chat.id == msg.from_user.id:
                    cls.info(f"{msg.from_user.id} - {msg.text}")
                else:
                    cls.info(f"{msg.from_user.id} / {msg.chat.id} - {msg.text}")

            elif isinstance(arg, types.CallbackQuery):
                callback = arg
                if callback.message is None:
                    return
                if callback.message.chat.id == callback.from_user.id:
                    cls.info(f"{callback.from_user.id} - {callback.data}")
                else:
                    cls.info(f"{callback.from_user.id} / {callback.message.chat.id} - {callback.data}")
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def error(  # pylint: disable=arguments-differ, arguments-renamed
        cls,
        msg: object,
        exc_info=None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
    ) -> None:
        cls.logger.error(msg=msg, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)

    @classmethod
    def info(  # pylint: disable=arguments-differ, arguments-renamed
        cls,
        msg: object,
        exc_info=None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
    ) -> None:
        cls.logger.info(msg=msg, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel, extra=extra)
