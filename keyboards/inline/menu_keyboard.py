from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

shell_callback = CallbackData("shell", "shell_name")

shell_keyboard = InlineKeyboardMarkup(row_width=1)

git_button = InlineKeyboardButton(text="git", callback_data=shell_callback.new(shell_name="git"))
shell_keyboard.insert(git_button)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
shell_keyboard.insert(cancel_button)

