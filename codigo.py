import csv_parser as ps
import matplotlib as plt
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
#hay que generar una grafica de tiempo frente a numero de mensajes,


def ejemplo():
    data = ps.parse_csv()
    data['Gen Time datetime'] = pd.to_datetime(data["Gen Time"]) 
    data.groupby(pd.Grouper (key= "Gen Time datetime", freq = "H")).sum()
    
    return print(data['Gen Time datetime'])
ejemplo()
def grafica():
    data = ps.parse_csv()
    horas = data['Gen Time datetime']
    plt.plot(horas, )
    return plt.show()

#numero de mensajes es el numero de filas