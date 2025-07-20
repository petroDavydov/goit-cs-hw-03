import time
import seed
import main_query_app
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    # Дати базі запуститись
    time.sleep(5)

    print(f"... Стартуємо заповнення бази...")
    seed.clear_tables()
    seed.insert_statuses()
    seed.insert_users()
    seed.insert_tasks()
    print(f" ... Дані згенеровано. Запускаємо консольний інтерфейс...\n")

    main_query_app.run()