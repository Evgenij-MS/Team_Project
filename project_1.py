# "Внести отдельно файл настроек

import TaskTracker

def Add_task(tracker): # task_tracker --> LIST[all_tasks]
    #print("\nДобавление новой задачи...")
    name = input("Введите имя задачи: ")
    deadline = input("Введите срок выполнения задачи: ")
    tracker.add_task(name, deadline)

