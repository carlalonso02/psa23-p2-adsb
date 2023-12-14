
#usar comando insert_one para añadir un elemento, para añadir varios insert_many, para que furrule bien ponerle lo de records, para mantener el formato adecuado
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv_long as pl

uri = "mongodb+srv://calonsoa2020:12345@ads-b.qipmeja.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

'''Lee el fichero CSV e importa todos los datos a una base de datos MongoDB.
Crea una colección donde vayas introduciendo los datos del CSV para todos los
vuelos que tengan “AA” en el código. Haz una captura de pantalla de Atlas
donde se vea el número total de registro. Esa captura de pantalla la has de subir
al repositorio con el nombre captura-atlas.png.
2'''
data = pl.parse_csv()
def intro_pnadas(data):
    #tenemos que crear una coleccion y guardarla en una cleccion
    db_adsb = client ["Aircraft_MSG3"]
    col_adsb = db_adsb["Aircraft ID"] #creo la coleccion

    #pasamos los datos en formato de diccionario, las claves son las columnas del diccionario
    print(data.head())
    colpassengers.insert_many(data.to_dict('records'))
'''
def insert_algo():
    #introduce an item from the csv into the DB hay que hacer un filtrado de datos, buscar los vuelos con lo que pide el eneuciado para subrilo
    adsb_row_data = data.iloc[0].to_dict() #automaticamente convierte los datos del dataframe en diccionario
    print(f"Data:\n{adsb_row_data}")
    #insert data
    result = db.insert_one(adsb_row_data)
    print(f"results: {result}")

def delete_algo():
    #create the query to remove the item
    adsb_row_data = data.iloc[0].to_dict[0]
    print(f"data:\n {adsb_row_data}")
    #we just need to query de datetime
    #query = [hex: adsb_row_data[hex]]
    query = {"log datetime:" adsb_row_data["lod datetime"]}
    print(f"delete query:\n {query}")
    #delete data
    result = db.delete_one(query)'''