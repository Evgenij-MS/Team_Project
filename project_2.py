# " Загрузка списка задач из файла и фиксация этого файла в файл настроек"

def Delete_task(task_tracker):
    print("\nУдаление задачи")
    print()
    task_tracker.del_task(task_tracker)
    print(f"Вы удалили задачу под номером {task_tracker.de}")