import os

from modules.utils.config_utils import get_from_env


def test_get_from_env1():
    field_name = "test_var1"
    value = "some value"
    os.environ[field_name] = value

    res = get_from_env(field_name)
    assert value == res


def test_get_from_env2():
    field_name = "test_var2"
    value = "some value"
    default = "default"
    os.environ[field_name] = value

    res = get_from_env(field_name, default=default)
    assert value == res


def test_get_from_env3():
    field_name = "test_var3"
    default = "default"

    res = get_from_env(field_name, default=default)
    assert default == res
