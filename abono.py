import datetime
import random
from dateutil.relativedelta import relativedelta


class Abono:
    def __init__(self, dni, vehiculo, id_plaza, meses, tarjeta):
        self.dni = dni
        self.vehiculo = vehiculo
        self.id_plaza = id_plaza
        self.pin = random.randint(100000, 1000000)
        self.meses = meses
        self.activacion = datetime.datetime.now()
        self.activacion = self.activacion + relativedelta(months=meses)
        self.tarjeta = tarjeta
        self.transacciones = []
