from funciones import checkNum

"""Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos."""

numeros = []
numero = ""
numDesv = 0

while True:
    numero = (input("Ingrese los números separados por un espacio: "))
    if len(numero)==0:
        continue
    else:
        break
       
numeros = numero.split()
for i in range(len(numeros)):
    numeros[i] = checkNum(numeros[i])

for num in numeros:
    numDesv += (num-(sum(numeros)/len(numeros)))**2

numDesv = numDesv / len(numeros)
numDesv = numDesv**0.5

dictCalculos = {
    "Números": numeros,
    "Suma": sum(numeros),
    "Promedio": sum(numeros)/len(numeros),
    "Numero mínimo": min(numeros),
    "Numero máximo": max(numeros),
    "Desviación estándar": numDesv
}

for clave,valor in dictCalculos.items():
    print(f"{clave} : {valor}")


