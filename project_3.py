def change_task_status(tracker):
    task_id = input("Введите ID задачи для изменения статуса: ")
    new_status = input("Введите новый статус задачи (OPEN, IN_PROGRESS, COMPLETED, OVERDUE): ")
    tracker.change_task_status(task_id, new_status)
    print("Статус задачи изменен.")

#файл содержит функцию для изменения статуса задач
#Запрашивает у пользователя идентификатор задачи и новый статус,
# затем изменяет статус задачи с указанным идентификатором.