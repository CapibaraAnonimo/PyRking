import datetime
import random


class Ticket:
    def __init__(self, matricula, plaza, pin=random.randint(100000, 1000000)):
        self._matricula = matricula
        self._fecha = datetime.datetime.now()
        self._plaza = plaza
        self._pin = pin

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, a):
        self._matricula = a

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, a):
        self._fecha = a

    @property
    def plaza(self):
        return self._plaza

    @plaza.setter
    def plaza(self, a):
        self._plaza = a

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, a):
        self._pin = a

    def __str__(self):
        return f"-- Ticket --\n" \
               f"Matricula: {self.matricula}\n" \
               f"Fecha de inicio: {self.fecha}\n" \
               f"Plaza asignada: {self.plaza.id}\n" \
               f"Pin de seguridad: {self.pin}"
