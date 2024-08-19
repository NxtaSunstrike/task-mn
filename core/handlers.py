from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from core.dictionary import start_message, help_message
from core.tasks import create_task, list_tasks

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(start_message)

@router.message(Command(commands=['help']))
async def command_help_handler(message: Message) -> None:
    await message.answer(help_message)

@router.message(Command(commands=['newtask']))
async def command_newtask_handler(message: Message) -> None:
    await create_task(message)

@router.message(Command(commands=['tasks']))
async def command_tasks_handler(message: Message) -> None:
    await list_tasks(message)