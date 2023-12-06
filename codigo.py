import csv_short as ps
import csv_long as pl
import matplotlib.pyplot as plt
import pandas as pd

def total_messages():
    '''Función para obtener el numero de mensajes totales, que sera el numero de filas del csv'''
    data = ps.parse_csv()
    number_rows = data.shape[0]
    return print(f'Hay un total de {number_rows} mensajes recibidos')
total_messages()

#unique() devulve los valores unicos de una columna
#nunique() el numero de esos valores unicos
def different_aircrafts():
    '''Función para saber cuantas aeronaves distintas sobrevolaron la zona, que es saber cuantos identificadores distitnos se tienen'''
    data = ps.parse_csv()
    different_ids = data['Aircraft ID'].nunique()
    return print(f'Se han visto {different_ids} aviones distintos')
different_aircrafts()

#Número de mensajes recibidos por el sensor cada hora 
#hacer con archivo pequeño y luego probar grande
def graph_messages_hour():
    '''Funcion para obtener el numero de mensajes recibidos por hora'''
    data =ps.hour_messages() #aqui data tiene una columna nueva, "Hour", donde esta las horas en un formato adecuado
    data["Hour"] = data['Hour'].astype(str)
    hours_graph = data["Hour"].value_counts().sort_index()
    #da una grafica pero fea, buscar error y corregir
    plt.bar(hours_graph.index, hours_graph.values, color='#1ABC9C')
    plt.title('Número de mensajes por hora')
    plt.xlabel('Hora')
    plt.ylabel('Número de mensajes')
    return plt.show()
graph_messages_hour()

#Número de aviones distintos vistos por el sensor cada hora (grafica)
#lo que me dice si tengo un avion igual a otro o no es el 'Aircraft ID', tengo que agrupar los mismso valores de esa columna y sumarlos, y relacioanrlos con que hora estaba o algo asi
#nunique() el numero de esos valores unicos
def graph_aircraft_hour():
    '''Funcion para obtener la grafica que muestra el número de aviones distintos vistos por el sensor cada hora '''
    data =ps.hour_messages() #aqui data tiene una columna nueva, "Hour", donde esta las horas en un formato adecuado
    hours_graph = data.groupby("Hour").value_counts().sort_index()


