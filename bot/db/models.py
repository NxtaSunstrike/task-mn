# bot/db/models.py
import datetime
from sqlalchemy import Column, Integer, VARCHAR, TEXT, ForeignKey, BOOLEAN, TIMESTAMP
from bot.db.base_model import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    
    tg_user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(32))
    date_joined = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.datetime.utcnow)

    def __str__(self) -> str:
        return f"Username: {self.username} - Telegram User ID:{self.tg_user_id}"


class Tasks(BaseModel):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(VARCHAR(255))
    description = Column(TEXT)
    status = Column(BOOLEAN, default=False, nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.tg_user_id", ondelete="CASCADE"), nullable=False)

    def __str__(self) -> str:
        return f"{self.id}. Title: {self.title}, Status: {self.status}"