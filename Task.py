

class Task:
    def __init__(self, name, deadline):
        ##############################################
        # NAME
        self.id = 0
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Имя должно быть строкой !")
        ##############################################
        # DEADLINE
        if isinstance(deadline, str):  #возможно нужно сделать тип datetime
            self.deadline = deadline
        else:
            raise TypeError("Срок должен быть строкой !")
        ##############################################
    def __str__(self):
        return f"имя: {self.name}     deadline: {self.deadline}     номер: {self.id}"