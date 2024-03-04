import os
from typing import TypeVar

from modules.exceptions.config_exc import ConfigFieldIsRequired, ConfigFieldWrongType


T = TypeVar('T', int, str)

def get_from_env(
        field: str, 
        default: T | None = None, 
        value_type: type[T] = str
) -> T:
    value = os.getenv(field, default)
    if value is None:
        raise ConfigFieldIsRequired(field)

    if not isinstance(value, value_type):
        if isinstance(value, str):
            try:
                return value_type(value)
            except Exception:
                raise ConfigFieldWrongType(field, value, value_type)  # pylint: disable=raise-missing-from
        raise ConfigFieldWrongType(field, value, value_type)

    return value
