from os import environ as env

from pydantic_settings import BaseSettings
from pydantic import Field


class BotConfig(BaseSettings):
    token: str = Field(env.get('TOKEN'))


class RedisConfig(BaseSettings):
    host: str = Field(env.get('redis-host'))
    port: int = Field(env.get('redis-port'))


class PostgresConfig(BaseSettings):
    host: str = Field(env.get('postgres-host'))
    port: int = Field(env.get('postgres-port'))
    user: str = Field(env.get('postgres-user'))
    password: str = Field(env.get('postgres-password'))
    database: str = Field(env.get('postgres-database'))