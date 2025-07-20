from dotenv import load_dotenv
import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from colorama import init, Fore
from env import username, password, cluster
from cats_db import cats

# Ініціалізація кольорового виводу
init(autoreset=True)
load_dotenv()

client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}", server_api=ServerApi('1'))
db = client.cats_hw3
cats_collection = db.cats

def add_sample_cats():
    cats_collection.delete_many({})
    cats_collection.insert_many(cats)
    print(Fore.GREEN + "Коти успішно додані.")

def get_all_cats():
    try:
        cats = cats_collection.find()
        for cat in cats:
            print(Fore.CYAN + str(cat))
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def get_cat_by_name(name):
    try:
        cat = cats_collection.find_one({"name": name})
        if cat:
            print(Fore.GREEN + str(cat))
        else:
            print(Fore.YELLOW + f"Кота з ім'ям {name} не знайдено.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def update_cat_age(name, new_age):
    try:
        result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(Fore.GREEN + f"Вік кота {name} оновлено.")
        else:
            print(Fore.YELLOW + f"Кота не знайдено.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def add_feature_to_cat(name, new_feature):
    try:
        result = cats_collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count > 0:
            print(Fore.GREEN + f"Характеристика додана.")
        else:
            print(Fore.YELLOW + f"Кота не знайдено.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def delete_cat_by_name(name):
    try:
        result = cats_collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(Fore.GREEN + f"Кота {name} видалено.")
        else:
            print(Fore.YELLOW + f"Не знайдено.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def delete_all_cats():
    try:
        result = cats_collection.delete_many({})
        print(Fore.GREEN + f"Видалено: {result.deleted_count}")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

def interactive_menu():
    while True:
        print(Fore.MAGENTA + "\n🧠 Виберіть дію:")
        print("1. Всі коти")
        print("2. Пошук кота")
        print("3. Оновити вік")
        print("4. Додати фічу")
        print("5. Видалити кота")
        print("6. Очистити всю базу")
        print("0. Вихід")
        choice = input(">> ")

        if choice == "1":
            get_all_cats()
        elif choice == "2":
            get_cat_by_name(input("Ім’я: "))
        elif choice == "3":
            update_cat_age(input("Ім’я: "), int(input("Новий вік: ")))
        elif choice == "4":
            add_feature_to_cat(input("Ім’я: "), input("Нова фіча: "))
        elif choice == "5":
            delete_cat_by_name(input("Ім’я: "))
        elif choice == "6":
            delete_all_cats()
        elif choice == "0":
            print("👋 До зустрічі!")
            break
        else:
            print(Fore.RED + "Невідома команда.")

if __name__ == "__main__":
    add_sample_cats()
    interactive_menu()
