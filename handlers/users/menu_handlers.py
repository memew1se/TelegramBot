from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from middlewares import rate_limit
from loader import dp


@rate_limit(2)
@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Chose shell ", reply_markup=menu)


@rate_limit(2)
@dp.message_handler(Text(equals=["Git", "git"]))
async def git_shell(message: Message):
    await message.answer(f"Enter commands for Git ", reply_markup=ReplyKeyboardRemove())


@rate_limit(2)
@dp.message_handler(Text(equals=["ssh", "SSH"]))
async def ssh_shell(message: Message):
    await message.answer(f"Enter commands for SSH ", reply_markup=ReplyKeyboardRemove())
