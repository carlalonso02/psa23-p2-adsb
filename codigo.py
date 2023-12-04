import csv_parser as ps
import matplotlib.pyplot as plt
import pandas as pd
#crear funcion que elimine columnas inecessaris(que tenga todo nulls por ejemplo)
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
def hour_messages():
    '''Funcion para obtener el numero de mensajes recibidos por hora'''
    data = ps.parse_csv()
    data["Gen Time hour"] = pd.to_datetime(data["Gen Time"], format='%H:%M:%S.%f')
    hour = data.groupby("Gen Time hour").sum().reset_index()
    return print(hour["Gen Time hour"])
hour_messages()

#Número de aviones distintos vistos por el sensor cada hora (grafica)
#lo que me dice si tengo un avion igual a otro o no es el 'Aircraft ID', tengo que agrupar los mismso valores de esa columna y sumarlos, y relacioanrlos con que hora estaba o algo asi
def hour_aircraft():
    '''Funcion para obtener el numerp...'''
    data = ps.parse_csv()
    data["Gen Time hour"] = pd.to_datetime(data["Gen Time"], format='%H:%M:%S.%f')
    hour = data.groupby("Gen Time hour").sum().reset_index()
    return hour
