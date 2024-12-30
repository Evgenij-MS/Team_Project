import project_1
import project_2
import project_3
import project_4
import project_5
import project_6
import project_7

import TaskTracker
import json

def main():
    tracker = TaskTracker.TaskTracker()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Изменить статус задачи")  #выполнено/не выполнено/в процессе
        print("4. Посмотреть все задачи")
        print("5. Посмотреть статус задач")
        print("6. Посмотреть срок выполнения задач")
        print("7. Завершить работу")

        choice = input("Выберите действие: ")

        if choice == "1":
            project_1.Add_task(tracker)
            tracker.save_tasks()

        elif choice == "2":
            project_2.Delete_task(tracker)
            tracker.save_tasks()


        elif choice == "3":
            project_3.Change_task_status(TaskTracker)

        elif choice == "4":
            project_4.View_all_tasks(TaskTracker.TaskTracker.show_tasks(TaskTracker.TaskTracker.__call__()))

        elif choice == "5":
            project_5.View_task_status(TaskTracker)

        elif choice == "6":
            project_6.View_task_deadlines(TaskTracker)

        elif choice == "7":
            project_7.App_exit()


if __name__ == "__main__":
    main()
