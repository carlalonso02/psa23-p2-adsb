import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd

#Llamdas a Dataframe
data = pl.parse_csv()

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
def graph_messages_hour(data):
    '''Funcion para obtener el numero de mensajes recibidos por hora'''
    
    hours_graph = data.groupby(pd.Grouper(freq='H')).count()
    hours_graph.plot
    plt.savefig("prueba.png",format="png")

#Número de aviones distintos vistos por el sensor cada hora (grafica)
#lo que me dice si tengo un avion igual a otro o no es el 'Aircraft ID', tengo que agrupar los mismso valores de esa columna y sumarlos, y relacioanrlos con que hora estaba o algo asi
#nunique() el numero de esos valores unicos

#Presentación 
total_messages(data)
different_aircrafts(data)
graph_messages_hour(data)