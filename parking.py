import datetime

from abono import Abono
from ticket import *
from transaccion import Transaccion
from vehiculo import Vehiculo


class Parking:
    def __init__(self, plazas):
        self._plazas = plazas
        self.tickets = []
        self.abonados = []
        self.transacciones = []

    @property
    def plazas(self):
        return self._plazas

    @plazas.setter
    def plazas(self, a):
        self._plazas = a

    def __str__(self):
        turismos = 0
        turismos_ocupados = 0
        motocicletas = 0
        motocicletas_ocupados = 0
        reducidos = 0
        reducidos_ocupados = 0

        for i in self.plazas:
            if i.tipo == 'turismo' and not i.abonada:
                turismos += 1
                turismos_ocupados = turismos_ocupados + 1 if i.ocupada else turismos_ocupados

            if i.tipo == 'motocicleta' and not i.abonada:
                motocicletas += 1
                motocicletas_ocupados = motocicletas_ocupados + 1 if i.ocupada else motocicletas_ocupados

            if i.tipo == 'reducido' and not i.abonada:
                reducidos += 1
                reducidos_ocupados = reducidos_ocupados + 1 if i.ocupada else reducidos_ocupados

        return f"Turismos: {turismos_ocupados}/{turismos}\n" \
               f"Motocicleta: {motocicletas_ocupados}/{motocicletas}\n" \
               f"Movilidad Reducida: {reducidos_ocupados}/{reducidos}"

    def depositar(self, tipo, matricula):  # TODO hacer esto bien y manejar que no hay sitio suficiente
        plaza = self.asignar_plaza(tipo)
        valido = True
        for t in self.tickets:
            if t.matricula == matricula:
                valido = False
        if plaza != -1 and valido:
            ticket = Ticket(matricula, plaza)
            self.tickets.append(ticket)
            return ticket
        else:
            return -1

    def depositar_abonado(self, matricula, dni):
        abonado = next((i for i in self.abonados if i.dni == dni and i.vehiculo.matricula == matricula), -1)
        if abonado != -1:
            plaza = next((i for i in self.plazas if (i.id == abonado.id_plaza)), -1)
            plaza.ocupada = True
            ticket = Ticket(matricula,
                            plaza,
                            abonado.pin)
            self.tickets.append(ticket)
            return ticket
        else:
            return -1

    def retirar(self, matricula, id_plaza, pin):
        ticket = next(
            (i for i in self.tickets if i.matricula == matricula and i.plaza.id == id_plaza and i.pin == pin), -1)

        if ticket != -1 and not ticket.plaza.abonada:
            ticket.plaza.ocupada = False
            self.tickets.remove(ticket)
            importe = round((((datetime.datetime.now() - ticket.fecha).total_seconds() / 60.0) * ticket.plaza.precio),
                            2)
            self.transacciones.append(Transaccion(importe))
            return f"Tiene que pagar {importe}€"
        else:
            return "Datos Incorrectos"

    def retirar_abonado(self, matricula, id_plaza, pin):
        ticket = next(
            (i for i in self.tickets if i.matricula == matricula and i.plaza.id == id_plaza and i.pin == pin), -1)
        if ticket != -1 and ticket.plaza.abonada:
            ticket.plaza.ocupada = False
            self.tickets.remove(ticket)
            return f"Datos correctos"
        else:
            return "Datos Incorrectos"

    def asignar_plaza(self, tipo):
        i = next((i for i in self.plazas if not i.ocupada and i.tipo == tipo and not i.abonada), -1)
        if i != -1:
            i.ocupada = True
        return i

    def estado_parking(self):
        turismos = 0
        turismos_ocupados = 0
        turismos_abonado = 0
        turismos_ocupados_abonado = 0
        motocicletas = 0
        motocicletas_ocupados = 0
        motocicletas_abonados = 0
        motocicletas_ocupados_abonados = 0
        reducidos = 0
        reducidos_ocupados = 0
        reducidos_abonados = 0
        reducidos_ocupados_abonados = 0

        for i in self.plazas:
            if i.tipo == 'turismo':
                if not i.abonada:
                    turismos += 1
                    turismos_ocupados = turismos_ocupados + 1 if i.ocupada else turismos_ocupados
                else:
                    turismos_abonado += 1
                    turismos_ocupados_abonado = turismos_ocupados_abonado + 1 if i.ocupada else turismos_ocupados_abonado

            if i.tipo == 'motocicleta':
                if not i.abonada:
                    motocicletas += 1
                    motocicletas_ocupados = motocicletas_ocupados + 1 if i.ocupada else motocicletas_ocupados
                else:
                    motocicletas_abonados += 1
                    motocicletas_ocupados_abonados = motocicletas_ocupados_abonados + 1 if i.ocupada else motocicletas_ocupados_abonados

            if i.tipo == 'reducido':
                if not i.abonada:
                    reducidos += 1
                    reducidos_ocupados = reducidos_ocupados + 1 if i.ocupada else reducidos_ocupados
                else:
                    reducidos_abonados += 1
                reducidos_ocupados_abonados = reducidos_ocupados_abonados + 1 if i.ocupada else reducidos_ocupados_abonados

        return f"Turismos: {turismos_ocupados}/{turismos}\n" \
               f"Turismos abonados: {turismos_ocupados_abonado}/{turismos_abonado}\n" \
               f"Motocicleta: {motocicletas_ocupados}/{motocicletas}\n" \
               f"Motocicleta abonados: {motocicletas_ocupados_abonados}/{motocicletas_abonados}\n" \
               f"Movilidad Reducida: {reducidos_ocupados}/{reducidos}\n" \
               f"Movilidad Reducida abonados: {reducidos_ocupados_abonados}/{reducidos_abonados}"

    def facturacion(self, fecha0, fechaf):
        total = 0
        numero = 0
        for fac in self.transacciones:
            if fecha0 <= fac.fecha <= fechaf:
                total += fac.importe
                numero += 1
        return numero, total

    def consulta_abonos(self):
        if len(self.abonados) < 1:
            print('No hay abonados')
        else:
            for a in self.abonados:
                if a.desactivacion > datetime.datetime.now():
                    print(a)

    def anadir_abonado(self, dni, matricula, tipo, meses, tarjeta, nombre, apellidos):
        correcto = True
        for i in self.abonados:
            if dni == i.dni or matricula == i.vehiculo.matricula:
                correcto = False
        plaza = self.asignar_plaza(tipo)
        plaza.ocupada = False

        if correcto and plaza != -1:
            plaza.abonada = True
            abonado = Abono(dni, Vehiculo(matricula, tipo), plaza.id, meses, tarjeta, nombre, apellidos)
            self.abonados.append(abonado)
            return "Se creo correctamente el abonado"
        elif not correcto:
            return "O el dni o la matricula ya está registrada en el sistema"
        else:
            return 'No hay hueco ahora mismo'

    def modificar_abono(self, dni, nombre, apellidos, tarjeta):

