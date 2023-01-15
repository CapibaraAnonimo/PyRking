from datetime import *
import random


class Ticket:
    def __init__(self, matricula, id_plaza):
        self.matricula = matricula
        self.fecha = datetime.now()
        self.id_plaza = id_plaza
        self.pin = random.randint(100000, 1000000)


    def __str__(self):
        return f"Matricula: {self.matricula}"
