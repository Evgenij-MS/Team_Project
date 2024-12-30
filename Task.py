

class Task:
    def __init__(self, name, deadline):

        self.id = 0
        if isinstance(name, str):
            self.name = name

        else:
            raise TypeError("Имя должно быть строкой !")
        if isinstance(deadline, str):  #возможно нужно сделать тип datetime
            self.deadline = deadline
        else:
            raise TypeError("Срок должен быть строкой !")

    def __str__(self):
        return f"{self.name}     дедлайн: {self.deadline}     номер:{self.id}"