from aiogram.utils.keyboard import InlineKeyboardBuilder

from modules.bot.keyboards import default


def test_add_delete_button1():
    kb = default.add_delete_button()
    button = next(kb.buttons)

    assert button.text == "Delete"
    assert button.callback_data == "delete"


def test_add_delete_button2():
    kb = default.add_delete_button(InlineKeyboardBuilder())
    button = next(kb.buttons)

    assert button.text == "Delete"
    assert button.callback_data == "delete"
