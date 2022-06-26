from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.functions.functions import clear_MD
from bot.functions.rights import is_admin


@is_admin
async def send_log(message: types.Message):
    with open('logs.log', 'r') as logs:
        await message.reply_document(logs)


@is_admin
async def forwarded_msg(message: types.Message):
    if message.is_forward:
        text = ""
        if message.forward_from_chat:
            text += f"Chat id: `{clear_MD(message.forward_from_chat.id)}`\n"
        if message.forward_from:
            if message.forward_from.is_premium:
                text += ":star:\n"
            if message.forward_from.is_bot:
                text += "BOT\n"
            text += f"User id: `{clear_MD(message.forward_from.id)}`\n"
            if message.forward_from.full_name:
                text += f"Full name: `{clear_MD(message.forward_from.full_name)}`\n"
            if message.forward_from.username:
                text += f"Mention: @{clear_MD(message.forward_from.username)}\n"
        if message.forward_sender_name:
            text += f"Sender name: `{clear_MD(message.forward_sender_name)}`\n"
        if message.forward_from_message_id:
            text += f"Msg id: `{clear_MD(message.forward_from_message_id)}`\n"
        if len(text) > 0:
            try:
                await message.reply(text, parse_mode='MarkdownV2')
            except:
                await message.reply(text)


def register_handlers_secondary(dp: Dispatcher):
    dp.register_message_handler(send_log, commands="get_logfile", state="*")

    dp.register_message_handler(forwarded_msg, state="*")
