
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
#sUBIDA DE DATOS
data = pl.parse_csv()
db = client['ADS-B']

# Selecciona la colección donde deseas insertar los datos
collection = db['Aircraft MSG3']

# Convierte el DataFrame de Pandas a formato de diccionario
data_dict = data.to_dict(orient='records')

# Inserta los datos en la colección
collection.insert_many(data_dict)

# Cierra la conexión
client.close()