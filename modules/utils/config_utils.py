import os

from modules.exceptions.config_exc import ConfigFieldIsRequired, ConfigFieldWrongType, T


def get_from_env(
        field: str, 
        default: T | None = None, 
        value_type: type[T] = str
) -> T:
    value = os.getenv(field, default)
    if value is None:
        raise ConfigFieldIsRequired(field)

    if isinstance(value, str):
        try:
            return value_type(value)
        except Exception:
            raise ConfigFieldWrongType(field, value, str(value_type))

    return value
