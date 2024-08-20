import sys
import os

# Add the parent directory of the bot directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiogram import Bot, Dispatcher
from handlers import (
    start_handler,
    invalid_answer,
    on_startup,
    on_shutdown,
    add_command,
    get_task_desc,
    get_task_name,
    done_task,
    get_all_tasks,
    change_task_by_id,
    delete_task,
    delete_task_by_id,
    show_keyboard,
)
from dotenv import load_dotenv
import asyncio

from aiogram.filters import Command
from aiogram import F

from utils.stateforms import StepsForm

load_dotenv(encoding='utf-8')
TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("postgresql_url")

print(f"TOKEN from main: {TOKEN}")
print(f"DATABASE_URL from main: {DATABASE_URL}")

async def main() -> None:
    print("Starting main function")
    bot = Bot(TOKEN)
    dp = Dispatcher()

    print("Registering startup and shutdown handlers")
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    print("Registering message handlers")
    dp.message.register(start_handler, Command(commands=["start", "run"]))
    dp.message.register(show_keyboard, Command(commands=["keyboard"]))

    # ADD TASK
    dp.callback_query.register(add_command, F.data == "add_task")
    dp.message.register(get_task_name, StepsForm.GET_task_title)
    dp.message.register(get_task_desc, StepsForm.GET_task_description)

    # LIST TASKS
    dp.callback_query.register(get_all_tasks, F.data == "list_all_task")

    # Done Task
    dp.callback_query.register(done_task, F.data == "done_task")
    dp.message.register(change_task_by_id, StepsForm.CHANGE_task_status)

    # Delete Task
    dp.callback_query.register(delete_task, F.data == "delete_task")
    dp.message.register(delete_task_by_id, StepsForm.DELETE_task_by_id)

    # Other Message Handler
    dp.message.register(invalid_answer)
    print("Starting polling")
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Running main function")
    asyncio.run(main())