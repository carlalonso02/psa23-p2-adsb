# Documentos a evaluar

# Funcionamiento codigo
Dividi el codigo en 3 archivos: 'csv_long.py', 'csv_short.py' y 'codigo.py' para obtener un codigo mas corto y facil de leer.

Los archivos 'csv_long.py' y 'csv_short.py' tienen las mismas funciones y estructura, pero solo cambia el archivo con el que trabajan. 'csv_short.py' llama al archivo 'aircraft_MSG3_short.csv' mientras que 'csv_long.py' llama a 'aircraft_MSG3.csv'. 

En los dos archivos se nombran las columnas y se tienen las siguientes funciones:
    - 'parse_csv()': funcion que lee el archivo y devuelve la información que contiene para trabajar con ella.
    - 'check_nans()': esta funcion dice que columnas estan vacias, por lo que podre eliminarlas y asi trabajar con documentos menos pesados.
    - main(): proporciona informacion del csv con el que se esta trabajando, que tipos de datos se tienen en cada columna.
    - hour_messages(): convierte los datos de la columna 'Gen Time' a un formato datetime y extraigo la hora.


Estos dos archivos actuan como 'modulos' de python, puedo usar estas funciones en otros archivos sin volver a crearlas. Tan solo llamadolas.

En el archivo retante, 'codigo.py', estan las funciones con las que se obtienen los datos pedidos en el apartado de analisis de la practica 9. 
Para obtener el numero de mensajes totales, tan solo es necesario saber cuantas columnas forman el csv, con la funcion de pandas '.shape[0]' se obtiene este numero.
Para obtener el numero de aeronaves distintas de ls que se recibio mensaje, hay que fijarse en la columna que nos proporciona el identificador de la aeronave. 'Aircraft ID'. Y usando la funcion de pandas .nunique()' se obtiene el  numero de valores unicos de la columna en la que se aplica. Este numero es el numero de aeronaves cuyo mensaje capto la antena.
Para obtener el numero de mensajes recibido por hora, primero llame a la funcion '.hour_message()', asi obtengo las horas a las que se recibieron los mensajes. Como lo que quiero es una grafica de barras con el numero de mensajes recibido para cada hora. Convierto la hora a una cadena, las agrupo por valores y las ordeno. 
Despues voy generando la grafica, como quiero representar el numero de mensajes por hora, esto es representar el numero de filas por hora. '.index' pone los valores que tiene 'hours_graph' como los valores del eje X, estos son las distintas horas a las que se recibieron mensajes. '.values' me da el numero de filas que estan en una determinada hora, lo que seria la altura de las barras de la grafica. 