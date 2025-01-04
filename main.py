import project_1 #файл содержит функции для добавления задач и просмотра задач по исполнителю.
import project_2 #файл содержит функцию для удаления задач
import project_3 #файл содержит функцию для изменения статуса задач
import project_4 #файл содержит функцию для отображения всех задач
import project_5 #файл содержит функцию для отображения задач по статусу
import project_6 #айл содержит функцию для отображения сроков выполнения задач
import project_7 #файл содержит функцию для завершения работы приложения

import TaskTracker
import json

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def save_config(config):
    with open('config.json', 'w') as file:
        json.dump(config, file)

def main():
    config = load_config()
    tracker = TaskTracker.TaskTracker(config)

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Изменить статус задачи")  # выполнено/не выполнено/в процессе
        print("4. Посмотреть все задачи")
        print("5. Посмотреть статус задач")
        print("6. Посмотреть срок выполнения задач")
        print("7. Показать/скрыть выполненные задания")
        print("8. Посмотреть задачи по исполнителю")
        print("9. Завершить работу")

        choice = input("Выберите действие: ")

        if choice == "1":
            project_1.add_task(tracker)
            tracker.save_tasks()

        elif choice == "2":
            project_2.delete_task(tracker)
            tracker.save_tasks()

        elif choice == "3":
            project_3.change_task_status(tracker)
            tracker.save_tasks()

        elif choice == "4":
            project_4.view_all_tasks(tracker)

        elif choice == "5":
            project_5.view_task_status(tracker)

        elif choice == "6":
            project_6.view_task_deadlines(tracker)

        elif choice == "7":
            tracker.toggle_show_completed()
            tracker.save_tasks()

        elif choice == "8":
            project_1.view_tasks_by_assignee(tracker)

        elif choice == "9":
            project_7.app_exit()
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 9.")

if __name__ == "__main__":
    main()
