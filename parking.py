from ticket import *


class Parking:
    def __init__(self, plazas):
        self.plazas = plazas
        self.tickets = []

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
        ticket = None
        if plaza != -1:
            ticket = Ticket(matricula, plaza)
            self.tickets.append(ticket)
            return ticket
        else:
            return -1

    def retirar(self, matricula, id_plaza, pin):
        ticket = next(
            (i for i in self.tickets if i.matricula == matricula and i.plaza.id == id_plaza and i.pin == pin), -1)
        if ticket != -1:
            return f"Tiene que pagar {((datetime.now() - ticket.fecha).total_seconds() / 60.0) * ticket.plaza.precio}"
        else:
            return "Datos Incorrectos"

    def asignar_plaza(self, tipo):  # TODO hacer esto con un next
        encontrado = False
        cont = 0
        while not encontrado:
            if cont < len(self.plazas):
                if self.plazas[cont].tipo == tipo and self.plazas[cont].ocupada == False:
                    self.plazas[cont].ocupada = True
                    return self.plazas[cont]
                cont += 1
            else:
                return -1
