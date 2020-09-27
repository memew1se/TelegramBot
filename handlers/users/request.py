from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from states.request_states import RequestGroup
from utils.misc.parcer import parse

from loader import dp, bot


@dp.message_handler(state=RequestGroup.R_git)
async def find_git_command(message: Message, state: FSMContext):
    await message.answer(parse("git-" + message["text"]))
    await state.finish()


@dp.message_handler()
async def find_command(message: Message):
    await message.answer(parse(message["text"]))
