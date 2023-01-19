class Vehiculo:
    def __init__(self, matricula, tipo):
        self._matricula = matricula
        self._tipo = tipo

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, a):
        self._matricula = a

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, a):
        self._tipo = a
