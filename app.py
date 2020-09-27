from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import BOT_TOKEN, ADMIN_ID


async def on_startup(dp):
    import middlewares
    middlewares.setup(dp)

    from utils.misc import on_startup_notify
    await on_startup_notify(dp)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
