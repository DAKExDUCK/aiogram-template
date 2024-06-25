from aiogram import F, Dispatcher, types
from aiogram.fsm.context import FSMContext

from global_vars import bot
from modules.logger import Logger
from modules.bot.keyboards.default import add_delete_button


@Logger.log_msg
async def start(message: types.Message, state: FSMContext) -> None:
    text = "Start message"
    await message.reply(text, reply_markup=add_delete_button().as_markup())
    await state.clear()


@Logger.log_msg
async def help(message: types.Message) -> None:
    text = "Help message"
    await message.reply(text, reply_markup=add_delete_button().as_markup())


async def delete_msg(query: types.CallbackQuery) -> None:
    if not isinstance(query.message, types.Message):
        return
    try:
        await bot.delete_message(query.message.chat.id, query.message.message_id)
        if query.message.reply_to_message:
            await bot.delete_message(query.message.chat.id, query.message.reply_to_message.message_id)
        await query.answer()
    except Exception as exc:
        Logger.error(exc)
        await query.answer("Error")


def register_handlers_default(dp: Dispatcher) -> None:
    dp.message.register(start, commands="start")
    dp.message.register(help, commands="help")

    dp.callback_query.register(
        delete_msg,
        F.func(lambda c: c.data == "delete"),
    )
