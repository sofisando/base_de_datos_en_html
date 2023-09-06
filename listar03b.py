import mysql.connector #libreria externa que vamos a usar de un tercero

conexion1=mysql.connector.connect(host="localhost",
                                   user="publico3", 
                                   passwd="Publiquito1.",
                                   database="prueba" ) #con esto estamos conectandocon la base de datos que tenemos
cursor1=conexion1.cursor() #se crea como un cursor
cursor1.execute("show tables")
for base in cursor1: #va mostrando todos los datos que recaudó cursor1 de la base de datos creo
    print(base)
conexion1.close() #esto como buena practica de programacion cerrar despues de usar
