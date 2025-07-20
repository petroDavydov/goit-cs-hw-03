
# 1.Отримати всі завдання певного користувача
def all_from_specific_user(user_id):
    return f"""
        SELECT *
        FROM tasks
        WHERE user_id = {user_id};
    """

# 2.Вибрати завдання за певним статусом
def status_specific_task(status_id):
    return f"""
        SELECT *
        FROM tasks
        WHERE status_id = {status_id};
    """

# 3.Оновити статус конкретного завдання
def update_status_task(task_id, status_id):
    return f"""
        UPDATE tasks
        SET status_id = {status_id}
        WHERE id = {task_id};
    """

# 4.Отримати список користувачів, які не мають жодного завдання
def users_without_tasks():
    return """
        SELECT *
        FROM users
        WHERE id NOT IN (SELECT user_id FROM tasks);
    """


# 5.Додати нове завдання для конкретного користувача
def add_new_task_for_user(user_id, title, description, status_id):
    return f"""
        INSERT INTO tasks (title, description, user_id, status_id)
        VALUES ('{title}', '{description}', {user_id}, {status_id});
    """


# 6.Отримати всі завдання, які ще не завершено
def not_completed_tasks():
    return """
        SELECT *
        FROM tasks
        WHERE status_id != (
            SELECT id FROM status
            WHERE name = 'completed'
        );
    """


# 7.Видалити конкретне завдання
def delete_task(task_id):
    return f"""
        DELETE FROM tasks
        WHERE id = {task_id};
    """

# 8.Знайти користувачів з певною електронною поштою
def find_users_by_email(email):
    return f"""
        SELECT *
        FROM users
        WHERE email LIKE '%{email}';
    """

# 9.Оновити ім'я користувача
def update_user_name(user_id, new_name):
    return f"""
        UPDATE users
        SET fullname = '{new_name}'
        WHERE id = {user_id};
    """


# 10.Отримати кількість завдань для кожного статусу
def count_tasks_by_status():
    return """
        SELECT status.name, COUNT(tasks.id) AS task_count
        FROM tasks
        JOIN status ON tasks.status_id = status.id
        GROUP BY status.name;
    """


# 11.Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
def find_user_by_email_domain(domain):
    return f"""
        SELECT tasks.*
        FROM tasks
        JOIN users ON tasks.user_id = users.id
        WHERE users.email LIKE '%{domain}';
    """


# 12.Отримати список завдань, що не мають опису
def tasks_without_description():
    return """
        SELECT *
        FROM tasks
        WHERE description IS NULL
        OR description = '';
    """


# 13.Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
def user_in_progress_tasks():
    return """
        SELECT users.fullname, tasks.title
        FROM users
        JOIN tasks ON users.id = tasks.user_id
        WHERE tasks.status_id = (
            SELECT id
            FROM status
            WHERE name = 'in progress'
        );
    """
# 14.Отримати користувачів та кількість їхніх завдань
def user_tasks_count():
    return """
        SELECT users.fullname, COUNT(tasks.id) AS task_count
        FROM users
        LEFT JOIN tasks ON users.id = tasks.user_id
        GROUP BY users.id, users.fullname;

    """