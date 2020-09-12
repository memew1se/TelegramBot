from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

import logging

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(format=u'%(filename)s '
                           u'[LINE:%(lineno)d] '
                           u'#%(levelname)-8s '
                           u'[%(asctime)s]  '
                           u'%(message)s',
                    level=logging.INFO,
                    )
