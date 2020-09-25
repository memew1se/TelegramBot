from aiogram.types import Message

from utils.misc.parcer import parse

from loader import dp, bot


@dp.message_handler()
async def find_command(message: Message):
    await message.answer(parse(message["text"]))
