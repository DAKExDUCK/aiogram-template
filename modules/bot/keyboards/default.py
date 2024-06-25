from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def add_delete_button(kb: InlineKeyboardBuilder | None = None) -> InlineKeyboardBuilder:
    if kb is None:
        kb = InlineKeyboardBuilder()
    del_btn = InlineKeyboardButton(
            text='Delete', 
            callback_data=f'delete',
    )
    kb.add(del_btn)

    return kb
