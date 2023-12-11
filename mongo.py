
#usar comando insert_one para añadir un elemento, para añadir varios insert_many, para que furrule bien ponerle lo de records, para mantener el formato adecuado
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://calonsoa2020:12345@ads-b.qipmeja.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



#tenemos que crear una coleccion y guardarla en una cleccion
db_adsb = client ['aircraft_MSG3']
col_adsb = db_adsb['aircrafts_ID'] #creo la coleccion
#pasamos los datos en formato de diccionario, las claves son las columnas del diccionario


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
    result = db.delete_one(query)