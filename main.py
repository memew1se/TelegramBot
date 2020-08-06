from aiogram import Bot, Dispatcher, executor
from config import bot_token


bot = Bot(bot_token, parse_mode='HTML')
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling()