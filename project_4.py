# "Вывод всех задач"

import TaskTracker # File

def View_all_tasks(task_tracker):
    print("\nВывод всех задач...")
    tracker = TaskTracker.TaskTracker()
    tracker.show_tasks()