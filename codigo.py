import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd

#Llamadas a Dataframe
data = ps.parse_csv()
FLIGHT = "504E2E"
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
•Mensajes totales = numero de veces que aparece esta ID en la columna ["Aircraft ID"]
•Número de mensajes cada 5 minutos = grafica, cambbiar frqe a minutos
•Cómo varía la altitud = variacion columna ["Altitude"] en grafica por hora/aparicion'''

#Presentación 
print('\033[1m'+ 'Práctica 9'+ '\033[0m') #negrita
print("\033[4;37m"+"Ejercicio 2: Análisis de datos"+"\033[0m")#subrayado