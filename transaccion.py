from datetime import *


class Transaccion:
    def __init__(self, importe):
        self.fecha = datetime.now()
        self.importe = importe

    def __str__(self):
        return str(self.importe)
