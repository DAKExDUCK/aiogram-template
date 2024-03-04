from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)


def add_delete_button(kb: InlineKeyboardMarkup | None = None) -> InlineKeyboardMarkup:
    if kb is None:
        kb = InlineKeyboardMarkup()
    del_btn = InlineKeyboardButton(
            'Delete', 
            callback_data=f'delete',
    )
    kb.add(del_btn)

    return kb
