from aiogram.types import Message

async def create_task(message: Message) -> None:
    # Logic to create a new task
    await message.answer("Task created!")

async def list_tasks(message: Message) -> None:
    # Logic to list all tasks
    await message.answer("Here are your tasks...")