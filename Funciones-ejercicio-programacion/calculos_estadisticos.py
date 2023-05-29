"""Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos."""

def checkNum(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            try:
                num = float(num)
            except ValueError:
                print (f"El valor '{num}' no es un numero")
                num = input("Ingrese un numero valido: ")

numeros = []
numero = ""
cantidad = 0
suma = 0
promedio = 0
numMinimo = 0
numMaximo = 0
numDesv = 0

numero = (input("Ingrese los numeros separados por un espacio: "))
numeros = numero.split()
for i in range(len(numeros)):
    numeros[i] = checkNum(numeros[i])

for num in numeros:
    suma += num
    cantidad += 1

promedio = suma / cantidad
numMinimo = min(numeros)
numMaximo = max(numeros)

for num in numeros:
    numDesv += (num-promedio)**2

numDesv = numDesv / cantidad
numDesv = numDesv**0.5

print(
f"""
La lista de numeros es la siguiente:
{numeros}
Calculos estadisticos realizados con la lista:
Suma: {suma}
Promedio: {promedio}
Numero minimo: {numMinimo}
Numero maximo: {numMaximo}
Desviacion estandar: {numDesv}
""")


