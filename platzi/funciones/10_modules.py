import sys
print(sys.path) #Obtengo la dirección donde se esta ejecutando el archivo

import re #Expresiones regulares
text = "Mi número de teléfono es 2414124124, el código del país es 54, mi número de la suerte es 7"
result = re.findall("[0-9]+", text) #Obtengo todos los números
print(result)

import time
timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local) # La hora en formato entendible para personas
print(result)

import collections
numbers = [1,1,1,1,1,2,2,2,3,3,3,3,3,3,5,5,5,5,5,5,5]
counter = collections.Counter(numbers) #Obtengo una lista con la frecuencia que aparece cada numero
print(counter)