from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def echo(message: Message):
    with open("lain.jpg", "rb") as photo:
        text = f"Привет, ты написал {message.text}"
        await message.reply_photo(photo, caption=text)
