from parking import *
from plaza import *

repetir = True

plazas = []

for i in range(1, 71):
    plazas.append(Plaza(i, "turismo", 0.12, False))

for i in range(71, 86):
    plazas.append(Plaza(i, "motocicleta", 0.12, False))

for i in range(86, 101):
    plazas.append(Plaza(i, "reducido", 0.12, False))


parking = Parking(plazas)

ticket = None

ticket = parking.depositar('turismo', '1234qwe')
print(ticket)

print(parking.retirar('1234qwe', ticket.plaza.id, ticket.pin))

while repetir:
    print(parking)
    repetir = False
