# Examen
Realice el ejercicio B
# Documentos a evaluar
_Ejercicio 2_ : codigo.py, csv_long.py, csv_short.py 

_Ejercicio 3_ : mongo.py, captura-atlas.png
# Funcionamiento csv_short.py y csv_long.py
Dividi el codigo en 3 archivos: 'csv_long.py', 'csv_short.py' y 'codigo.py' para obtener un código mas corto y facil de leer.

Los archivos 'csv_long.py' y 'csv_short.py' tienen las mismas funciones y estructura, pero solo cambia el archivo con el que trabajan. 'csv_short.py' llama al archivo 'aircraft_MSG3_short.csv' mientras que 'csv_long.py' llama a 'aircraft_MSG3.csv'.

En los dos archivos se nombran las columnas con el tipo de información que transmiten esos campos en cada mensaje y se tienen las siguientes funciones:
    - 'parse_csv()': función que lee el archivo y devuelve la información que contiene para trabajar con ella. Además para facilitar el funcionamiento del código, se establecieron como índice las horas a las que se emitieron los mensajes en formato DateTime ya que son valores únicos para cada mensaje. Para ello se usa la expresión '.set_index'.
    - 'check_nans()': esta función dice que columnas están vacias, por lo que podre eliminarlas y asi trabajar con documentos menos pesados.
    - main(): proporciona información del csv con el que se esta trabajando, que tipos de datos se tienen en cada columna.
    
Estos dos archivos actuan como 'modulos' de python, puedo usar estas funciones en otros archivos sin volver a crearlas. Tan solo llamadolas.
# Funcionamiento codigo.py
En el archivo  'codigo.py', estan las funciones con las que se obtienen los datos pedidos en el ejercicio 2.
Para obtener el número de mensajes totales, tan solo es necesario saber cuantas columnas forman el csv, con la función de pandas '.shape[0]' se obtiene este número.

Para obtener el número de aeronaves distintas de las que se recibió mensaje, hay que fijarse en la columna que nos proporciona el identificador de la aeronave, 'Aircraft ID'. Y usando la función de pandas '.nunique()' se obtiene el  número de valores únicos de la columna en la que se aplica. Este número es el número de aeronaves cuyo mensaje captó el sensor.

Para obtener el número de mensajes recibidos por el sensor cada hora agrupe todos los mensajes recibido por horas usando '(pd.Grouper(freq='H'))', siendo 'H' lo que hace que la frecuencia de la agrupación sea en horas. Y se le añade '.count()' para que cuente el número de esos valores. Despues esta agrupación se puede representar en un gráfico de barras y obtener asi el número de mensajes recibido por cada hora, que es el número de filas del archivo por cada hora.

Para obtener el número de aviones visto por el sensor cada hora tambien agrupo la información pero de forma distinta. Para saber el número de aeronaves distintas hay que tener en cuenta el identificador de la aeronave, que va reflejado en la columna "Aircraft ID". Lo agrupe usando la funcion '.groupby(data.index.hour)' para juntar los distintos identificadores vistos en cada hora. Una vez esta agrupado se puede obtener usando '.plot' la gráfica de barras del número de veces que aparece el identificador de la aeronave cada hora.

Para obtener el número de mensajes del avión cuyo identificador es una constante FLIHT, se hace un filtrado en la columna "Aircraft ID" para obtener el número de veces que aparece ese avión en el sensor.

Para obtener el número de mensajes cada 5 minutos del avión cuyo identificador es una constante FLIHT, se realiza otra vez un filtrado para trabajar solamente con un dataframe que sean los mensajes recibidos del avión en cuestión. Despues se agrupa usando '(pd.Grouper(freq = '5T'))', esta vez '5T' se refiere a una frecuencia de 5 minutos. Usando '.plot' se vuelve a obtener la gráfica buscada.

Para obtener como varia la altitud del avión cuyo identificador es una constante FLIHT, se sigue usando el dataframe formado por los mensajes recibidos unicamente del avión FLIGHT. La altitud viene reflejada en la columna "Altitude", asi que tan solo hay que graficar esta columna frente a los índices, que es la hora a la que se recibio cada mensaje con su respectiva altitud.

Para obtener los 10 aviones de los que más mensajes recibe el sensor otra vez se trata con la columna "Aircraft ID", se agrupa el dataframe en función de los valores de esta usando '.value_counts()'; que obtiene el número de veces que aparece cada ID, y una vez se tiene con '.head(10)' se obtienen los 10 que más se repiten.

Para obtener los 10 aviones que más tiempo estan en el rango del sensor, se trata de buscar los aviones que durante mas tiempo de continuo, considerando continuo intervalos inferiores a 30 segundos, han estado en el rango del sensor. 
Agrupo el dataframe en intervalos de 30 segundos, de esa agrupación obtengo la cantidad de veces que aparece cada ID y lo guardo en una nueva columna. Estoy bsucando las aeronaves que se repiten en cada intervalo de manera continua, para ello busco el máximo intervalo continuo para cada avion y despues los ordeno de mayor a menos y los 10 primeros son los aviones buscados.

Para calcular la distancia máxima, mínima y la media de los mensajes que recibe el sensor hay que llamar previamente al modulo de python 'geopy' e importar 'distance', y e importar tambien 'numpy'. Para calcular la distancia se calcula desde las coordenadas de la URJC, que es donde se encuentra el sensor. En las columnas 'Lat','Lon' se encuentran por separado las latitudes y longitudes de la ubicación de los aviones en el momento en el que fueron captados por el sensor. Para poder realizar el calculo es necesario que esten juntos formando una coordenada, para ello creo una tupla con las dos columnas ya que mantiene el formato y asi se puede realizar el calculo de la distancia. La tupla tiene todas las coordenadas de los mensajes recibidos por el sensor, pero como algunos mensajes no tenian estos campos cubiertos, se realiza un filtrado previo. Usando '.dropna' que elimina las filas que tengan algún campo, ya sea de 'Lat' o de 'Lon', vacios. Con este dataframe se crea la tupla anteriormente descrita y creo una lista vacia para introducir las distancias. Mediante un bucle for, recorro toda la tupla calculando la distancia entre las coordenadas del sensor y las de cada elemento de la tupla, y las guarda en la lista vacia de distancias. Una vez estan calculadas, ya se pueden obtener la media, la mínima y la máxima usando respectivamente 'np.mean', 'min', 'max'.
# Funcionamiento mongo.py
Al ejecutar este código se inició sesión en mi cuenta de MongoDB, se creó una base de datos llamada "Aircraft_MSG3", y dentro de ellas una colección llamada "Aircraft ID" en la que guardé todos los datos de las aeronaves captadas por el sensor que tienen una 'AA' en su identificador.

Para ello primero inicié sesión en la base de datos con un código que proporciona MongoDB. Despues, para subir solamente las aeronaves especificadas se realizo un filtrado usando '.str.contains(key, case = False)' en la columna "Aircraft ID". Está linea crea un nuevo dataframe que solo contiene las aeronaves con una 'AA' en su identificador. 

Despues se crea la base de datos y la colección, y se añadió el dataframe nuevo pero con la información de los mensajes en formato diccionario y usando como claves los nombre de las columnas del dataframe, que es con la estructura de datos que trabaja Mongo, usando '.to_dict(orient = 'records')'.