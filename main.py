import atexit
import time
import pickle

from parking import Parking
from plaza import Plaza

print('\n\n\n\n-----No detenga el programa de manera manual o no se guardarán los cambios realizados-----')
time.sleep(3)

repetir = True

# plazas = []
#
# for i in range(1, 71):
#     plazas.append(Plaza(i, "turismo", 0.12, False, False))
#
# for i in range(71, 86):
#     plazas.append(Plaza(i, "motocicleta", 0.12, False, False))
#
# for i in range(86, 101):
#     plazas.append(Plaza(i, "reducido", 0.12, False, False))


with open('PyRking.pkl', 'rb') as arc:
    parking = pickle.load(arc)
    arc.close()


# parking = Parking(plazas)


@atexit.register
def pre_exit():
    print('Estamos saliendo de Latam manito')
    with open("PyRking.pkl", 'wb') as arc:
        pickle.dump(parking, arc)
        arc.close()


parking.anadir_abonado("12345678q", "1234asd", 'turismo')

ticket = parking.depositar('turismo', '1234qwe')
print(ticket)
print(parking.retirar('1234qwe', ticket.plaza.id, ticket.pin))
ticket = parking.depositar_abonado('1234asd', '12345678q')
print(ticket)
print(parking.retirar_abonado('1234asd', ticket.plaza.id, ticket.pin))

print(parking)

while repetir:
    seccion = 0
    while seccion != 1 and seccion != 2 and seccion != 3:
        try:
            seccion = int(input("Seleccione zona a acceder\n1. Zona usuario\n2. Zona administrador\n3. Salir"))
            if seccion != 1 and seccion != 2 and seccion != 3:
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
                    accion = int(
                        input("¿Bienvenido, ¿que quiere hacer?\n1. Depositar mi vehiculo\n2. Retirar mi vehiculo"))
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
                            dni = input("Introduzca su dni")
                        except:
                            print("Introduzca un número")
                    ticket = parking.depositar_abonado(matricula, dni)
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
                correcto = False

                while not correcto:
                    matricula = ''
                    plaza = ''
                    pin = 0
                    salir = 0
                    while 100000 > pin < 999999:
                        try:
                            matricula = input("Introduzca su matricula")
                            plaza = int(input("Introduzca su plaza"))
                            pin = int(input("Introduzca su pin"))
                        except:
                            print("Introduzca un número")
                    respuesta = parking.retirar_abonado(matricula, plaza, pin)
                    if respuesta == 'Datos correctos':
                        correcto = True
                        print(respuesta)
                        print("Retire su vehiculo")
                    else:
                        print(respuesta)
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
            accion = -1
            while accion != 1 and accion != 2:
                try:
                    accion = int(
                        input("¿Bienvenido, ¿que quiere hacer?\n1. Depositar mi vehiculo\n2. Retirar mi vehiculo"))
                    if accion != 1 and accion != 2:
                        print("Introduzca una opción válida")
                except:
                    print("Introduzca un número")
            if accion == 1:
                correcto = False

                while not correcto:
                    matricula = ''
                    tipo = 0
                    salir = 0

                    print(parking)
                    while tipo < 1 or tipo > 3:
                        try:
                            matricula = input("Introduzca su matricula")
                            tipo = int(input("Tipo de vehiculo\n1. Turismo\n2. Motocicleta\n3. Movilidad reducida"))
                        except:
                            print("Introduzca un número")
                    if tipo == 1:
                        tipo = 'turismo'
                    elif tipo == 2:
                        tipo = 'motocicleta'
                    elif tipo == 3:
                        tipo = 'reducido'
                    ticket = parking.depositar(tipo, matricula)
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
                correcto = False

                while not correcto:
                    matricula = ''
                    plaza = ''
                    pin = 0
                    salir = 0
                    while 100000 >= pin <= 999999:
                        try:
                            matricula = input("Introduzca su matricula")
                            plaza = int(input("Introduzca su plaza"))
                            pin = int(input("Introduzca su pin"))
                        except:
                            print("Introduzca un número")
                    respuesta = parking.retirar(matricula, plaza, pin)
                    if respuesta != 'Datos Incorrectos':
                        correcto = True
                        print(respuesta)
                        print("Retire su vehiculo")
                    else:
                        print(respuesta)
                        try:
                            salir = int(input("¿Quiere salir?\n1. Sí\n2. No"))
                            if salir == 1:
                                correcto = True
                            elif salir != 2:
                                correcto = True
                                raise Exception()
                        except:
                            print("No ha introducido una opción valida, saliendo...")
    elif seccion == 2:
        salir_admin = False
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n_____Administrador_____')
        while not salir_admin:
            opcion = 0
            while opcion not in [1, 2, 3, 4, 5, 6]:
                try:
                    opcion = int(input("1. Estado Parking\n"
                                       "2. Facturación\n"
                                       "3. Consulta Abonados\n"
                                       "4. Abonos\n"
                                       "5. Caducidad Abonos\n"
                                       "6. Salir"))
                    if opcion not in [1, 2, 3, 4, 5, 6]:
                        print("Sección no valida")
                except:
                    print("Introduzca un número")
            if opcion == 1:
                print(parking.estadoParking())
            elif opcion == 2:
                fechas = 0
                fecha0 = None
                fechaf = None
                while fechas != 2:
                    try:
                        ano = int(input('Introduce un año'))  # XD
                    except:
                        print('Introduce un número')
            elif opcion == 3:
                1
            elif opcion == 4:
                1
            elif opcion == 5:
                1
            elif opcion == 6:
                salir_admin = True
    elif seccion == 3:
        repetir = False
