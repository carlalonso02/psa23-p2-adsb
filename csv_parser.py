#aqui estara todo el codigo relacionado con la lectura de los datos
#guardamos funciones para llamr desde otro archivo
#como esta aqui podemos eliminar las funciones en otros archivos
import pandas as pd

CSV_FILE = "aircraft_MSG3_short.csv"
CSV_COLUMNS=["Msg Type","Trans Type","Sesion ID","Aircraft ID","HEX","Flight ID","Gen Date","Gen Time","Log Date","Log Time","Callsign","Altitude","GND Speed","Track","Lat","Lon","Ver Rate","Squawk","Alert","Emergency","SPI","Is On Ground"]

def parse_csv():
    data = pd.read_csv(CSV_FILE, names = CSV_COLUMNS)
    return data

def check_nans(data):
    '''funcion que dice que columnas son null'''
    for label, col_data in data.items(): #para recorrer todas las columnas de un dataframe, usar con un bucle for
    #col_data.isnull() nos devuelve una lista con valore true o false
    #col_data.isna()
        if col_data.isnull().all(): #.any() o .all() any nos mdice si hay alguno o no, no nos da la lista
            print(f'La columna {label} esta vacia') #con esto obtenemos que columnas estan completamente vacios por usar .all

def main():
    data=parse_csv()
    print(data)
    print(data.info())

    check_nans(data)