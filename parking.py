from ticket import *


class Parking:
    def __init__(self, plazas):
        self.plazas = plazas

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

    def depositar(self, tipo, matricula):
        id_plaza = -1
        for i in self.plazas:
            if i.tipo == tipo and i.ocupada == False: id_plaza = i.id
        return Ticket(matricula, id_plaza)
