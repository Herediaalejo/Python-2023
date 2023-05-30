numeros = (1,3,5,7,9,12)
mayor = 0
menor = 0
for numero in numeros:
    if(numeros.index(numero)==0):
        mayor = numero
        menor = numero
    if(numero>mayor):
        mayor=numero
    if(numero<menor):
        menor=numero
print(f"El mayor es {mayor} y el menor es {menor}")
    