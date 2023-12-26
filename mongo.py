
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

data = pl.parse_csv()
#Filtrado datos mongo
def filt_data(data):
    key = "AA"
    filt = data[data["Aircraft ID"].str.contains(key, case = False)]
    return filt
def intro_pandas(data):
    #tenemos que crear una coleccion y guardarla en una coleccion
    db_adsb = client ["Aircraft_MSG3"]
    col_adsb = db_adsb["Aircraft ID"] #creo la coleccion
    aircrafts_aa = filt_data(data)
    aircraft_ID = aircrafts_aa.to_dict(orient = 'records')  #convierto el filtrado anterior en una lista
    col_adsb.insert_many(aircraft_ID) #subo la lista
intro_pandas(data)