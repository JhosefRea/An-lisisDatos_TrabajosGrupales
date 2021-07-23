# AnalisisDatos_TrabajosGrupales
# Ejercicio con MongoDBy CouchDB

Integrantes:
--------------------------------------------------
Johan Quinatoa
Quisaguano Bryan
Rea Jhosef
Antony Sanchez

Proceso:
-------------------------
1. Se debe crear una base de datos en MongoDB Atlas, dentro del cual se debe generar un enlace para conectarse desde la aplicacion de MongoDB compas. 


<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/7.png" alt="1"/>

2. Con la base de datos lista, se ha creado las colecciones con los nombres de los integrantes.

<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/1.png" alt="1"/>

3. Ahora a cada colección se debe agregar datos, los cuales han sido extraidos de Kaggle e importados a la base de datos en MongoDB.
 
<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/2.png" alt="2"/>

4. La base de datos queda de la siguiente manera:

<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/3.png" alt="3"/>

5.   Asi quedan las colecciones: <img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/6.png" alt="1"/>
6.   Se instala la liberia necesaria para establecer la conexión entre MongoDB y CouchDB
      <br> pip3 install pymongo[srv] </br>
8.   Escribimos el codigo de python para enlazar las dos bases de datos
<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/4.png" alt="1"/>
<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/8.png" alt="1"/>
8.  Se confirma el enlace en CouchDB
<img src="https://github.com/JhosefRea/An-lisisDatos_TrabajosGrupales/blob/Ejercicio_MongoDB_CouchDB/Img/5.png" alt="1"/>

![Captura de Pantalla 2021-07-22 a la(s) 20 19 09](https://user-images.githubusercontent.com/66568293/126727413-fedc8b05-b3ad-4532-b616-ce0c32eb4c6f.png)


