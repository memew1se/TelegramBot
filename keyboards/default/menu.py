from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Git"),
            KeyboardButton(text="SSH")
        ]
    ],
    resize_keyboard=True
)
