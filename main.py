from asyncio import run

import global_vars
from modules.bot import main as start
from modules.classes import Suspendable
from modules.logger import Logger


Logger.load_config()

async def start_bot():
    global_vars.bot_task = Suspendable(start(global_vars.bot, global_vars.dp))

if __name__ == "__main__":
    run(start_bot())
