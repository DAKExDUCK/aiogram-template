from asyncio import run

import global_vars
from modules.bot import main as start
from modules.logger import Logger

Logger.load_config()


async def start_bot():
    # place for connecting the db or something
    await start(global_vars.bot, global_vars.dp)


if __name__ == "__main__":
    run(start_bot())
