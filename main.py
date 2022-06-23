import asyncio
import logging
import os

from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import dotenv

from bot.handlers.default import register_handlers_default

dotenv.load_dotenv()
logger = logging.getLogger("main")


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Начать"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/stop", description="Остановить"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt='%d/%m %H:%M:%S'
    )
    logger.info("Configuring...")

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_default(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())