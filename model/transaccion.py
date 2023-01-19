from datetime import *


class Transaccion:
    def __init__(self, importe):
        self._fecha = datetime.now()
        self._importe = importe

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, a):
        self._fecha = a

    @property
    def importe(self):
        return self._importe

    @importe.setter
    def importe(self, a):
        self._importe = a

    def __str__(self):
        return 'Fecha ' + str(self.fecha.replace(microsecond=0)) + '    Importe: ' + str(self.importe)
