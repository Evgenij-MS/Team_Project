#файл содержит функцию для удаления задач
#Запрашивает у пользователя идентификатор задачи и удаляет задачу с этим идентификатором из трекера.

def delete_task(tracker):
    task_id = input("Введите ID задачи для удаления: ")
    tracker.remove_task(task_id)
    print("Задача удалена.")
