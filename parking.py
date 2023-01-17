from abono import Abono
from ticket import *
from vehiculo import Vehiculo


class Parking:
    def __init__(self, plazas):
        self.plazas = plazas
        self.tickets = []
        self.abonados = []

    def __str__(self):
        turismos = 0
        turismos_ocupados = 0
        motocicletas = 0
        motocicletas_ocupados = 0
        reducidos = 0
        reducidos_ocupados = 0

        for i in self.plazas:
            if i.tipo == 'turismo':
                turismos += 1
                turismos_ocupados = turismos_ocupados + 1 if i.ocupada else turismos_ocupados

            if i.tipo == 'motocicleta':
                motocicletas += 1
                motocicletas_ocupados = motocicletas_ocupados + 1 if i.ocupada else motocicletas_ocupados

            if i.tipo == 'reducido':
                reducidos += 1
                reducidos_ocupados = reducidos_ocupados + 1 if i.ocupada else reducidos_ocupados

        return f"Turismos: {turismos_ocupados}/{turismos}\n" \
               f"Motocicleta: {motocicletas_ocupados}/{motocicletas}\n" \
               f"Movilidad Reducida: {reducidos_ocupados}/{reducidos}"

    def depositar(self, tipo, matricula):  # TODO hacer esto bien y manejar que no hay sitio suficiente
        plaza = self.asignar_plaza(tipo)
        if plaza != -1:
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

    def anadir_abonado(self, dni, matricula, tipo):
        correcto = True
        for i in self.abonados:
            if dni == i.dni or matricula == i.vehiculo.matricula:
                correcto = False
        plaza = self.asignar_plaza(tipo)
        plaza.ocupada = False

        if correcto and plaza.id != -1:
            plaza.abonada = True
            abonado = Abono(dni, Vehiculo(matricula, tipo), plaza.id)
            self.abonados.append(abonado)
            return "Se creo correctamente el abonado"
        else:
            return "Datos invalidos para la creación de un abono"

    def retirar(self, matricula, id_plaza, pin):
        ticket = next(
            (i for i in self.tickets if i.matricula == matricula and i.plaza.id == id_plaza and i.pin == pin), -1)

        if ticket != -1 and not ticket.plaza.abonada:
            ticket.plaza.ocupada = False
            self.tickets.remove(ticket)
            return f"Tiene que pagar {round((((datetime.now() - ticket.fecha).total_seconds() / 60.0) * ticket.plaza.precio), 2)}€"
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
