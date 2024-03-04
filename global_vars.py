from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from modules.classes import Suspendable


bot_task: Suspendable | None = None
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
