import asyncio

from aiogram import Bot, Dispatcher

from settings.config import BotConfig


async def main(config: BotConfig) -> None:

    bot = Bot(token = config.token)
    dispatcher = Dispatcher()
    
    await dispatcher.start_polling(bot)


if '__name__' == '__main__':
    asyncio.run(
        main = main()
    )
    
