from time import localtime, strftime
from aiogram import dispatcher
from data.config import ADMIN_ID


async def on_startup_notify(dp: dispatcher):
    with open("start_logs.txt", "rt+") as start_log:
        log = start_log.read()
        if len(log) > 0:
            sessions = log.split("\n")
            last_session = sessions[-1].split(" | ")

            new_session_number = int(last_session[0]) + 1
            new_session_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
            start_log.write(f"\n{new_session_number} | {new_session_time}")
        else:
            new_session_number = 0
            new_session_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
            start_log.write(f"{new_session_number} | {new_session_time}")

    await dp.bot.send_message(ADMIN_ID, f"Bot started [{new_session_number}] | {new_session_time}")
