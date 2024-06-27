from aiogram import Dispatcher, F, types
from aiogram.filters.command import Command

from modules.bot.keyboards.default import add_delete_button
from modules.logger import Logger


@Logger.log_msg
async def start(message: types.Message) -> None:
    text = "Start message"
    await message.reply(text, reply_markup=add_delete_button().as_markup())
    return None


@Logger.log_msg
async def help_handler(message: types.Message) -> None:
    text = "Help message"
    await message.reply(text, reply_markup=add_delete_button().as_markup())
    return


async def delete_msg(query: types.CallbackQuery) -> None:
    if not isinstance(query.message, types.Message):
        return
    if query.bot is None:
        return
    try:
        await query.bot.delete_message(query.message.chat.id, query.message.message_id)
        if query.message.reply_to_message:
            await query.bot.delete_message(query.message.chat.id, query.message.reply_to_message.message_id)
        await query.answer()
    except Exception as exc:
        Logger.error(exc)
        await query.answer("Error")


def register_handlers_default(dp: Dispatcher) -> None:
    dp.message.register(start, Command("start"))
    dp.message.register(help_handler, Command("help"))

    dp.callback_query.register(
        delete_msg,
        F.func(lambda c: c.data == "delete"),
    )
