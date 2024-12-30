import os
import Task

class TaskTracker:
    def __init__(self):
        self.all_tasks = []
        if os.path.isfile("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for s in file.readlines():
                    f = s.split(sep=":")
                    self.add_task(f[0], f[1])
        else:
            self.all_tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        id = 0
        for t in self.all_tasks:
            if t.id >= id:
                id = t.id
        task.id = id+1

        if not task in self.all_tasks:
            self.all_tasks.append(task)
        else:
            print("Задача уже существует!")


    def show_tasks(self):
        for t in self.all_tasks:
            print(t)


    def del_task(self):
        number = input("Введите номер задачи, которую нужно удалить:")
        i = int(number)
        for n,t in enumerate(self.all_tasks):
            if i == t.id:
                del self.all_tasks[n]
                break
            else :
                raise ValueError("Задачи с таким номером не существует!")
        return number

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for t in self.all_tasks:
                file.write(t.name + ":" + t.deadline + "\n")

