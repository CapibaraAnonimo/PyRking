import datetime

from dateutil.relativedelta import relativedelta

from abono import Abono
from ticket import *
from transaccion import Transaccion
from vehiculo import Vehiculo


class Parking:
    def __init__(self, plazas):
        self._plazas = plazas
        self._tickets = []
        self._abonados = []
        self._transacciones = []

    @property
    def plazas(self):
        return self._plazas

    @plazas.setter
    def plazas(self, a):
        self._plazas = a

    @property
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, a):
        self._tickets = a

    @property
    def abonados(self):
        return self._abonados

    @abonados.setter
    def abonados(self, a):
        self._abonados = a

    @property
    def transacciones(self):
        return self._transacciones

    @transacciones.setter
    def transacciones(self, a):
        self._transacciones = a

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
        lista_turismos_ocupados = []
        turismos_abonado = 0
        turismos_ocupados_abonado = 0
        lista_turismos_ocupados_abonado = []
        motocicletas = 0
        motocicletas_ocupados = 0
        lista_motocicletas_ocupados = []
        motocicletas_abonados = 0
        motocicletas_ocupados_abonados = 0
        lista_motocicletas_ocupados_abonados = []
        reducidos = 0
        reducidos_ocupados = 0
        lista_reducidos_ocupados = []
        reducidos_abonados = 0
        reducidos_ocupados_abonados = 0
        lista_reducidos_ocupados_abonados = []

        for i in self.plazas:
            if i.tipo == 'turismo':
                if not i.abonada:
                    turismos += 1
                    turismos_ocupados = turismos_ocupados + 1 if i.ocupada else turismos_ocupados
                    if i.ocupada:
                        lista_turismos_ocupados.append(i)
                else:
                    turismos_abonado += 1
                    turismos_ocupados_abonado = turismos_ocupados_abonado + 1 if i.ocupada else turismos_ocupados_abonado
                    if i.ocupada:
                        lista_turismos_ocupados_abonado.append(i)

            if i.tipo == 'motocicleta':
                if not i.abonada:
                    motocicletas += 1
                    motocicletas_ocupados = motocicletas_ocupados + 1 if i.ocupada else motocicletas_ocupados
                    if i.ocupada:
                        lista_motocicletas_ocupados.append(i)
                else:
                    motocicletas_abonados += 1
                    motocicletas_ocupados_abonados = motocicletas_ocupados_abonados + 1 if i.ocupada else motocicletas_ocupados_abonados
                    if i.ocupada:
                        lista_motocicletas_ocupados_abonados.append(i)

            if i.tipo == 'reducido':
                if not i.abonada:
                    reducidos += 1
                    reducidos_ocupados = reducidos_ocupados + 1 if i.ocupada else reducidos_ocupados
                    if i.ocupada:
                        lista_reducidos_ocupados.append(i)
                else:
                    reducidos_abonados += 1
                    reducidos_ocupados_abonados = reducidos_ocupados_abonados + 1 if i.ocupada else reducidos_ocupados_abonados
                    if i.ocupada:
                        lista_reducidos_ocupados_abonados.append(i)

        return f"Turismos: {turismos_ocupados}/{turismos}\n" \
               f"    Plazas Turismos ocupadas: {''.join(str(l) + ', ' for l in lista_turismos_ocupados)}\n" \
               f"Turismos abonados: {turismos_ocupados_abonado}/{turismos_abonado}\n" \
               f"    Plazas Turismos abonados ocupadas: {''.join(str(l) + ', ' for l in lista_turismos_ocupados_abonado)}\n" \
               f"Motocicleta: {motocicletas_ocupados}/{motocicletas}\n" \
               f"    Plazas Motocicletas ocupadas: {''.join(str(l) + ', ' for l in lista_motocicletas_ocupados)}\n" \
               f"Motocicleta abonados: {motocicletas_ocupados_abonados}/{motocicletas_abonados}\n" \
               f"    Plazas Motocicletas abonadas ocupadas: {''.join(str(l) + ', ' for l in lista_motocicletas_ocupados_abonados)}\n" \
               f"Movilidad Reducida: {reducidos_ocupados}/{reducidos}\n" \
               f"    Plazas Movilidad Reducida ocupadas: {''.join(str(l) + ', ' for l in lista_reducidos_ocupados)}\n" \
               f"Movilidad Reducida abonadas: {reducidos_ocupados_abonados}/{reducidos_abonados}\n" \
               f"    Plazas Movilidad Reducida abonadas ocupadas: {''.join(str(l) + ', ' for l in lista_reducidos_ocupados_abonados)}\n"

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
        abonado = next((i for i in self.abonados if i.dni == dni), -1)
        if abonado != -1:
            abonado.modificar(nombre, apellidos, tarjeta)
            print(f'Se modificó el abono con dni {dni}')
        else:
            print(f'No se encontró ningún abono con dni {dni}')

    def listar_abonos(self):
        cadena = '-----Lista de Abonados-----'
        for a in self.abonados:
            cadena = cadena + f'\n{a.nombre} {a.apellidos}:\n    Dni: {a.dni}'
        return cadena

    def renovar_abono(self, dni, meses):
        abonado = next((i for i in self.abonados if i.dni == dni), -1)
        if abonado != -1:
            abonado.renovar(meses)
            return f'Tendrá  abono hasta {abonado.desactivacion}'
        else:
            return f'No se encontró ningún abono con dnni {dni}'

    def baja_abono(self, dni):
        abonado = next((i for i in self.abonados if i.dni == dni), -1)
        if abonado != -1:
            abonado.baja()
            return 'Se dio de baja el abono'
        return 'No existe ese abono'

    def caducidad_abonos(self, fecha, dias):
        for a in self.abonados:
            if fecha <= a.desactivacion <= (fecha + relativedelta(days=dias)):
                print(a)
