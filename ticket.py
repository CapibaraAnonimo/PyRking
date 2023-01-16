from datetime import *
import random


class Ticket:
    def __init__(self, matricula, plaza):
        self.matricula = matricula
        self.fecha = datetime.strptime('01/16/23 10:00:26', '%m/%d/%y %H:%M:%S')
        self.plaza = plaza
        self.pin = random.randint(100000, 1000000)

    def __str__(self):
        return f"-- Ticket --\n" \
               f"Matricula: {self.matricula}\n" \
               f"Fecha de inicio: {self.fecha}\n" \
               f"Plaza asignada: {self.plaza.id}\n" \
               f"Pin de seguridad: {self.pin}"
