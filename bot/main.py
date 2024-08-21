import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from settings.config import BotConfig

from entities.databases.postgres.models.tasks_model import Task
from entities.databases.postgres.models.user_model import User

from entities.containers.database.postgres_container import PostgresContainer
from entities.containers.database.redis_container import UserRedisContainer
from entities.containers.database.redis_container import TasksRedisContainer


async def main(
    config: BotConfig, dispatcher: Dispatcher, postgres: PostgresContainer,
    user_redis: UserRedisContainer, tasks_redis: TasksRedisContainer
) -> None:

    postgres.config.host.from_value(config.db_host)
    postgres.config.port.from_value(config.db_port)
    postgres.config.user.from_value(config.db_user)
    postgres.config.password.from_value(config.db_password)
    postgres.config.database.from_value(config.db_database)

    user_redis.config.host.from_value(config.redis_host)
    user_redis.config.port.from_value(config.redis_port)
    user_redis.config.db.from_value(1)

    tasks_redis.config.host.from_value(config.redis_host)
    tasks_redis.config.port.from_value(config.redis_port)
    tasks_redis.config.db.from_value(2)

    postgres.config.host(config)


    bot = Bot(token = config.token)

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(
        main = main(
            config = BotConfig(),
            dispatcher = Dispatcher(),
            postgres = PostgresContainer(),
            user_redis = UserRedisContainer(),
            tasks_redis = TasksRedisContainer(),
        )
    )
    
