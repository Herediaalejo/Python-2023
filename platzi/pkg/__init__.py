#Archivo obligatorio en las version anteriores a la de Python 3.3

# Los paquetes deben tener siempre un archivo de nombre __init__.py (por lo general esta vacio, ya que así es compatible con programas python versiones anteriores a la 3.3), con esto le estamos indicado a python que esto se trata de un paquete y no de una carpeta.


print("Se inicio paquete")

URL = "platzi.com"

import pkg.mod_1, pkg.mod_2

#Un namespace es un sistema que tiene un nombre único para cada objeto en Python.

#Es posible habilitar un namespace a través del archivo __init__.py si los módulos de dicho paquete se importan en el mismo:

#Archivo __init__.py
#import pkg.mod_1