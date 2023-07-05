def suma(a,b):
    return a + b

resultado = suma(10,50)
print(resultado)

def find_volume(length:int=1, width:int=1, depth:int=1) -> tuple: # Solo especifico lo que debería tomar como argumento y devolver pero no cambia nada a nivel código
    return "El volumen es: ", length * width * depth, "cm3" # Por defecto devuelve una tupla con los valores

def find_volume(length:int=1, width:int=1, depth:int=1) -> list:
    return ["El volumen es: ", length * width * depth, "cm3"] # Devuelve una lista

def find_volume(length:int=1, width:int=1, depth:int=1) -> set: 
    return {"El volumen es: ", length * width * depth, "cm3"} # Devuelva un conjunto


result = find_volume(width=50)
print(type(result))

mensaje,volume,medida = find_volume(depth=100)

print(mensaje)
print(volume)
print(medida)