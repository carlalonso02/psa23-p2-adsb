import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd

#Llamdas a Dataframe
data = ps.parse_csv()

def total_messages(data):
    '''Función para obtener el numero de mensajes totales, que sera el numero de filas del csv'''
    number_rows = data.shape[0]
    return print(f'Hay un total de {number_rows} mensajes recibidos')

#unique() devulve los valores unicos de una columna
#nunique() el numero de esos valores unicos
def different_aircrafts(data):
    '''Función para saber cuantas aeronaves distintas sobrevolaron la zona, que es saber cuantos identificadores distitnos se tienen'''
    different_ids = data['Aircraft ID'].nunique()
    return print(f'Se han visto {different_ids} aviones distintos')

#Número de mensajes recibidos por el sensor cada hora 
#me da una grafica, pero no la que quiero
def graph_messages_hour(data):
    '''Funcion para obtener el numero de mensajes recibidos por hora'''
    hours_graph = data.groupby(pd.Grouper(freq='H')).count()
    hours_graph.plot(kind='bar')
    plt.xlabel('Hora')
    plt.ylabel('Número de mensajes')
    plt.title('Número de mensajes recibidos por el sensor cada hora')
    plt.xticks(rotation=45)  # Para que las horas en el eje x queden legibles
    plt.savefig("messages_hour.png",format="png")

#Número de aviones distintos vistos por el sensor cada hora (grafica)
def graph_aircrafts_message(data):
    '''Función que representa el numero de mensajes recibido por hora de distintas aeronaves'''
    IDs_graph = data["Aircraft ID"].groupby(data.index.hour).value_counts().unstack()
    IDs_graph.plot(kind='bar')
    plt.xlabel('Hora')
    plt.ylabel('Número de aviones')
    plt.title('Número de aviones distintos vistos por el sensor cada hora')
    plt.legend(title='Aircraft ID', loc='upper left')
    plt.savefig("aircraft_message.png",format="png")

   

#Presentación 
