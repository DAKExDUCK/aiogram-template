from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.handlers.logger import print_msg


@print_msg
async def start(message: types.Message, state: FSMContext):
    text = "Start message"
    await message.reply(text)


@print_msg
async def stop(message: types.Message, state: FSMContext):
    text = "Stop message"
    await message.reply(text)
    await state.finish()


@print_msg
async def help(message: types.Message):
    text = "Help message"
    await message.reply(text)


def register_handlers_default(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(stop, commands="stop", state="*")
    dp.register_message_handler(help, commands="help", state="*")
