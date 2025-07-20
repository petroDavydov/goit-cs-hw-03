from queries import *
from config import DB_PARAMS
import psycopg2


def show_menu():
    print(" ... Виберіть дію ...:")
    print("0. Вихід")
    print("1. Показати таблицю користувачів")
    print("2. Показати статуси")
    print("3. Показати таблицю завдань")
    print("4. Отримати всі завдання певного користувача")
    print("5. Вибрати завдання за певним статусом")
    print("6. Оновити статус завдання")
    print("7. Користувачі без завдань")
    print("8. Додати нове завдання")
    print("9. Незавершені завдання")
    print("10. Видалити завдання")
    print("11. Знайти користувача за email")
    print("12. Оновити ім’я користувача")
    print("13. Кількість завдань по статусах")
    print("14. Завдання по домену пошти")
    print("15. Завдання без опису")
    print("16. Завдання у статусі 'in progress'")
    print("17. Кількість завдань кожного користувача")


def execute_query(query: str):
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        conn.close()
    except Exception as e:
        print(f" !!! Помилка: {e} !!!")


def run():
    while True:
        show_menu()
        choice = input("Ваш вибір: ").strip()

        if choice == "0":
            print("👋 Вихід з програми.")
            break

        elif choice == "1":
            execute_query("SELECT * FROM users;")

        elif choice == "2":
            execute_query("SELECT * FROM status;")

        elif choice == "3":
            execute_query("SELECT * FROM tasks;")

        elif choice == "4":
            user_id = input("Введіть user_id: ")
            execute_query(all_from_specific_user(user_id))

        elif choice == "5":
            status_id = input("Введіть status_id: ")
            execute_query(status_specific_task(status_id))

        elif choice == "6":
            task_id = input("Введіть task_id: ")
            status_id = input("Новий status_id: ")
            execute_query(update_status_task(task_id, status_id))

        elif choice == "7":
            execute_query(users_without_tasks())

        elif choice == "8":
            user_id = input("user_id: ")
            title = input("title: ")
            description = input("description: ")
            status_id = input("status_id: ")
            execute_query(add_new_task_for_user(
                user_id, title, description, status_id))

        elif choice == "9":
            execute_query(not_completed_tasks())

        elif choice == "10":
            task_id = input("id завдання: ")
            execute_query(delete_task(task_id))

        elif choice == "11":
            email = input("Email або домен: ")
            execute_query(find_users_by_email(email))

        elif choice == "12":
            user_id = input("user_id: ")
            new_name = input("Нове ім’я: ")
            execute_query(update_user_name(user_id, new_name))

        elif choice == "13":
            execute_query(count_tasks_by_status())

        elif choice == "14":
            domain = input("Домен чи  краще пошту (наприклад, @gmail.com): ")
            execute_query(find_user_by_email_domain(domain))

        elif choice == "15":
            execute_query(tasks_without_description())

        elif choice == "16":
            execute_query(user_in_progress_tasks())

        elif choice == "17":
            execute_query(user_tasks_count())

        else:
            print(" Невідома команда або тестується.")


if __name__ == "__main__":
    run()
