from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("postgresql_url")

print(f"TOKEN: {TOKEN}")
print(f"DATABASE_URL: {DATABASE_URL}")