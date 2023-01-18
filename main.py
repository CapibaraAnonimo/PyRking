import atexit
import datetime
import time
import pickle

from parking import Parking
from plaza import Plaza

print('\n\n\n\n-----No detenga el programa de manera manual o no se guardarán los cambios realizados-----')
time.sleep(0)  # TODO poner esto a 3 antes de entregar

repetir = True

plazas = []

for i in range(1, 71):
    plazas.append(Plaza(i, "turismo", 0.12, False, False))

for i in range(71, 86):
    plazas.append(Plaza(i, "motocicleta", 0.12, False, False))

for i in range(86, 101):
    plazas.append(Plaza(i, "reducido", 0.12, False, False))

# with open('PyRking.pkl', 'rb') as arc:
#     parking = pickle.load(arc)
#     arc.close()


parking = Parking(plazas)


@atexit.register
def pre_exit():
    print('Estamos saliendo de Latam manito')
    with open("PyRking.pkl", 'wb') as arc:
        pickle.dump(parking, arc)
        arc.close()


parking.anadir_abonado("12345678q", "1234asd", 'turismo', 3, '12345678', 'Adrián', 'Arnaiz Cano')

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
            seccion = int(input("Seleccione zona a acceder\n1. Zona usuario\n2. Zona administrador\n3. Salir\n>"))
            if seccion != 1 and seccion != 2 and seccion != 3:
                print("Introduzca una sección válida")
        except:
            print("Introduzca un número")
    if seccion == 1:
        abonado = -1
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n_____Zona de Clientes_____")
        while abonado != 1 and abonado != 2:
            try:
                abonado = int(input("¿Tienes un abono?\n1. Sí\n2. No\n>"))
                if abonado != 1 and abonado != 2:
                    print("Introduzca una opción válida")
            except:
                print("Introduzca un número")
        if abonado == 1:
            accion = -1
            while accion != 1 and accion != 2:
                try:
                    accion = int(
                        input("¿Bienvenido, ¿que quiere hacer?\n1. Depositar mi vehiculo\n2. Retirar mi vehiculo\n>"))
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
                            matricula = input("Introduzca su matricula\n>")
                            dni = input("Introduzca su dni\n>")
                        except:
                            print("Introduzca un número")
                    ticket = parking.depositar_abonado(matricula, dni)
                    if ticket != -1:
                        correcto = True
                        print(ticket)
                    else:
                        print("Datos inválidos")
                        try:
                            salir = int(input("¿Quiere salir?\n1. Sí\n2. No\n>"))
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
                            matricula = input("Introduzca su matricula\n>")
                            plaza = int(input("Introduzca su plaza\n>"))
                            pin = int(input("Introduzca su pin\n>"))
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
                            salir = int(input("¿Quiere salir?\n1. Sí\n2. No\n>"))
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
                        input("¿Bienvenido, ¿que quiere hacer?\n1. Depositar mi vehiculo\n2. Retirar mi vehiculo\n>"))
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
                            matricula = input("Introduzca su matricula\n>")
                            tipo = int(input("Tipo de vehiculo\n1. Turismo\n2. Motocicleta\n3. Movilidad reducida\n>"))
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
                            salir = int(input("¿Quiere salir?\n1. Sí\n2. No\n>"))
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
                            matricula = input("Introduzca su matricula\n>")
                            plaza = int(input("Introduzca su plaza\n>"))
                            pin = int(input("Introduzca su pin\n>"))
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
                            salir = int(input("¿Quiere salir?\n1. Sí\n2. No\n>"))
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
                                       "6. Salir\n>"))
                    if opcion not in [1, 2, 3, 4, 5, 6]:
                        print("Sección no valida")
                except:
                    print("Introduzca un número")
            if opcion == 1:
                print(parking.estado_parking())
            elif opcion == 2:
                fechas = 0
                fecha0 = None
                fechaf = None
                while fechas != 2:
                    try:
                        if fechas == 0:
                            print('Introduce los datos de la fecha de inicio')
                        else:
                            print('Introduce los datos del a fecha final')
                        ano = int(input('Introduce un año\n>'))  # XD
                        mes = int(input('Introduce un mes\n>'))
                        dia = int(input('Introduce un día\n>'))
                        hora = int(input('Introduce un hora\n>'))
                        if fechas == 0:
                            fecha0 = datetime.datetime(ano, mes, dia, hora)
                            if datetime.datetime(2023, 1, 1, 00) <= fecha0 <= datetime.datetime.now():
                                print(fecha0)
                                fechas = 1
                                print('Fecha inicial correcta')
                            else:
                                print('Fecha inicial incorrecta')
                        else:
                            fechaf = datetime.datetime(ano, mes, dia, hora)
                            if datetime.datetime.now() >= fechaf >= datetime.datetime(2023, 1, 1, 00):
                                print(fechaf)
                                fechas = 2
                                print('Fecha final correcta')
                            else:
                                print('Fecha final incorrecta')
                    except:
                        print('Introduce un número')
                facturacion = parking.facturacion(fecha0, fechaf)
                print(f'Ha habido {facturacion[0]} transacciones, por un total de {facturacion[1]}€')
            elif opcion == 3:
                parking.consulta_abonos()
            elif opcion == 4:
                ab_opcion = 0

                while ab_opcion not in [1, 2, 3]:
                    try:
                        ab_opcion = int(
                            input(
                                '1. Dar de alta un nuevo abono\n2. Modificar un abonado\n3. Dar de baja\n>'))  # TODO añadir un salir
                        if ab_opcion not in [1, 2, 3]:
                            print('Introduce una opción válida')
                    except:
                        print('Introduce un número')
                if ab_opcion == 1:
                    alta_correcto = False
                    dni = ''
                    matricula = ''
                    tipo = 0
                    meses = 0
                    tarjeta = 0
                    nombre = ''
                    apellido = ''

                    while not alta_correcto:
                        try:
                            dni = input('Introduce el dni')
                            matricula = input('Introduce la matricula')
                            tipo = int(input("Tipo de vehiculo\n1. Turismo\n2. Motocicleta\n3. Movilidad reducida\n>"))
                            meses = int(input("Meses de abono\n1. 1 mes\n2. 3 meses\n3. 6 meses\n4. 12 meses\n>"))
                            tarjeta = input("Introduce la tarjeta\n>")
                            nombre = input('Introduce el nombre\n>')
                            apellido = input('Introduce los apellidos\n>')
                        except:
                            print('Introduce un número')
                        if tipo == 1:
                            tipo = 'turismo'
                        elif tipo == 2:
                            tipo = 'motocicleta'
                        elif tipo == 3:
                            tipo = 'reducido'

                        if meses == 1:
                            meses = 1
                        elif meses == 2:
                            meses = 3
                        elif meses == 3:
                            meses = 6
                        elif meses == 4:
                            meses = 12
                        if tipo in ['turismo', 'motocicleta', 'reducido'] and meses in [1, 3, 6, 12] \
                                and nombre != '' and apellido != '':
                            alta_correcto = True
                            print(parking.anadir_abonado(dni, matricula, tipo, meses, tarjeta, nombre, apellido))
                        else:
                            print('Datos incorrectos')
                elif ab_opcion == 2:
                    mod_opcion = 0

                    while not mod_opcion not in [1, 2, 3]:
                        try:
                            mod_opcion = int(input('1. Modificar datos de un abonado\n2. Renovar abono\n3. Salir'))
                            if mod_opcion not in [1, 2, 3]:
                                print('Introduzca una sección válida')
                        except:
                            print('Introduce un número')
                    if mod_opcion == 1:
                        print('Para dejar el campo como está pulse intro sin introducir nada')

                        nombre = input('Introduce el nuevo nombre')
                        apellidos = input('Introduce los nuevos apellidos')
                        tarjeta = input('Introduce la nuevas tarjeta')

                    elif mod_opcion == 2:
                        1
                else:
                    1
            elif opcion == 5:
                1
            elif opcion == 6:
                salir_admin = True
    elif seccion == 3:
        repetir = False
