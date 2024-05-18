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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import bellmanford as bf
from DISClib.Algorithms.Graphs import bfs
from DISClib.Algorithms.Graphs import dfs
from DISClib.Algorithms.Graphs import prim
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from haversine import haversine

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {
            'disComercial': None,
            'timeComercial': None,
            'disCarga': None,
            'timeCarga': None,
            'disMilitar':None,
            'timeMilitar': None,
            'coordenadas': None
    }
    
    catalog['disComercial'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000
                                              )
    
    catalog['timeComercial'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000)
    
    catalog['disCarga'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000)
 
    catalog['timeCarga'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000)
    
    catalog['disMilitar'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000)

    catalog['timeMilitar'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000
                                              )
    catalog['coordenadas'] = mp.newMap()
    
    catalog['coordenadas-inverso'] = mp.newMap()
    return catalog


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass
    


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass

def add_vertex(catalog, airport):
    #Agregar vertices a vuelos comerciales
    gr.insertVertex(catalog['disComercial'], airport['ICAO'])
    gr.insertVertex(catalog['timeComercial'], airport['ICAO'])
    #Agregar vertices a vuelos Militares
    gr.insertVertex(catalog['disMilitar'], airport['ICAO'])
    gr.insertVertex(catalog['timeMilitar'], airport['ICAO'])
    #Agregar vertices a vuelos de Carga
    gr.insertVertex(catalog['disCarga'], airport['ICAO'])
    gr.insertVertex(catalog['timeCarga'], airport['ICAO'])
    #Agregar un mapa con las coordenadas de cada aeropuerto
    latitud = float(airport['LATITUD'].replace(',','.'))
    longitud = float(airport['LONGITUD'].replace(',','.'))
    aero = (latitud, longitud)
    
    mp.put(catalog['coordenadas'], airport['ICAO'], aero)
    
    mp.put(catalog['coordenadas-inverso'], aero, airport['ICAO'])
        
def add_arcoComercial(catalog,flight):
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    gr.addEdge(catalog['disComercial'],flight['ORIGEN'],flight['DESTINO'], distancia)
    gr.addEdge(catalog['timeComercial'],flight['ORIGEN'],flight['DESTINO'],flight['TIEMPO_VUELO'])
    
def add_arcoCarga(catalog,flight):
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    gr.addEdge(catalog['disCarga'],flight['ORIGEN'],flight['DESTINO'],distancia)
    gr.addEdge(catalog['timeCarga'],flight['ORIGEN'],flight['DESTINO'],flight['TIEMPO_VUELO'])    
    
# Funciones de consulta
def add_arcoMilitar(catalog,flight):
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    gr.addEdge(catalog['disMilitar'],flight['ORIGEN'],flight['DESTINO'],distancia)
    gr.addEdge(catalog['timeMilitar'],flight['ORIGEN'],flight['DESTINO'],flight['TIEMPO_VUELO'])

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def totalVertex(data_structs):
    return gr.numVertices(data_structs)

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return gr.numEdges(data_structs)


def req_1(catalog, origen, destino):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    print(mp.contains(catalog['coordenadas_inverso'], origen))


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def data_size(grafo):
    lista = gr.vertices(grafo)
    return lt.size(lista)