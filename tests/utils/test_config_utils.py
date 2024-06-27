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


def test_get_from_env5():
    field_name = "test_var4"
    value = "5"
    default = 5
    os.environ[field_name] = value

    res = get_from_env(field_name, default=default, value_type=int)
    assert int(value) == res


def test_get_from_env6():
    field_name = "test_var5"
    default = 5

    res = get_from_env(field_name, default=default, value_type=int)
    assert default == res
