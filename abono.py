import datetime
import random
from dateutil.relativedelta import relativedelta

from transaccion import Transaccion


class Abono:
    def __init__(self, dni, vehiculo, id_plaza, meses, tarjeta, nombre, apellidos):
        self._dni = dni
        self._vehiculo = vehiculo
        self._id_plaza = id_plaza
        self._pin = random.randint(100000, 1000000)
        self._meses = meses
        self._activacion = datetime.datetime.now()
        self._desactivacion = self.activacion + relativedelta(months=meses)
        print(self.desactivacion)
        self._tarjeta = tarjeta
        self._transacciones = []
        self.add_transaccion(self.meses)
        self._nombre = nombre
        self._apellidos = apellidos

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, a):
        self._dni = a

    @property
    def vehiculo(self):
        return self._vehiculo

    @vehiculo.setter
    def vehiculo(self, a):
        self._vehiculo = a

    @property
    def id_plaza(self):
        return self._id_plaza

    @id_plaza.setter
    def id_plaza(self, a):
        self._id_plaza = a

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, a):
        self._pin = a

    @property
    def meses(self):
        return self._meses

    @meses.setter
    def meses(self, a):
        self._meses = a

    @property
    def activacion(self):
        return self._activacion

    @activacion.setter
    def activacion(self, a):
        self._activacion = a

    @property
    def desactivacion(self):
        return self._desactivacion

    @desactivacion.setter
    def desactivacion(self, a):
        self._desactivacion = a

    @property
    def tarjeta(self):
        return self._tarjeta

    @tarjeta.setter
    def tarjeta(self, a):
        self._tarjeta = a

    @property
    def transacciones(self):
        return self._transacciones

    @transacciones.setter
    def transacciones(self, a):
        self._transacciones = a

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, a):
        self._nombre = a

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, a):
        self._apellidos = a

    def __str__(self):
        cadena = f'Dni: {self.dni}:'
        for t in self.transacciones:
            cadena = cadena + f'\n    {t}'
        return cadena

    def add_transaccion(self, meses):
        if meses == 1:
            self.transacciones.append(Transaccion(25))
        elif meses == 3:
            self.transacciones.append(Transaccion(70))
        elif meses == 6:
            self.transacciones.append(Transaccion(130))
        elif meses == 12:
            self.transacciones.append(Transaccion(200))

    def renovar(self, meses):
        self.meses = meses
        if self.desactivacion < datetime.datetime.now():
            self.activacion = datetime.datetime.now()
            self.desactivacion = self.activacion + relativedelta(months=meses)
        else:
            self.desactivacion = self.desactivacion + relativedelta(months=meses)
        self.add_transaccion(meses)
        print(f"Se renovó correctamente el abono con {meses} meses")

    def modificar(self, nombre, apellidos, tarjeta):
        if nombre != '':
            self.nombre = nombre
        if apellidos != '':
            self.apellidos = apellidos
        if tarjeta != '':
            self.tarjeta = tarjeta

    def baja(self):
        self.meses = 0
        self.desactivacion = datetime.datetime.now()
        self.nombre = ''
        self.apellidos = ''
        self.tarjeta = ''
        self.vehiculo = None
