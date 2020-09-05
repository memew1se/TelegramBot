from loader import dp
from aiogram.types import Message


@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, ты написал {message.text}"
    await message.answer(text=text)
