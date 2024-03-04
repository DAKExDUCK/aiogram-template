from aiogram.types import BotCommand
import dotenv

from .handlers.default import register_handlers_default
from .handlers.admin import register_handlers_admin
from ..logger import Logger

dotenv.load_dotenv()


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/stop", description="Остановить"),
        BotCommand(command="/get_logfile", description="Получить Logs (admin)"),
    ]
    await bot.set_my_commands(commands)


async def main(bot, dp):
    Logger.info("Configuring...")
    
    register_handlers_default(dp)
    register_handlers_admin(dp)

    await set_commands(bot)

    await dp.start_polling()
