# Documentos a evaluar

# Funcionamiento codigo
Dividi el codigo en 3 archivos: 'csv_long.py', 'csv_short.py' y 'codigo.py' para obtener un codigo mas corto y facil de leer.

Los archivos 'csv_long.py' y 'csv_short.py' tienen las mismas funciones y estructura, pero solo cambia el archivo con el que trabajan. 'csv_short.py' llama al archivo 'aircraft_MSG3_short.csv' mientras que 'csv_long.py' llama a 'aircraft_MSG3.csv'. 

En los dos archivos se nombran las columnas y se tienen las siguientes funciones:
    - 'parse_csv()': funcion que lee el archivo y devuelve la información que contiene para trabajar con ella. Ademas para facilitar el funcionamiento del codigo, se estableciron como indice las horas a las que se emitieron los mensajes en formato DateTime ya que son valores unicos para cada mensaje. Para ellos se usa la expresion '.set_index'. 
    - 'check_nans()': esta funcion dice que columnas estan vacias, por lo que podre eliminarlas y asi trabajar con documentos menos pesados.
    - main(): proporciona informacion del csv con el que se esta trabajando, que tipos de datos se tienen en cada columna.
    


Estos dos archivos actuan como 'modulos' de python, puedo usar estas funciones en otros archivos sin volver a crearlas. Tan solo llamadolas.

En el archivo retante, 'codigo.py', estan las funciones con las que se obtienen los datos pedidos en el apartado de analisis de la practica 9. 
Para obtener el numero de mensajes totales, tan solo es necesario saber cuantas columnas forman el csv, con la funcion de pandas '.shape[0]' se obtiene este numero.
Para obtener el numero de aeronaves distintas de ls que se recibio mensaje, hay que fijarse en la columna que nos proporciona el identificador de la aeronave. 'Aircraft ID'. Y usando la funcion de pandas .nunique()' se obtiene el  numero de valores unicos de la columna en la que se aplica. Este numero es el numero de aeronaves cuyo mensaje capto la antena.

Para obtener el numero de mensajes recibido por hora, como lo que quiero es realizar una grafica de barras, necesito que le eje x sean las horas, y el eje y el numero de mensajes recibido en determinada hora, que seria el numero de filas que estan en un rango de tiempo.
Para realizar esto, agrupe por el DataFrame por horas usando '.groupby(pd.Grouper'H')' y con '.count()' cuento los valores que hay en cada hora, que en este caso son las filas. Y usando '.plot(kind='bar')' obtengo el grafico de barras con el numero de mensajes por hora. RESULTADO FEO

Para obtener el numero de aviones vistos por el sensor cada hora, quiero generar grafico de barras, en el eje x las distintas horas, y en el eje y, el numero de veces que aparece en ese lapso de tiempo las distintas ID. Para ello voy a trabajar con la columna "Aircraft ID", despues, agrupo los datos de esa columna por la hora del indice ',groupby(data.index.hour)'. Con '.value_counts()' cuento cuantas veces aparecen valores unicos en esa columna, que seria el numero de mensajes recibidos por distintas aeronaves. Para obtener la grafica de barras uso '.plot(kind='bar')' y ya tendria los datos pedidos en una imagen.