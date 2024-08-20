from bot.db.base_model import BaseModel
from bot.db.database import start_db

async def on_startup():
    await start_db()