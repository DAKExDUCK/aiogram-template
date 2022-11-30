from aiogram import Dispatcher, types
from ..functions.rights import IsAdmin


async def send_log(message: types.Message):
    with open('logs.log', 'r') as logs:
        await message.reply_document(logs)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(send_log, IsAdmin(), commands="get_logfile", state="*")
