import numpy as np
from Funciones import *
arreglo_asientos = np.full((10, 10), '--')
lista_asientos = []
asiento = Asiento()
com = True
while com:
    print("Eventos Creativos.cl")
    print("---------------------------------------")
    print("Menu")
    print("---------------------------------------")
    print("1) Comprar entrada")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asientos")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    try:
        op_menu = int(input("Seleccione (1-5): "))
        match op_menu:
            case 1:
                comprarentrada(arreglo_asientos, lista_asientos)
            case 2:
                mostrar(arreglo_asientos)
            case 3:
                print("")
                # listaasientos(lista_asientos)
            case 4:
                ganancias(arreglo_asientos)
            case 5:
                com = salir()
    except BaseException as error_menu:
        print(f"Error: {error_menu}")
