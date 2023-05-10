import os

numeros = (1,2,3,4,5,6,7,8,9,10)
indice = 0
b = 0
continuar = ""

while(b==0):

    indice = input("Ingrese el indice del valor a buscar: ")


    while(True):
        try:
            indice = int(indice)
            break
        except ValueError:
            indice = input("Valor incorrecto. Ingrese un nuevo indice: ")

    if (indice>9 or indice<0):
        print("No existe valor para ese indice")
        continuar = input("Presione ENTER para continuar")
        os.system("cls")
    else:   
        print(f"El valor con ese indice es: {numeros[indice]}")
        b=1