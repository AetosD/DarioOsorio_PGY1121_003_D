from Asiento import *


def llenar(arreglo):
    x = 1
    for f in range(10):
        for c in range(10):
            arreglo[f][c] = x
        x = x+1


def mostrar(arreglo):
    x = 0
    for f in arreglo:
        filer = ''
        for c in arreglo:
            x = x+1
            arreglo[f][c] = x
            print(filer + arreglo[f][c] + ' | ')


def validarcanentradas():
    c = False
    while not c:
        print("---------------------------------------")
        try:
            can_entradas = int(input("Seleccione cantidad entradas (1-3): "))
            if 1 <= can_entradas <= 3:
                c = True
                return can_entradas
            else:
                print("---------------------------------------")
                print("Cantidad ingresada no valida")
        except BaseException as error_can:
            print(f"Error: {error_can}")


def validarasiento(arreglo):
    c = False
    while not c:
        asiento_ingresado = int(input("Ingrese el numero del asiento:"))
        for asiento_ingresado in arreglo:
            if arreglo != 'XX':
                c = True
                return asiento_ingresado
            else:
                print("El siento esta ocupado")
                c = False


def comprarentrada(arreglo, lista):
    asiento = Asiento()
    can_entradas = validarcanentradas()
    mostrar(arreglo)
    asiento_elejido = validarasiento(arreglo)
    x = 0
    while can_entradas != x:
        try:
            c = False
            while not c:
                c = asiento.setrut("Ingrese el rut (ej. 11111111): ")
            print("---------------------------------------")
            print("Ingreso exitoso")
            print("---------------------------------------")
            lista.append(arreglo)
        except BaseException as error_num:
            print(f"Error: {error_num}")


def ganancias(arreglo):
    cantidad_plat = 0
    cantidad_gold = 0
    cantidad_silver = 0
    for f in arreglo:
        for c in arreglo:
            if 1 <= arreglo[f][c] <= 20 and arreglo == 'XX':
                cantidad_plat = cantidad_plat + 1
            elif 21 <= arreglo[f][c] <= 50 and arreglo == 'XX':
                cantidad_gold = cantidad_gold + 1
            elif 21 <= arreglo[f][c] <= 50 and arreglo == 'XX':
                cantidad_silver = cantidad_silver + 1
    valor_plat = cantidad_plat * 120000
    valor_gold = cantidad_gold * 80000
    valor_silver = cantidad_silver * 50000
    can_total = cantidad_plat+cantidad_gold+cantidad_silver
    valor_total = valor_silver + valor_gold + valor_plat
    print("----------------------------------------------------------")
    print("Platinum $120.000" + ' | ' + cantidad_plat + ' | ' + '$' + valor_plat)
    print("Gold $80.000" + ' | ' + cantidad_plat + ' | ' + '$' + valor_gold)
    print("Silver $50.000" + ' | ' + cantidad_plat + ' | ' + '$' + valor_silver)
    print("----------------------------------------------------------")
    print("Total" + ' | ' + can_total + ' | ' + valor_total)


def salir():
    print("---------------------------------------")
    print("---------------------------------------")
    print("Cerrando sistema")
    print("Desarrollado por Darío Osorio")
    print("Version: 2.0.0")
    print("---------------------------------------")
    print("---------------------------------------")
    return False
