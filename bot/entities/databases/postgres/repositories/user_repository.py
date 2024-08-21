from typing import Dict

from sqlalchemy import select, delete, update, insert
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession



class UserRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session_factory: AsyncSession = session


    async def create_user(self, telegram_id: int) -> Dict[str: int]:
        async with self.session_factory() as session:
            ...
            