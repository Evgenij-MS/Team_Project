from datetime import datetime

class Task:
    def __init__(self, name, deadline):
        ##############################################
        # NAME
        #self.id = 0
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Имя должно быть строкой !")
        ##############################################
        # DEADLINE
        try:
            self.deadline = datetime.strptime(deadline, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Срок должен быть в формате ДД.ММ.ГГГГ!")
        ###############################################################
        # ID
        self.id = None

    def __repr__(self):
        return f"Task(name={self.name}, deadline={self.deadline.strftime('%d.%m.%Y')}, id={self.id})"

    def __str__(self):
        return f"имя: {self.name} deadline: {self.deadline.strftime('%d.%m.%Y')} номер: {self.id}"
