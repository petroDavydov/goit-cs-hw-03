import psycopg2
from contextlib import contextmanager
from colorama import init, Fore
from faker import Faker
from random import choice
import os
from dotenv import load_dotenv

# Ініціалізація
init(autoreset=True)
load_dotenv()
fake = Faker()

# Змінні з .env
dbname: str = os.getenv("POSTGRES_DB", "mydb")
dbuser: str = os.getenv("POSTGRES_USER", "dbuser")
dbpassword: str = os.getenv("POSTGRES_PASSWORD", "dbpassword")
dbhost: str = os.getenv("POSTGRES_HOST", "localhost")
dbport: int = int(os.getenv("POSTGRES_PORT", "5432"))

DB_PARAMS = {
    "dbname": dbname,
    "user": dbuser,
    "password": dbpassword,
    "host": dbhost,
    "port": dbport
}
NUMBER_USERS = int(os.getenv("NUMBER_USERS", "10"))
NUMBER_TASKS = int(os.getenv("NUMBER_TASKS", "15"))



@contextmanager
def get_conn():
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        print(Fore.RED + f"!!![Error] {e} !!!")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def clear_tables():
    with get_conn() as cur:
        # Очистити таблиці (починаючи з залежної)
        cur.execute("DELETE FROM tasks;")
        cur.execute("DELETE FROM users;")
        cur.execute("DELETE FROM status;")
    print(Fore.YELLOW + "[↻] Таблиці очищено")

def insert_statuses():
    statuses = ['new', 'in progress', 'completed']
    with get_conn() as cur:
        for status in statuses:
            cur.execute("""
                INSERT INTO status (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
            """, (status,))
    print(Fore.GREEN + " ... Статуси додано ...")

def insert_users(n=NUMBER_USERS):
    with get_conn() as cur:
        for _ in range(n):
            name = fake.name()
            email = fake.unique.email()
            cur.execute("""
                INSERT INTO users (fullname, email)
                VALUES (%s, %s)
            """, (name, email))
    print(Fore.GREEN + f"[✓] Додано {n} користувачів")

def insert_tasks(n=NUMBER_TASKS):
    with get_conn() as cur:
        cur.execute("SELECT id FROM users")
        user_ids = [row[0] for row in cur.fetchall()]
        cur.execute("SELECT id FROM status")
        status_ids = [row[0] for row in cur.fetchall()]

        for _ in range(n):
            title = fake.sentence(nb_words=6)
            description = fake.text()
            user_id = choice(user_ids)
            status_id = choice(status_ids)
            cur.execute("""
                INSERT INTO tasks (title, description, user_id, status_id)
                VALUES (%s, %s, %s, %s)
            """, (title, description, user_id, status_id))
    print(Fore.GREEN + f"... Додано {n} завдань ...")

if __name__ == "__main__":
    clear_tables()
    insert_statuses()
    insert_users()
    insert_tasks()
    print(Fore.CYAN + "!!! База успішно заповнена фейковими даними !!!")
