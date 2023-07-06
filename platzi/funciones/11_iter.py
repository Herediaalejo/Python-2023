for i in range (1, 11):
    print(i)

my_iter = iter(range(1, 11)) # Range es un tipo de dato iterable pero que por si mismo no muestra nada
# Para poder recorrer un range necesito convertirlo en un iterador con la palabra reservada iter()
# Ya siendo un objeto iterador puedo recorrerlo utilizando una función llamada next() la cual va a iterar uno a uno los elementos de mi objeto iterador

print(my_iter) # Es un objeto por lo tanto solo imprime su dirección en memoria

print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # 4, y asi hasta terminar los elementos del iterador, si quiero superar dichos elementos voy a tener un error

# Me sirve para optimizar memoria al intentar leer listas con muchos datos

# Otro ejemplo, iterar cadenas de texto

name = "Edward"
name = iter(name)
print(next(name)) # E
print(next(name)) # d
print(next(name)) # w
print(next(name)) # a

# Otro ejemplo, iterar tuplas

tup = ("manzana", "naranja", "pera")

tup = iter(tup)

print(next(tup)) # manzana
print(next(tup)) # naranja

# Otro ejemplo mas complejo, poniéndole un limite fijo
monedas = ['btc', 'eth', 'sol', 'xrp']
length = len(monedas)
token_iteration = iter(range(length))

count = 0
while count <= length-1:
  print(monedas[next(token_iteration)])
  count += 1


