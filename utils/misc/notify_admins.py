from aiogram import dispatcher
from data.config import ADMIN_ID


async def on_startup_notify(dp: dispatcher):
    await dp.bot.send_message(ADMIN_ID, "Бот запущен")
