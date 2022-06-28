from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.handlers.logger import print_msg
from bot.keyboards.default import (add_delete_button)
from bot.handlers.logger import logger
from bot.functions.rights import admin_list


@print_msg
async def start(message: types.Message, state: FSMContext):
    text = "Start message"
    await message.reply(text, reply_markup=add_delete_button(None))


@print_msg
async def stop(message: types.Message, state: FSMContext):
    text = "Stop message"
    await message.reply(text)
    await state.finish()


@print_msg
async def help(message: types.Message):
    text = "Help message"
    await message.reply(text)


@print_msg
async def msg_to_admin(message: types.Message):
    await message.reply(f"Message to Admin `{admin_list[0]}`, "
                        f"reply to this message to send message",
                        parse_mode='MarkdownV2')


async def delete_msg(query: types.CallbackQuery):
    await query.answer()
    try:
        await query.bot.delete_message(query.message.chat.id, query.message.message_id)
        if query.message.reply_to_message:
            await query.bot.delete_message(query.message.chat.id, query.message.reply_to_message.message_id)
    except Exception as exc:
        logger.error(exc)
        await query.answer("Error with deleting, message is too old")


def register_handlers_default(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(stop, commands="stop", state="*")
    dp.register_message_handler(help, commands="help", state="*")
    dp.register_message_handler(msg_to_admin, commands="msg_to_admin", state="*")

    dp.register_callback_query_handler(
        delete_msg,
        lambda c: c.data == "delete",
        state="*"
    )
