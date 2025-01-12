# " Загрузка списка задач из файла и фиксация этого файла в файл настроек"


def change_task_status(self, task_name, new_status):
    """Изменить статус задачи."""
    for task in self.tasks:
        if task["name"] == task_name:
            if new_status in ["не выполнено", "в процессе", "выполнено"]:
                task["status"] = new_status
                print(f"Статус задачи '{task_name}' изменён на '{new_status}'.")
            else:
                print("Некорректный статус. Используйте: 'не выполнено', 'в процессе', 'выполнено'.")
            return
    print(f"Задача '{task_name}' не найдена.")