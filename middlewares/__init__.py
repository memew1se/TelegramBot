from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware, rate_limit


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())