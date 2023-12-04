#para calcular distancias
from geopy import distance
urjc = (40.51907, -3.824176) #enunciado practica
aircraft = (40.51097, -4.01713) #lo sacamos del csv
dist = distance.geodesic(urjc, aircraft)
print(dist)
#head nos da las primeras l9injeas de un archivo , head -n x, nos dan las pirmeras x lineas del csv, si le añadimso > mete la salida de otro comando en otro archivo,
#head -n 500 < archivo_nuevo.csv