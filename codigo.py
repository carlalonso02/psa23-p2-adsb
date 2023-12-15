import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd

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

#grafica erronea, corregir!!!
def graph_messages_hour(data):
    '''Funcion para obtener el numero_message de mensajes recibidos por hora'''
    hours_graph = data.groupby(pd.Grouper(freq='H')).count()
    hours_graph.plot(kind='bar')
    plt.autoscale()
    plt.xlabel('Hora',fontfamily="monospace")
    plt.ylabel('Número de mensajes',fontfamily="monospace")
    plt.title('Número de mensajes recibidos por el sensor cada hora',fontfamily="monospace")
    plt.savefig("messages_hour.png",format="png")

def graph_aircrafts_message(data):
    '''Función que representa el numero de mensajes recibido por hora de distintas aeronaves'''
    IDs_graph = data["Aircraft ID"].groupby(data.index.hour).value_counts().unstack()
    IDs_graph.plot(kind='bar')
    plt.autoscale()
    plt.xlabel('Hora', fontfamily="monospace")
    plt.ylabel('Número de aviones',fontfamily="monospace")
    plt.title('Número de aviones distintos vistos por el sensor cada hora', fontfamily="monospace")
    plt.legend(title='Aircraft ID', loc='upper left',fontfamily="monospace") #ajustar escala bien
    plt.savefig("aircraft_message.png",format="png")

'''calcula y muestra (en subgráficas)= subplot:
•Número de mensajes cada 5 minutos = grafica, cambbiar frqe a minutos
tengo que crear un dataframe filtrado, y graficarlo cada 5 mins'''
def info_flight(data, FLIGHT):
    ''' Función que muestra el numero de mensajes recibidos por una aeronave concreta'''
    num = data["Aircraft ID"].value_counts()[FLIGHT]
    return print(f'Se reciben {num} mensajes de la aeronave cuya ID es {FLIGHT}')

def time_flight(data,Flight):
    data_filter = data[data["Aircraft ID"] == FLIGHT]
    IDs_graph = data_filter.groupby(pd.Grouper(freq = '5T')).value_counts() #5 es la frequecia 5 minutos
    IDs_graph.plot(kind = 'bar')
    plt.savefig("time_flight.png", format = "png")

def altitude_flight(data, FLIGHT):
    '''Función que muetsra visualemnte la variacion de la altura de vuelo de una determinada aeronave'''
    data_filter = data[data["Aircraft ID"] == FLIGHT]
    plt.plot(data_filter.index, data_filter[["Altitude"]], linestyle = '--', color = '#1ABC9C')
    plt.xlabel('Hora', fontfamily="monospace")
    plt.ylabel('Altitud', fontfamily="monospace")
    plt.title(f'Variacion de la altitud del vuelo {FLIGHT} con el tiempo', fontfamily="monospace")
    plt.savefig("altitude_flight.png", format = "png")

#mejorar formato, aparece el numero de veces que se repite cada string, intentar que no aparezca
def repetitive(data):
    '''Función que obtiene los 10 aviones mas captados por el sensor'''
    ID_times = data["Aircraft ID"].value_counts()
    ID_repetitive = ID_times.head(10)
    return print(f'Las 10 aernovaes uqe mas aparecen en el sensor son: {ID_repetitive}')
#Presentación 
print('\033[1m'+ 'Práctica 9'+ '\033[0m') #negrita
print("\033[4;37m"+"Ejercicio 2: Análisis de datos"+"\033[0m")#subrayado