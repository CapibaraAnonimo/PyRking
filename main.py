from parking import *
from plaza import *

repetir = True

plazas = []

for i in range(1, 71):
    plazas.append(Plaza(i, "turismo", 0.12, False, False))

for i in range(71, 86):
    plazas.append(Plaza(i, "motocicleta", 0.12, False, False))

for i in range(86, 101):
    plazas.append(Plaza(i, "reducido", 0.12, False, False))

parking = Parking(plazas)

parking.anadir_abonado("qqqqqqq1", "1234asd", 'turismo')

ticket = None

ticket = parking.depositar('turismo', '1234qwe')
print(ticket)
# print(parking.retirar('1234qwe', ticket.plaza.id, ticket.pin))
ticket = parking.depositar_abonado('1234asd', 'qqqqqqq1')
print(ticket)

# print(parking.retirar('1234qwe', ticket.plaza.id, ticket.pin))

while repetir:
    print(parking)
    repetir = False
