"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control):

    start_time = get_time()
    
    loadAirports(control['model'])
    total_vuelos, aeropuertos, militar, comercial, carga = loadVuelos(control['model'])
    
    end_time = get_time()   
    deltaTime = delta_time(start_time, end_time)
    print(deltaTime,"[ms]")

    return total_vuelos, aeropuertos, militar, comercial, carga



# Funciones de ordenamiento
def loadAirports(data_structs):
    booksfile_1 = cf.data_dir + str("airports-2022.csv")
    airportfile = csv.DictReader(open(booksfile_1, encoding="utf-8"), delimiter=";")
    
    for airport in airportfile:
        model.add_vertex(data_structs, airport)

        
def loadVuelos(catalog):
    booksfile_2 = cf.data_dir + str("flights-2022.csv")
    flightfile = csv.DictReader(open(booksfile_2, encoding="utf-8"), delimiter=";")
    total_vuelos = 0
    for flight in flightfile:
        total_vuelos +=1
        if flight['TIPO_VUELO']=='MILITAR':
            model.add_arcoMilitar(catalog,flight)
        
        elif flight['TIPO_VUELO']=='AVIACION_CARGA':
            model.add_arcoCarga(catalog,flight)
            
        elif flight['TIPO_VUELO']=='AVIACION_COMERCIAL':
            model.add_arcoComercial(catalog,flight)
            
        
    aeropuertos = model.totalVertex(catalog['disCarga'])
    militar, comercial, carga = model.crear_tablas(catalog)
    return total_vuelos, aeropuertos, militar, comercial, carga

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, origen, destino):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    datos = model.req_1(control['model'], model.me.getValue(model.mp.get(control['model']['coordenadas'],'KDAL')), (5.0296, -75.4647))
    end_time = get_time()
  
    print(delta_time(start_time, end_time),'ms')
  
    return datos


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    return model.req_3(control['model'])


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control,n):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    
    return model.req_6(control['model'],n)


def req_7(control, origen, destino):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start_time = get_time()
    datos = model.req_7(control['model'], model.me.getValue(model.mp.get(control['model']['coordenadas'],'KDAL')), (5.0296, -75.4647))
    end_time = get_time()
  
    print(delta_time(start_time, end_time),'ms')
  
    return datos



def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
