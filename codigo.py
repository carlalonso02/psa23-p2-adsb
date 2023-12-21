import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd
from geopy import distance
import numpy as np
#Llamadas a Dataframe
data = ps.parse_csv()
FLIGHT = "E8044F"
def total_messages(data):
    '''Función para obtener el numero de mensajes totales, que sera el numero de filas del csv'''
    number_rows = data.shape[0]
    return print(f'Hay un total de {number_rows} mensajes recibidos')

def different_aircrafts(data):
    '''Función para saber cuantas aeronaves distintas sobrevolaron la zona, que es saber cuantos identificadores distitnos se tienen'''
    different_ids = data['Aircraft ID'].nunique()
    return print(f'Se han visto {different_ids} aviones distintos')

#arreglar indice eje x y quitar escala
def graph_messages_hour(data):
    '''Funcion para obtener el numero_message de mensajes recibidos por hora'''
    hours_graph = data.groupby(pd.Grouper(freq='H')).count()
    hours_graph.plot(y = 'HEX', kind='bar', color = '#AF7AC5')
    plt.autoscale()
    plt.xlabel('Hora',fontfamily="monospace")
    plt.ylabel('Número de mensajes',fontfamily="monospace")
    plt.title('Número de mensajes recibidos por el sensor cada hora',fontfamily="monospace")
    plt.savefig("messages_hour.png",format="png")
    plt.show()

def graph_aircrafts_message(data):
    '''Función que representa el numero de mensajes recibido por hora de distintas aeronaves'''
    IDs_graph = data["Aircraft ID"].groupby(data.index.hour).value_counts().unstack()
    IDs_graph.plot(kind='bar')
    plt.autoscale()
    plt.xlabel('Hora', fontfamily="monospace")
    plt.ylabel('Número de aviones',fontfamily="monospace")
    plt.title('Número de aviones distintos vistos por el sensor cada hora', fontfamily="monospace")
    plt.legend(title='Aircraft ID', loc='upper left') #ajustar escala bien
    plt.savefig("aircraft_message.png",format="png")
    plt.show()

def info_flight(data, FLIGHT):
    ''' Función que muestra el numero de mensajes recibidos por una aeronave concreta'''
    num = data["Aircraft ID"].value_counts()[FLIGHT]
    return print(f'Se reciben {num} mensajes de la aeronave cuya ID es {FLIGHT}')

def time_flight(data,Flight):
    '''Funcion que representa el número de mensajes cada 5 minutos'''
    data_filter = data[data["Aircraft ID"] == FLIGHT]
    IDs_graph = data_filter.groupby(pd.Grouper(freq = '5T')).count() #5 es la frequencia 5 minutos
    IDs_graph.plot(y = 'HEX', kind = 'bar', color = '#F5B041')
    plt.autoscale()
    plt.xlabel('Hora',fontfamily="monospace")
    plt.ylabel('Número de mensajes',fontfamily="monospace")
    plt.title('Número de mensajes recibidos cada 5 minutos',fontfamily="monospace")
    plt.savefig("time_flight.png", format = "png")
    plt.show()

def altitude_flight(data, FLIGHT):
    '''Función que muetsra visualemnte la variacion de la altura de vuelo de una determinada aeronave'''
    data_filter = data[data["Aircraft ID"] == FLIGHT]
    plt.plot(data_filter.index, data_filter[["Altitude"]], linestyle = '--', color = '#1ABC9C')
    plt.xlabel('Hora', fontfamily="monospace")
    plt.ylabel('Altitud', fontfamily="monospace")
    plt.title(f'Variacion de la altitud del vuelo {FLIGHT} con el tiempo', fontfamily="monospace")
    plt.savefig("altitude_flight.png", format = "png")
    plt.show()

#mejorar formato, aparece el numero de veces que se repite cada string, intentar que no aparezca
def repetitive(data):
    '''Función que obtiene los 10 aviones mas captados por el sensor'''
    ID_times = data["Aircraft ID"].value_counts()
    ID_repetitive = ID_times.head(10)
    return print(f'Las 10 aeronavaes que más aparecen en el sensor son:\n{ID_repetitive}')

'''Obtén los 10 aviones que durante más tiempo están en el rango del sensor.
Nótese que para identificar estos aviones, los mensajes sucesivos enviados
por los aviones no han de haberse enviado en un intervalo mayor de 30
segundos'''
def more_repetitive(data):
    '''Función que obtiene los 10 aviones que mas tiempo estan en el sensor'''
    num = data.groupby(pd.Grouper(freq = '30S')).count() #agrupacion cada 30 segundos, buscar los 10 aviones que ma se repiten? usar HEX

def calculate_distance(data):
    '''Función que calcula la distancia maxima y minima entre las coordenadas de los mensajes recibidos'''
    urjc_coord = (40.283205,-3.821476) 
    coord = tuple(zip(data['Lat'] ,data['Lon'])) #creo una tupla para junatr los datos de las columnas lat y long ,manteniendo el formato
    distances = [] #creo una lista para introducir las distancias
    for i in range(len(coord)-1):
        dist = distance.geodesic(urjc_coord, coord[i])
        distances.append(dist)
    max_distance = max(distances)
    min_distance = min(distances) 
    media_distance = np.mean(distances)   
    return print(f'El mensaje mas lejano que recibió está a {max_distance} ,el mas cercano a {min_distance} y la media es de {media_distance} ')
#Presentación 
print('\033[1m'+ 'Práctica 9'+ '\033[0m') #negrita
print("\033[4;37m"+"Ejercicio 2: Análisis de datos"+"\033[0m")#subrayado
#total_messages(data)
#different_aircrafts(data)
#graph_messages_hour(data)
#graph_aircrafts_message(data)
#info_flight(data,FLIGHT)
#time_flight(data, FLIGHT)
#altitude_flight(data,FLIGHT)
#repetitive(data)
#calculate_distance(data)