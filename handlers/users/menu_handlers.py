import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from keyboards.inline.menu_keyboard import shell_keyboard,shell_callback
from middlewares import rate_limit

from loader import dp, bot


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Chose shell ", reply_markup=shell_keyboard)


@dp.callback_query_handler(shell_callback.filter(shell_name="git"))
async def git_shell(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Enter commands for Git ")
    await call.message.edit_reply_markup(reply_markup=None)



@dp.callback_query_handler(shell_callback.filter(shell_name="ssh"))
async def ssh_shell(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Enter commands for SSH ")
    await call.message.edit_reply_markup(reply_markup=None)


@dp.callback_query_handler(text="cancel")
async def default_shell(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.edit_reply_markup(reply_markup=None)
