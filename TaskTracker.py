import os
import Task
import json
from enum import Enum

class TaskStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    OVERDUE = "Overdue"

class Task:
    _id_counter = 1

    def __init__(self, title, description, status, due_date, assignee=None):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.assignee = assignee

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'due_date': self.due_date,
            'assignee': self.assignee
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data['title'],
            description=data['description'],
            status=TaskStatus[data['status'].replace(" ", "_").upper()],
            due_date=data['due_date'],
            assignee=data.get('assignee')
        )
        task.id = data['id']
        Task._id_counter = max(Task._id_counter, task.id + 1)
        return task

class TaskTracker:
    def __init__(self, config):
        self.tasks = []
        self.config = config
        self.load_tasks()
        self.notify_user()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != int(task_id)]

    def change_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.id == int(task_id):
                task.status = TaskStatus[new_status.replace(" ", "_").upper()]
                break

    def display_tasks(self, show_completed=False):
        for task in self.tasks:
            if show_completed:
                if task.status == TaskStatus.COMPLETED:
                    print(f"{task.id}: {task.title} - {task.status.value} - {task.assignee}")
            else:
                if task.status != TaskStatus.COMPLETED:
                    print(f"{task.id}: {task.title} - {task.status.value} - {task.assignee}")

    def display_tasks_by_status(self, status):
        for task in self.tasks:
            if task.status == TaskStatus[status.replace(" ", "_").upper()]:
                print(f"{task.id}: {task.title} - {task.status.value} - {task.assignee}")

    def display_tasks_by_assignee(self, assignee):
        for task in self.tasks:
            if task.assignee == assignee:
                print(f"{task.id}: {task.title} - {task.status.value} - {task.assignee}")

    def display_task_deadlines(self):
        for task in self.tasks:
            print(f"{task.id}: {task.title} - {task.due_date} - {task.assignee}")

    def toggle_show_completed(self):
        self.config['show_completed'] = not self.config.get('show_completed', False)
        self.save_config()
        self.display_tasks(show_completed=self.config['show_completed'])

    def save_tasks(self):
        with open(self.config['tasks_file'], 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        try:
            with open(self.config['tasks_file'], 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл со списком задач не найден или поврежден. Создание нового списка задач.")
            self.tasks = []

    def save_config(self):
        with open('config.json', 'w') as file:
            json.dump(self.config, file, indent=4)

    def notify_user(self):
        print("Уведомления о задачах:")
        for task in self.tasks:
            if task.status in [TaskStatus.OPEN, TaskStatus.OVERDUE]:
                print(f"{task.id}: {task.title} - {task.status.value} - {task.due_date} - {task.assignee}")
