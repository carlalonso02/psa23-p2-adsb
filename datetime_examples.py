import pandas as pd
import csv_parser as ps

def main():
    data= ps.parse_csv() 
    print(data.info())

    cols_filtered = ["Log Date","Log Time","Altitude","Lat","Lon"]
    dt = data[cols_filtered]
    print(dt)
    print(dt.info())
    dt['Log datetime'] = pd.to_datetime(dt['Log Date']+ ' '+ dt['Log Time'])
    print(dt)
    print(dt.info())
    #extraer tiempo mayores a 4 seg en x columna
    data_4s = dt[dt['Log datetime'].dt.second > 4] #es como un filtro en la columna long time busco en que filas el tiempo es mayor que 4 sec
    #hay .hour y mas cosas, indagar
    print(data_4s)
    timestamp_fist = dt['Log datetime'].iloc[0] #primer elemto columna
    timestamp_last = dt['Log datetime'].iloc[-1] #ultimo elemento columna
    print(f"First timestap: {timestamp_fist}")
    print(f'Last timestap {timestamp_last}')

    elapsed_time = timestamp_last - timestamp_fist
    print(elapsed_time)
    print(elapsed_time.total_seconds()) #

if __name__ == '__main__':
    main()