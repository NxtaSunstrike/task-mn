import sys
import os

# Add the parent directory of the bot directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine, update, delete
from bot.db.models import User, Tasks, BaseModel
from dotenv import load_dotenv
from bot.utils import log_action  # Ensure this is the correct path


load_dotenv()
DATABASE_URL = os.getenv("postgresql_url")
engine = create_engine(DATABASE_URL)
session = Session(bind=engine)
print(os.getenv("postgresql_url"), "from database.py")


async def start_db():

    with engine.connect():
        BaseModel.metadata.create_all(bind=engine)



async def shutdown_db():
    session.close()
    engine.dispose()

async def add_user(username: str, id: int):
    with session as ses:
        stmt = select(User).where(User.tg_user_id == id)
        user = ses.execute(stmt).all()
        if not user:
            ses.add(User(username=username, tg_user_id=id))
            ses.commit()
            log_action().info("User Added to Database")

async def add_task(title: str, description: str, owner_id: int):
    with session as ses:
        task = Tasks(title=title, description=description, owner_id=owner_id)
        ses.add(task)
        ses.commit()
        log_action().info("Task Added to Database")

async def get_tasks(id: int):
    with session as ses:
        stmt = select(Tasks).where(Tasks.owner_id == id)
        tasks = ses.execute(stmt).scalars().all()
        return tasks

async def change_task_status(task_id: int, owner_id: int):
    with session as ses:
        stmt = update(Tasks).where(Tasks.id == task_id, Tasks.owner_id == owner_id).values(status=True)
        ses.execute(stmt)
        ses.commit()
        log_action().info("Task Status Updated")

async def delete_task_from_db(task_id: int, owner_id: int):
    with session as ses:
        stmt = delete(Tasks).where(Tasks.id == task_id, Tasks.owner_id == owner_id)
        ses.execute(stmt)
        ses.commit()
        log_action().info("Task Deleted from Database")