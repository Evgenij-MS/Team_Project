# "Вынести отдельно файл настроек"

def Add_task(task_tracker):
    print("Добавление задачи...")
    name = input("Введите имя задачи:")
    deadline = input("Введите срок выполнения задачи:")
    task_tracker.add_task(name, deadline)


    return task_tracker