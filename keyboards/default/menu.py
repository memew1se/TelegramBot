from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Git"),
            KeyboardButton(text="SSH")
        ],
        [
            KeyboardButton(text="Never mind...")
        ]
    ],
    resize_keyboard=True
)
