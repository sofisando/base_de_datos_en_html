import cgi
import mysql.connector #libreria externa que vamos a usar de un tercero

#header
print ("Content-Type: text/html")  
print() 

conexion1=mysql.connector.connect(host="localhost",
                                   user="publico3", 
                                   passwd="Publiquito1.",
                                   database="prueba" ) #con esto estamos conectandocon la base de datos que tenemos
cursor1=conexion1.cursor() #se crea como un cursor
cursor1.execute("select * from autor")

print("<html>")
print("<body>")
print("<h1>Lista de Autores</h1>")
print("<table border='1'>")
print("<tr><th>ID</th><th>Nombre</th><th>Edad</th></tr>")

  # Iteramos sobre los resultados de la consulta y los imprimimos en la tabla HTML
for fila in cursor1:
    print(f"<tr><td>{fila[0]}</td><td>{fila[1]}</td><td>{fila[2]}</td></tr>")

print("</table>")
print("</body>")
print("</html>")

conexion1.close() #esto como buena practica de programacion cerrar despues de usar
