from aiogram import Bot, Dispatcher, executor
from config import bot_token


bot = Bot(bot_token, parse_mode='HTML')
dp = Dispatcher(bot)


if __name__ == '__main__':
    from handlers import send_to_admin, dp
    executor.start_polling(dp, on_startup=send_to_admin)