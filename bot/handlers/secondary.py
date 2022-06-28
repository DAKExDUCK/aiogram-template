from aiogram import Dispatcher, types
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from bot.functions.functions import clear_MD
from bot.functions.rights import is_Admin, is_admin
from bot.keyboards.default import add_delete_button
from bot.handlers.logger import logger


@is_Admin
async def send_log(message: types.Message):
    with open('logs.log', 'r') as logs:
        await message.reply_document(logs)


async def last_handler(message: types.Message):
    if is_admin(message.from_user.id):
        if message.is_forward():
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
                await message.reply(text, parse_mode='MarkdownV2', reply_markup=add_delete_button(None))
        else:
            if 'User id' in message.reply_to_message.text:
                for row in message.reply_to_message.text.split('\n'):
                    if 'User id' in row:
                        user_id = row.replace('User id: ', '')
                        break
                try:
                    await message.bot.send_message(user_id, f"Message from Admin `{message.from_user.id}`, "
                                                   f"reply to this message to answer:\n\n{message.text}", 
                                                   parse_mode='MarkdownV2')
                    await message.reply_to_message.edit_text(message.reply_to_message.text+'\n\n*Answered*', parse_mode='MarkdownV2')
                except aiogram.exceptions.BotBlocked:
                    await message.reply('Bot blocked by user', reply_markup=add_delete_button(None))
            else:
                if 'Message from ' in message.reply_to_message.text:
                    user_id = message.reply_to_message.text.split('\n')[0].split()[-1].replace(':','')
                    try:
                        await message.bot.send_message(user_id, f"Message from Admin `{message.from_user.id}`, "
                                                    f"reply to this message to answer:\n\n{message.text}", 
                                                    parse_mode='MarkdownV2')
                        await message.reply_to_message.edit_text(message.reply_to_message.md_text+'\n\n*Answered*', parse_mode='MarkdownV2')
                    except aiogram.exceptions.BotBlocked:
                        await message.reply('Bot blocked by user', reply_markup=add_delete_button(None))
    else:
        if 'Message from Admin ' in message.reply_to_message.text:
            text = message.reply_to_message.text.replace('Message from Admin ', '')
            pos = text.find(' ') - 1
            admin_id = int(text[:pos])

            try:
                await message.bot.send_message(admin_id, f"Message from `{message.from_user.full_name}` "
                                           f"[{message.from_user.username}](t.me/{message.from_user.username}) `{message.from_user.id}`:"
                                           f"\n\n{message.text}", parse_mode='MarkdownV2')
                await message.reply_to_message.edit_text(message.reply_to_message.md_text+'\n\n*Answered*', parse_mode='MarkdownV2')
            except Exception as exc:
                logger.error(exc)
                await message.reply("Error while sending message")
            

def register_handlers_secondary(dp: Dispatcher):
    dp.register_message_handler(send_log, commands="get_logfile", state="*")

    dp.register_message_handler(last_handler, state="*")
