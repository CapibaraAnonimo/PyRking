import random


class Abono:
    def __init__(self, dni, vehiculo, id_plaza):
        self.dni = dni
        self.vehiculo = vehiculo
        self.id_plaza = id_plaza
        self.pin = random.randint(100000, 1000000)
