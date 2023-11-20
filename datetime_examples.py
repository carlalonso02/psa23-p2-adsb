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

if __name__ == '__main__':
    main()