import os
from typing import TypeVar

from modules.exceptions.config_exc import ConfigFieldIsRequired

T = TypeVar("T")


def get_from_env(field: str, default: T | None = None) -> T | str:
    value = os.getenv(field, default)
    if value is None:
        raise ConfigFieldIsRequired(field)

    return value
