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

parking.anadir_abonado("12345678q", "1234asd", 'turismo')

ticket = None

ticket = parking.depositar('turismo', '1234qwe')
print(ticket)
print(parking.retirar('1234qwe', ticket.plaza.id, ticket.pin))
ticket = parking.depositar_abonado('1234asd', '12345678q')
print(ticket)

print(parking.retirar_abonado('1234asd', ticket.plaza.id, ticket.pin))

while repetir:
    print(parking)
    repetir = False

seccion = 0
while seccion != 1 and seccion != 2:
    try:
        seccion = int(input("Seleccione zona a acceder\n1. Zona usuario\n2. Zona administrador"))
        if seccion != 1 and seccion != 2:
            print("Introduzca una sección válida")
    except:
        print("Introduzca un número")
if seccion == 1:
    abonado = -1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n_____Zona de Clientes_____")
    while abonado != 1 and abonado != 2:
        try:
            abonado = int(input("¿Tienes un abono?\n1. Sí\n2. No"))
            if abonado != 1 and abonado != 2:
                print("Introduzca una opción válida")
        except:
            print("Introduzca un número")
    if abonado == 1:
        accion = -1
        while accion != 1 and accion != 2:
            try:
                accion = int(input("¿Bienvenido, ¿que quiere hacer?\n1. Depositar mi vehiculo\n2. Retirar mi vehiculo"))
                if accion != 1 and accion != 2:
                    print("Introduzca una opción válida")
            except:
                print("Introduzca un número")
        if accion == 1:
            correcto = False

            while not correcto:
                matricula = ''
                dni = ''
                salir = 0
                while len(dni) != 9:
                    try:
                        matricula = input("Introduzca su matricula")
                        # tipo = int(input("Tipo de vehiculo\n1. Turismo\n2. Motocicleta\n3. Movilidad reducida"))
                        dni = input("Introduzca su dni")
                    except:
                        print("Introduzca un número")
                ticket = parking.depositar_abonado(matricula, dni)
                print(ticket)
                if ticket != -1:
                    correcto = True
                    print(ticket)
                else:
                    print("Datos inválidos")
                    try:
                        salir = int(input("¿Quiere salir?\n1. Sí\n2. No"))
                        if salir == 1:
                            correcto = True
                        elif salir != 2:
                            correcto = True
                            raise Exception()
                    except:
                        print("No ha introducido una opción valida, saliendo...")

else:
    1
