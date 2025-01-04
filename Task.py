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
