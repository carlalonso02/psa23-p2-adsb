import pandas as pd

CSV_FILE = "aircraft_MSG3_short.csv"
CSV_COLUMNS=["Msg Type","Trans Type","Sesion ID","HEX","Aircraft ID","Flight ID","Gen Date","Gen Time","Log Date","Log Time","Callsign","Altitude","GND Speed","Track","Lat","Lon","Ver Rate","Squawk","Alert","Emergency","SPI","Is On Ground"]

def parse_csv():
    data = pd.read_csv(CSV_FILE, names = CSV_COLUMNS)
    data["Gen Time hour"] = pd.to_datetime(data["Gen Time"], format='%H:%M:%S.%f')
    data.set_index(["Gen Time hour"], inplace = True) #hace que los indices sean las horas a la que se recibio el mensaje
    return data

def check_nans(data):
    '''Funcion que dice que columnas estan vacias'''
    for label, col_data in data.items(): #para recorrer todas las columnas de un dataframe, usar con un bucle for
    #col_data.isnull() nos devuelve una lista con valore true o false
    #col_data.isna()
        if col_data.isnull().all(): #.any() o .all() any nos dice si hay alguno o no, no nos da la lista
            print(f'La columna {label} esta vacia') #con esto obtenemos que columnas estan completamente vacios por usar .all
            #data = data.drop(label, axis=1) #de esta forma se eliminan las columnas que estan vacias 
            #data.to_csv('aircraft_MSG3_short.csv', index = False) #se guarda el cambio


def main(data):
    print(data)
    return print(data.info())
