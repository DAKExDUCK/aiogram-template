from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import dotenv

from modules.bot.handlers.default import register_handlers_default
from modules.bot.handlers.admin import register_handlers_admin
from modules.logger import Logger

dotenv.load_dotenv()


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/stop", description="Остановить"),
        BotCommand(command="/get_logfile", description="Получить Logs (admin)"),
    ]
    await bot.set_my_commands(commands)


async def main(bot: Bot, dp: Dispatcher) -> None:
    Logger.info("Configuring...")

    register_handlers_default(dp)
    register_handlers_admin(dp)

    await set_commands(bot)

    await dp.start_polling(bot)
