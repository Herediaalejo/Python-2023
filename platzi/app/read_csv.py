import csv

def read_csv(path):
    with open(path, "r") as csvfile: # Abro el archivo con permiso solo de lectura
        reader = csv.reader(csvfile, delimiter=",") # La función csv.reader() recibe dos valores, el primero es el archivo csv y el segundo es el caracter que divide cada dato en el archivo, en este caso es la coma (,), algunos archivos csv estan separados por punto y coma (;)
        #La función reader devuelve el archivo como un iterador
        header = next(reader) # Reader al ser un iterador puedo aplicarle la función next para obtener la primer iteracion, en este caso los headers de las columnas
        data = []
        for row in reader:
            iterable = zip(header, row) # Une el header y el row y los convierte en un array de tuplas
            country_dict = {key: value for key, value in iterable} # Creo un diccionario con clave (el header) y valor(el valor en esa columna)
            data.append(country_dict) #Agrego cada diccionario a una lista
        return data # Devuelvo la lista de diccionarios
    
if __name__ == "__main__":
    data = read_csv("./app/data.csv") # Ejecuto mi función y lo guardo en la variable data
    print(data) # Imprimo el primer diccionario obtenido del csv

 