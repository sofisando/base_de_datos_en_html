import mysql.connector #libreria externa que vamos a usar de un tercero

conexion1=mysql.connector.connect(host="localhost", user="publico3", passwd="Publiquito1.") #con esto estamos conectandocon la base de datos que tenemos
cursor1=conexion1.cursor() #se crea como un cursor
cursor1.execute("show databases")
for base in cursor1: #va mostrando todos los datos que recaudó cursor1 de la base de datos creo
    print(base)
conexion1.close() #esto como buena practica de programacion cerrar despues de usar



# mantenimiento de tabla mysql
# ABM de tabla mysql
# interfaz web (GUI CGI)
# controlador y modelo python