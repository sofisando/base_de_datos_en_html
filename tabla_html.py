import cgi
import mysql.connector #libreria externa que vamos a usar de un tercero

#header
print ("Content.Type: text/html")  
print() 

conexion1=mysql.connector.connect(host="localhost",
                                   user="publico3", 
                                   passwd="Publiquito1.",
                                   database="prueba" ) #con esto estamos conectandocon la base de datos que tenemos
cursor1=conexion1.cursor() #se crea como un cursor
cursor1.execute("select * from autor")


print ("""<html>
<table>
  <tr>
    <th>id_autor</th>
    <th>nombre</th>
    <th>edad</th>
  </tr>
  <tr>
    </html>""")
for fila in cursor1:
  print("""<html>
        <td>
        </html>""")
  print(fila[0])
  print("""<html>
  </td>
    </tr>
  </table>   
  </html>""")


conexion1.close() #esto como buena practica de programacion cerrar despues de usar
