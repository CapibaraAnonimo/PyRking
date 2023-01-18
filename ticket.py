import datetime
import random


class Ticket:
    def __init__(self, matricula, plaza, pin=random.randint(100000, 1000000)):
        self.matricula = matricula
        self.fecha = datetime.datetime.strptime('01/16/23 10:00:26',
                                                '%m/%d/%y %H:%M:%S')  # TODO esto hay que ponerlo en now antes de entregar
        self.plaza = plaza
        self.pin = pin

    def __str__(self):
        return f"-- Ticket --\n" \
               f"Matricula: {self.matricula}\n" \
               f"Fecha de inicio: {self.fecha}\n" \
               f"Plaza asignada: {self.plaza.id}\n" \
               f"Pin de seguridad: {self.pin}"
