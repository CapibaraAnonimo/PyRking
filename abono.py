import datetime
import random
from dateutil.relativedelta import relativedelta

from transaccion import Transaccion


class Abono:
    def __init__(self, dni, vehiculo, id_plaza, meses, tarjeta):
        self.dni = dni
        self.vehiculo = vehiculo
        self.id_plaza = id_plaza
        self.pin = random.randint(100000, 1000000)
        self.meses = meses
        self.activacion = datetime.datetime.now()
        self.desactivacion = self.activacion + relativedelta(months=meses)
        self.tarjeta = tarjeta
        self.transacciones = []
        self.add_transaccion(self.meses)

    def add_transaccion(self, meses):
        if meses == 1:
            self.transacciones.append(Transaccion(25))
        elif meses == 3:
            self.transacciones.append(Transaccion(70))
        elif meses == 6:
            self.transacciones.append(Transaccion(130))
        elif meses == 12:
            self.transacciones.append(Transaccion(200))

    def reactivar(self, meses):
        if meses in [1, 3, 6, 12]:
            self.meses = meses
            self.activacion = datetime.datetime.now()
            self.desactivacion = self.activacion + relativedelta(months=meses)
            print(f"Se reactivó correctamente el abono con {meses} meses")
