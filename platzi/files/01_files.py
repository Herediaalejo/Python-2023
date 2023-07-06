file = open('files/text.txt') # Abre el archivo
#print(file.read()) # Lee todo el contenido del archivo, puede ser bastante pesado
#print(file.readline()) # Lee linea a linea
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)


file.close() # Cierra el archivo

with open("files/text.txt") as file: # Cierra el archivo de manera automática
    for line in file:
        print(line)