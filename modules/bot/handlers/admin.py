from aiogram import Dispatcher, types
from ..functions.rights import IsAdmin


async def send_log(message: types.Message) -> None:
    with open('logs.log', 'r') as logs:
        await message.reply_document(logs.read())


def register_handlers_admin(dp: Dispatcher) -> None:
    dp.message.register(send_log, IsAdmin(), commands="get_logfile", state="*")
