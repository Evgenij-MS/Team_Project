# "Внести отдельно файл настроек

import TaskTracker # File


def Add_task(): # task_tracker --> LIST[all_tasks]
    print("\nДобавление новой задачи...")
    name = input("Введите имя задачи: ")
    deadline = input("Введите срок выполнения задачи: ")
    tracker = TaskTracker.TaskTracker()
    tracker.add_task(name=name, deadline=deadline)
