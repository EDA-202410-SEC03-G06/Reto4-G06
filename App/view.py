"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    origen_lat = float(input('Ingrese la latitud del origen: '))
    origen_lon = float(input('Ingrese la longitud del origen: '))
    destino_lat = float(input('Ingrese la latitud del destino: '))
    destino_lon = float(input('Ingrese la longitud del destino: '))
    
    origen = (origen_lat,origen_lon)
    destino = (destino_lat, destino_lon)
    # TODO: Imprimir el resultado del requerimiento 1
    ans = controller.req_1(control,origen,destino)
    return ans


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    origen = input('Ingrese el punto de origen con latitud y longitud: ')
    destino = input('Ingrese el destino con latitud y longitud: ')
    # TODO: Imprimir el resultado del requerimiento 2
    ans = controller.req_2(control,origen,destino)
    return ans

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print('Buscando la mayor red de trayectos con menor distancia desde el de mas concurrencia...')
    ans = controller.req_3(control)
    return ans

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print('Buscando la mayor red de rutas de transporte con menor distancia (partiendo con el aereopuerto de mayor carga)...')
    ans = controller.req_4(control)
    return ans

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print('Buscando la mayor red de trayectos en Colombia (desee el de mayor importancia militar)...')
    ans = controller.req_5(control)
    return ans


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    M = int(input('Cantidad de aereopuertos con mayor prioridad (M)'))
    ans = controller.req_6(control,M)
    return ans


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    origen = input('Ingrese el punto de origen con latitud y longitud: ')
    destino = input('Ingrese el destino con latitud y longitud: ')
    # TODO: Imprimir el resultado del requerimiento 1
    ans = controller.req_1(control,origen,destino)
    return ans


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print('\nLa cantidad total de aeropuertos es:', data[3])
            print('La cantidad de vuelos comerciales es:', data[0])
            print('La cantidad de vuelos de carga es:', data[1])
            print('La cantidad total de vuelos militares es de:', data[2])
            print('Por lo que la cantidad total de vuelos es de:', (data[0]+data[1]+data[2]))
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
            
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
