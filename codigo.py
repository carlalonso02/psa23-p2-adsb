import csv_parser as ps

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
#numeros de mensajes recibidos por sensor cada hora