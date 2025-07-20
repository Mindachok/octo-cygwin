import json, os

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as read_task:
        try:
            data = json.load(read_task)
            task = data.get("active", [])
            task_completed = data.get("completed", [])
        except json.JSONDecodeError:
            task = []
            task_completed = []
else:
    with open("tasks.json", "w") as write_task:
        json.dump({"active": [], "completed": []}, write_task)
    task = []
    task_completed = []


def back_menu():
    while True:
        return_menu = input("Хотите вернуться в меню? Да [y] 😊, Нет [n] 👋: ")
        if return_menu.lower() == "y":
            menu()
            break
        elif return_menu.lower() == "n":
            print("Спасибо за использование программы! До свидания! 👋")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова. 🤔")
            continue


def menu():
    while True:
        try:
            choice = int(input(
                "\nЗдравствуйте! 👋\nВыберите действие:\n"
                "1. Посмотреть список текущих задач 📋\n"
                "2. Добавить новую задачу ➕\n"
                "3. Отметить задачу как выполненную ✅\n"
                "4. Посмотреть список выполненных задач 🎉\n"
                "5. Удалить задачу 🗑️\n"
                "6. Выйти из программы 🚪\n"
                "Ваш выбор: "))
        except ValueError:
            print("Пожалуйста, вводите только цифры от 1 до 6. ❌")
            continue

        if choice == 1:
            read_task()
            break
        elif choice == 2:
            append_task()
            break
        elif choice == 3:
            mark_completed()
            break
        elif choice == 4:
            show_completed()
            break
        elif choice == 5:
            delete_task()
            break
        elif choice == 6:
            print("Выход из программы. До новых встреч! 👋")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите число от 1 до 6. 🤨")


def avto_save():
    with open("tasks.json", "w") as f:
        json.dump({"active": task, "completed": task_completed}, f)


def append_task():
    add_task = input("Введите новую задачу ✍️: ")
    if add_task.strip():
        task.append(add_task.strip())
        avto_save()
        print("Задача успешно добавлена! 🎉")
    else:
        print("Пустая задача не может быть добавлена. 🚫")
    back_menu()


def read_task():
    if not task:
        print("У вас пока нет активных задач. Добавьте новую! 😊")
    else:
        print("\nСписок текущих задач 📋:")
        for index, value in enumerate(task):
            print(f"{index + 1}. {value}")
    back_menu()


def delete_task():
    if not task:
        print("Список задач пуст. Нет задач для удаления. 😕")
        back_menu()
        return

    print("\nСписок задач 📝:")
    for index, value in enumerate(task):
        print(f"{index + 1}. {value}")

    while True:
        try:
            delete = int(input("Введите номер задачи, которую хотите удалить 🗑️: "))
            if delete < 1 or delete > len(task):
                print(f"Ошибка: введите число от 1 до {len(task)}. ⚠️")
            else:
                deleted_task = task.pop(delete - 1)
                avto_save()
                print(f"Задача '{deleted_task}' была удалена. 🗑️")
                break
        except ValueError:
            print("Ошибка: вводите только цифры. 🚫")
    back_menu()


def mark_completed():
    if not task:
        print("У вас нет активных задач для отметки. 😌")
        back_menu()
        return

    print("\nСписок текущих задач 📋:")
    for index, value in enumerate(task):
        print(f"{index + 1}. {value}")

    while True:
        try:
            complet = int(input("Введите номер задачи, которую вы выполнили ✅: "))
            if complet < 1 or complet > len(task):
                print(f"Пожалуйста, введите число от 1 до {len(task)}. ⚠️")
            else:
                completed_task = task.pop(complet - 1)
                task_completed.append(completed_task)
                avto_save()
                print(f"Задача '{completed_task}' успешно отмечена как выполненная! 🎉")
                break
        except ValueError:
            print("Пожалуйста, вводите только цифры. 🚫")
    back_menu()


def show_completed():
    if not task_completed:
        print("Пока нет выполненных задач. Вперед к делам! 🚀")
    else:
        print("\nСписок выполненных задач 🎊:")
        for index, value in enumerate(task_completed):
            print(f"{index + 1}. {value}")
    back_menu()
menu()