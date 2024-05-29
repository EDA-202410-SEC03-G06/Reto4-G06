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
            'disColombia': None,
            'ciudadesCol': None,
            'timeMilitar': None,
            'coordenadas': None,
            'coordenadas_inverso': None,
            'aeropuertosData': None,
            'vuelosComercial': None,
            'vuelosCarga': None,
            'vuelosMilitar':None
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
    
    catalog['disColombia'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000
                                              )
    catalog['ciudadesCol'] = lt.newList('ARRAY_LIST')
    catalog['coordenadas'] = mp.newMap()
    
    catalog['coordenadas_inverso'] = mp.newMap()
    
    catalog['aeropuertosData'] = mp.newMap()
    
    catalog['vuelosComercial'] = mp.newMap()
    catalog['vuelosCarga'] = mp.newMap()
    catalog['vuelosMilitar'] = mp.newMap()
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
    #Agregar a disColombia
    if airport['PAIS']=='Colombia':
        gr.insertVertex(catalog['disColombia'], airport['ICAO'])
        ispresent = lt.isPresent(catalog['ciudadesCol'],airport['ICAO'])
        if not ispresent:
            lt.addLast(catalog['ciudadesCol'],airport['ICAO'])
        
    #Agregar un mapa con las coordenadas de cada aeropuerto
    latitud = float(airport['LATITUD'].replace(',','.'))
    longitud = float(airport['LONGITUD'].replace(',','.'))
    aero = (latitud, longitud)
    
    mp.put(catalog['coordenadas'], airport['ICAO'], aero)
    
    mp.put(catalog['coordenadas_inverso'], aero, airport['ICAO'])
    
    airport['cantidad_Comercial']= 0
    airport['cantidad_Militar'] = 0
    airport['cantidad_Carga']= 0
    airport['cantidad_Colombia']= 0

    mp.put(catalog['aeropuertosData'],airport['ICAO'], airport)
    
        
def add_arcoComercial(catalog,flight):
    origen = flight['ORIGEN']
    destino = flight['DESTINO']
    
    parejaOrigen = mp.get(catalog['aeropuertosData'],origen)
    infoOrigen = me.getValue(parejaOrigen)
    infoOrigen['cantidad_Comercial'] +=1
    
    
    parejaDestino = mp.get(catalog['aeropuertosData'],destino)
    valor_destino = me.getValue(parejaDestino)
    valor_destino['cantidad_Comercial'] +=1
    
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    
    origenISpresent = lt.isPresent(catalog['ciudadesCol'],flight['ORIGEN'])
    destinoISpresent = lt.isPresent(catalog['ciudadesCol'],flight['DESTINO']) 
    if origenISpresent!=0 and destinoISpresent!=0:
        infoOrigen['cantidad_Colombia'] +=1
        valor_destino['cantidad_Colombia'] +=1
        gr.addEdge(catalog['disColombia'],flight['ORIGEN'],flight['DESTINO'], distancia)
    
    llave= (flight['ORIGEN'],flight['DESTINO'])
    mp.put(catalog['vuelosComercial'], llave, flight)
    
    gr.addEdge(catalog['disComercial'],flight['ORIGEN'],flight['DESTINO'], distancia)
    gr.addEdge(catalog['timeComercial'],flight['ORIGEN'],flight['DESTINO'],int(flight['TIEMPO_VUELO']))
    
def add_arcoCarga(catalog,flight):
    origen = flight['ORIGEN']
    destino = flight['DESTINO']
    
    parejaOrigen = mp.get(catalog['aeropuertosData'],origen)
    infoOrigen = me.getValue(parejaOrigen)
    infoOrigen['cantidad_Carga'] +=1
    
    parejaDestino = mp.get(catalog['aeropuertosData'],destino)
    valor_destino = me.getValue(parejaDestino)
    valor_destino['cantidad_Carga'] +=1
    
    llave= (flight['ORIGEN'],flight['DESTINO'])
    mp.put(catalog['vuelosCarga'], llave, flight)
    
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    gr.addEdge(catalog['disCarga'],flight['ORIGEN'],flight['DESTINO'],distancia)
    gr.addEdge(catalog['timeCarga'],flight['ORIGEN'],flight['DESTINO'],int(flight['TIEMPO_VUELO']))
    
# Funciones de consulta
def add_arcoMilitar(catalog,flight):
    origen = flight['ORIGEN']
    destino = flight['DESTINO']
    
    parejaOrigen = mp.get(catalog['aeropuertosData'],origen)
    infoOrigen = me.getValue(parejaOrigen)
    infoOrigen['cantidad_Militar'] +=1
    
    parejaDestino = mp.get(catalog['aeropuertosData'],destino)
    valor_destino = me.getValue(parejaDestino)
    valor_destino['cantidad_Militar'] +=1
    
    llave= (flight['ORIGEN'],flight['DESTINO'])
    mp.put(catalog['vuelosMilitar'], llave, flight)
    
    origen = me.getValue(mp.get(catalog['coordenadas'], flight['ORIGEN']))
    destino = me.getValue(mp.get(catalog['coordenadas'], flight['DESTINO']))
    distancia = haversine(origen, destino)
    gr.addEdge(catalog['disMilitar'],flight['ORIGEN'],flight['DESTINO'],distancia)
    gr.addEdge(catalog['timeMilitar'],flight['ORIGEN'],flight['DESTINO'],int(flight['TIEMPO_VUELO']))

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

def datosTablas(data_structs, tipo_Avion):
    if tipo_Avion =='militar':
        merg.sort(data_structs, sort_criteria_tabla_militar)
    elif tipo_Avion =='comercial':
        merg.sort(data_structs, sort_criteria_tabla_comercial)
    else:
        merg.sort(data_structs, sort_criteria_tabla_carga)
    
    primeros = lt.subList(data_structs,1,5)
    ultimos = lt.lastElement(data_structs)
    prim_ult = []
    for valor in lt.iterator(primeros):
        prim_ult.append(valor)
    prim_ult.append(ultimos)
    return prim_ult

def crear_tablas(catalog):
    militar = datosTablas(mp.valueSet(catalog['aeropuertosData']), 'militar')
    comercial = datosTablas(mp.valueSet(catalog['aeropuertosData']), 'comercial')
    carga = datosTablas(mp.valueSet(catalog['aeropuertosData']), 'carga')
    
    return militar, comercial, carga
    

def encontrar_aeropuerto(catalog, origen):
    aeropuertos = mp.keySet(catalog['coordenadas_inverso'])
    cerca_origen = float('inf')
    aero_cerca = None
    for aeropuerto in lt.iterator(aeropuertos):
        distancia_origen = haversine(origen, aeropuerto)
        if distancia_origen < cerca_origen:
            cerca_origen = distancia_origen
            aero_cerca = aeropuerto
    
    return cerca_origen, aero_cerca
    
        
    
        
    
def req_1(catalog, origen, destino):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    dist_origen, aero_origen = encontrar_aeropuerto(catalog, origen)
    dist_destino, aero_destino = encontrar_aeropuerto(catalog, destino)
    vertOrigen = me.getValue(mp.get(catalog['coordenadas_inverso'], aero_origen))
    vertDestino = me.getValue(mp.get(catalog['coordenadas_inverso'], aero_destino))
    
    if dist_origen <=30 and dist_destino <= 30:
        caminos = bfs.BreathFirstSearch(catalog['disComercial'], vertOrigen)
  
        camino = bfs.pathTo(caminos, vertDestino)
        distancia = 0
        aeropuertos = lt.newList()
        
        totalAeropuertos = 0
  
    
        for vuelo in lt.iterator(camino):
            if totalAeropuertos != 0:
                arcoTiempo = gr.getEdge(catalog['timeComercial'],vuelo, verticeA)
                arcoDistancia = gr.getEdge(catalog['disComercial'],vuelo, verticeA)
                aeropuertoA['TIEMPO'] = arcoTiempo['weight']
                distancia += arcoDistancia['weight']
                
        
            totalAeropuertos+=1
            aeropuertoA = me.getValue(mp.get(catalog['aeropuertosData'],vuelo))
            aeropuertoA['TIEMPO'] = 0
            lt.addLast(aeropuertos, aeropuertoA)
            verticeA = vuelo
        aeropuertosTabla = []
        for aeropuerto in lt.iterator(aeropuertos):
            info = {'ICAO': aeropuerto['ICAO'], 'NOMBRE': aeropuerto['NOMBRE'], 'CIUDAD': aeropuerto['CIUDAD'], 'PAIS': aeropuerto['PAIS'], 'TIEMPO': aeropuerto['TIEMPO']}
            aeropuertosTabla.insert(0, info)
        return distancia, totalAeropuertos, aeropuertosTabla
    else:
        distancia = 0
        totalAeropuertos = 0
        aeropuertosTabla=[]
        vertOrigen = me.getValue(mp.get(catalog['aeropuertosData'], vertOrigen))
        vertDestino = me.getValue(mp.get(catalog['aeropuertosData'], vertDestino))
        infoA={'AEROPUERTO': 'ORIGEN','ICAO': vertOrigen['ICAO'], 'NOMBRE': vertOrigen['NOMBRE'], 'CIUDAD': vertOrigen['CIUDAD'], 'PAIS': vertOrigen['PAIS'], 'DISTANCIA': dist_origen}
        aeropuertosTabla.append(infoA)
        infoB = {'AEROPUERTO':'DESTINO','ICAO': vertDestino['ICAO'], 'NOMBRE': vertDestino['NOMBRE'], 'CIUDAD': vertDestino['CIUDAD'], 'PAIS': vertDestino['PAIS'], 'DISTANCIA': dist_destino}
        aeropuertosTabla.append(infoB)
        return distancia, totalAeropuertos, aeropuertosTabla

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
    disComercial = data_structs['disComercial']
    listaConcurrencia = mp.valueSet(data_structs['aeropuertosData'])
    merg.sort(listaConcurrencia,sort_criteria_tabla_comercial)
    mayorConcurrencia = lt.firstElement(listaConcurrencia)
    arbol = prim.PrimMST(disComercial,mayorConcurrencia['ICAO'])
    prim.edgesMST(disComercial,arbol)
    arcos = arbol['mst']
    grafo = gr.newGraph()
    
    
    for vuelo in lt.iterator(arcos):
        gr.insertVertex(grafo,vuelo['vertexA'])
        ispresent = gr.containsVertex(grafo,vuelo['vertexB'])
        if not ispresent:
            gr.insertVertex(grafo,vuelo['vertexB'])
        gr.addEdge(grafo,vuelo['vertexA'],vuelo['vertexB'],vuelo['weight'])   
    
    Dijktra = djk.Dijkstra(grafo,mayorConcurrencia['ICAO'])
    disMayor = 0
    aeroMayor =''
    for aeropuerto in lt.iterator(gr.vertices(grafo)):
        disAeropuerto = djk.distTo(Dijktra,aeropuerto)
        if disAeropuerto>disMayor:
            disMayor = disAeropuerto
            aeroMayor = aeropuerto
            
    ruta = djk.pathTo(Dijktra,aeroMayor)
#usar prim.weight para suma de la distancia de los trayectos
    disTotal = prim.weightMST(grafo,arbol)
    vuelosRuta =[]
    aeropRuta = []
    for camino in lt.iterator(ruta):
            verticeA = camino['vertexA']
            verticeB = camino['vertexB']
            viaje = (verticeA,verticeB)
            aeropRuta.insert(0,verticeA)
            if verticeB not in aeropRuta:
                aeropRuta.insert(0,verticeB)
            vuelosRuta.insert(0,viaje)
    trayecto = ordenar_vuelos(data_structs,vuelosRuta,'Comercial')
    mayorConcurrencia = [{'ICAO':mayorConcurrencia['ICAO'],'NOMBRE':mayorConcurrencia['NOMBRE'],'CIUDAD':mayorConcurrencia['CIUDAD'],
                             'PAIS':mayorConcurrencia['PAIS'],'CONCURRENCIA_NACIONAL':mayorConcurrencia['cantidad_Colombia'],
                             'CONCURRENCIA_TOTAL':mayorConcurrencia['cantidad_Comercial']}]
    return mayorConcurrencia, disTotal, data_size(grafo)-1, trayecto


def req_4(catalog):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    listaAeropuertos = mp.valueSet(catalog['aeropuertosData'])

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs, n):
    
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    disComercial = data_structs['disColombia']
    listaConcurrencia = mp.valueSet(data_structs['aeropuertosData'])
    merg.sort(listaConcurrencia,sort_criteria_tabla_comercial)
    mayorConcurrencia = lt.firstElement(listaConcurrencia)
    count = 1
    rutas = lt.newList('ARRAY_LIST')
    
                
    while count<(n+1):
        count+=1
        destino = lt.getElement(listaConcurrencia,count)
        Dijktra = djk.Dijkstra(disComercial,mayorConcurrencia['ICAO'])
        distancia = djk.distTo(Dijktra,destino['ICAO'])
        ruta = djk.pathTo(Dijktra,destino['ICAO'])
        aeropuertos =[]
        vuelos = []
        
        for camino in lt.iterator(ruta):
            verticeA = camino['vertexA']
            verticeB = camino['vertexB']
            viaje = verticeA+'-'+verticeB
            aeropuertos.insert(0,verticeA)
            if verticeB not in aeropuertos:
                aeropuertos.insert(0,verticeB)
            vuelos.insert(0,viaje)

        lt.addLast(rutas,{'Total Aeropuertos:':len(aeropuertos),'Aeropuertos:':aeropuertos,'Vuelos':vuelos,'Distancia':round(distancia,5)})
        
    mayorConcurrencia = [{'ICAO':mayorConcurrencia['ICAO'],'NOMBRE':mayorConcurrencia['NOMBRE'],'CIUDAD':mayorConcurrencia['CIUDAD'],
                             'PAIS':mayorConcurrencia['PAIS'],'CONCURRENCIA_NACIONAL':mayorConcurrencia['cantidad_Colombia'],
                             'CONCURRENCIA_TOTAL':mayorConcurrencia['cantidad_Comercial']}]

    return mayorConcurrencia, rutas


def req_7(catalog, origen, destino):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    dist_origen, aero_origen = encontrar_aeropuerto(catalog, origen)
    dist_destino, aero_destino = encontrar_aeropuerto(catalog, destino)
    vertOrigen = me.getValue(mp.get(catalog['coordenadas_inverso'], aero_origen))
    vertDestino = me.getValue(mp.get(catalog['coordenadas_inverso'], aero_destino))
    
    if dist_origen <=30 and dist_destino <= 30:
        caminos = djk.Dijkstra(catalog['timeComercial'], vertOrigen)
    
        camino = djk.pathTo(caminos, vertDestino)
        tiempo = djk.distTo(caminos, vertDestino)
  
        aeropuertos = lt.newList()
  
        totalAeropuertos = 1
  
        distancia = 0
        for vuelo in lt.iterator(camino):
            verticeA = vuelo['vertexA']
            verticeB = vuelo['vertexB']
            arcoDistancia = gr.getEdge(catalog['disComercial'],verticeA, verticeB)
            distancia += arcoDistancia['weight']
            aeropuertoA = me.getValue(mp.get(catalog['aeropuertosData'],verticeA))
            aeropuertoA['DISTANCIA'] = dist_origen
            aeropuertoA['TIEMPO'] = 0
            aeropuertoB = me.getValue(mp.get(catalog['aeropuertosData'],verticeB))
            aeropuertoB['DISTANCIA'] = arcoDistancia['weight']
            aeropuertoB['TIEMPO']= vuelo['weight']
       
            if totalAeropuertos == 1:
            
                lt.addLast(aeropuertos, aeropuertoB)
            
            lt.addLast(aeropuertos, aeropuertoA)
            totalAeropuertos+=1
        
        aeropuertosTabla = []
        for aeropuerto in lt.iterator(aeropuertos):
            info = {'ICAO': aeropuerto['ICAO'], 'NOMBRE': aeropuerto['NOMBRE'], 'CIUDAD': aeropuerto['CIUDAD'], 'PAIS': aeropuerto['PAIS'], 'TIEMPO': aeropuerto['TIEMPO'], 'DISTANCIA': aeropuerto['DISTANCIA']}
            aeropuertosTabla.insert(0,info)
        return distancia, totalAeropuertos, aeropuertosTabla, tiempo
    else:
        distancia = 0
        totalAeropuertos = 0
        aeropuertosTabla=[]
        vertOrigen = me.getValue(mp.get(catalog['aeropuertosData'], vertOrigen))
        vertDestino = me.getValue(mp.get(catalog['aeropuertosData'], vertDestino))
        infoA={'AEROPUERTO': 'ORIGEN','ICAO': vertOrigen['ICAO'], 'NOMBRE': vertOrigen['NOMBRE'], 'CIUDAD': vertOrigen['CIUDAD'], 'PAIS': vertOrigen['PAIS'], 'DISTANCIA': dist_origen}
        aeropuertosTabla.append(infoA)
        infoB = {'AEROPUERTO':'DESTINO','ICAO': vertDestino['ICAO'], 'NOMBRE': vertDestino['NOMBRE'], 'CIUDAD': vertDestino['CIUDAD'], 'PAIS': vertDestino['PAIS'], 'DISTANCIA': dist_destino}
        aeropuertosTabla.append(infoB)
        return distancia, totalAeropuertos, aeropuertosTabla
    
    


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


def sort_criteria_tabla_militar(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    if data_1['cantidad_Militar']==data_2['cantidad_Militar']:
        return data_1['ICAO'] < data_2['ICAO']
    else:
        return data_1['cantidad_Militar']> data_2['cantidad_Militar']
    
def sort_criteria_tabla_comercial(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
  
    
    if data_1['cantidad_Comercial']==data_2['cantidad_Comercial']:
        return data_1['ICAO'] < data_2['ICAO']
    else:
        return data_1['cantidad_Comercial']> data_2['cantidad_Comercial']


def sort_criteria_tabla_carga(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    if data_1['cantidad_Carga']==data_2['cantidad_Carga']:
        return data_1['ICAO'] < data_2['ICAO']
    else:
        return data_1['cantidad_Carga']> data_2['cantidad_Carga']
    
def sort_criteria_tabla_Colombia(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
  
    
    if data_1['cantidad_Colombia']==data_2['cantidad_Colombia']:
        return data_1['ICAO'] < data_2['ICAO']
    else:
        return data_1['cantidad_Colombia']> data_2['cantidad_Colombia']


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def data_size(grafo):
    lista = gr.vertices(grafo)
    return lt.size(lista)

def cercania(aeropuertos,ubicacion):
    pass

def ordenar_vuelos(catalog,flights,tipo):
    distancia = str('dis'+tipo)
    vuelos = str('vuelos'+tipo)
    vuelos_index = catalog[vuelos]
    info = []
    for vuelo in flights:
        datos = me.getValue(mp.get(vuelos_index,vuelo))
        info.append({'ICAO':vuelo,'ORIGEN_CIUDAD':datos['CIUDAD_ORIGEN'],'DESTINO_CIUDAD':datos['CIUDAD_DESTINO'],
                       'TIEMPO':datos['TIEMPO_VUELO'],'DISTANCIA':round(gr.getEdge(catalog[distancia],vuelo[0],vuelo[1])['weight'],5)})
    return info