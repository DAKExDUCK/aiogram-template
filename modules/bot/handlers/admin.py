from aiogram import Dispatcher, types
from aiogram.filters.command import Command

from modules.bot.functions.rights import IsAdmin


async def send_log(message: types.Message) -> None:
    logs = types.FSInputFile("logs.log")
    await message.reply_document(logs)


def register_handlers_admin(dp: Dispatcher) -> None:
    dp.message.register(send_log, IsAdmin(), Command("get_logfile"))
