from dotenv import load_dotenv
import os

load_dotenv()

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB", "my-postgres"),
    "user": os.getenv("POSTGRES_USER", "artur"),
    "password": os.getenv("POSTGRES_PASSWORD", "postgress"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", "5432"))
}