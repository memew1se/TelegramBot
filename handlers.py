from main import bot, dp
from aiogram.types import Message
from config import ADMIN_ID


async def send_to_admin(*args):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен (ый)')


@dp.message_handler()
async def echo(message: Message):
    with open("lain.jpg", "rb") as photo:
        text = f"Привет, ты написал {message.text}"
        await message.reply_photo(photo, caption=text)
