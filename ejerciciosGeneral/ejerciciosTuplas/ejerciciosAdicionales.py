import os

seguir = ""

""" Escribe un programa que solicite al usuario que ingrese una lista de números enteros.
El programa debe crear una tupla a partir de la lista y luego imprimir la tupla en orden
inverso. """


lista = list(input("Ingrese numeros a listar (sin separaciones): "))
lista.reverse()
lista = tuple(lista)
print(f"Tupla en orden inverso: {lista}")

seguir = input("Presione ENTER para continuar")
os.system("cls")


""" Escribe una función llamada intercambiar_tupla que acepte una tupla como parámetro
y devuelva una nueva tupla en la que el primer y el último elemento de la tupla
original se intercambian. Por ejemplo, si la tupla original es (1, 2, 3, 4), la función
debería devolver (4, 2, 3, 1). """

def intercambiar_tupla(tupla):
    tupla = list(tupla)
    primero = 0
    ultimo = 0
    for elemento in tupla:
        if tupla.index(elemento)==0:
            primero = elemento
        if tupla.index(elemento)== (len(tupla) - 1):
            ultimo = elemento
    tupla.pop(0)
    tupla.insert(0,ultimo)
    tupla.pop(len(tupla)-1)
    tupla.append(primero)
    tupla = tuple(tupla)
    return tupla

tupla = (1,2,3,4,5,6,7,8,9)
print(f"Tupla con primer y ultimo elemento intercambiados: {intercambiar_tupla(tupla)}")

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Escribe una función llamada encontrar_pares_impares que acepte una tupla de
números enteros como parámetro y devuelva una tupla que contenga dos listas: una
lista de números pares y otra lista de números impares. Por ejemplo, si la tupla original
es (1, 2, 3, 4, 5, 6, 7, 8, 9), la función debería devolver ([2, 4, 6, 8], [1, 3, 5, 7, 9]). """


def encontrar_pares_impares(tupla):
    par = []
    impar = []
    for elemento in tupla:
        if elemento % 2 == 0:
            par.append(elemento)
        else:
            impar.append(elemento)
    tupla = []
    tupla.append(par)
    tupla.append(impar)
    tupla = tuple(tupla)
    return(tupla)

print(f"Tupla con lista de numeros pares e impares: {encontrar_pares_impares(tupla)}")

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Escribe un programa que solicite al usuario que ingrese una lista de nombres. El
programa debe crear una tupla a partir de la lista y luego imprimir los nombres que
comienzan con la letra 'A'. """

continuar = 0
listaNombres = []
while(True):
    nombre = input("Ingrese un nombre: ")
    listaNombres.append(nombre)
    continuar = int(input("¿Desea continuar agregando nombres?\n1-Si\n2-No\n:"))
    if continuar == 1:
        continue
    elif continuar == 2:
        break
    else:
        print("Opcion no valida")

listaNombres = tuple(listaNombres)

print("Nombres que comienzan con A:")
for nombre in listaNombres:
    if nombre[0]=="A":
        print(nombre)

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Escribe un programa que cree una tupla que contenga los primeros diez números de la
serie de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55) y luego imprima la tupla.
 """
 
tupla = [0,1]
con = 0
n1 = 0
n2 = 1
resultado = 0
while(con<9):
    resultado = n1+n2
    tupla.append(resultado)
    n1 = n2
    n2 = resultado
    con+=1
tupla.pop(0)
tupla = tuple(tupla)
print(f"Primeros diez elementos de la serie Fibonacci (Sin el 0): {tupla}")

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Escribe un programa que reciba una tupla de colores y cree un diccionario donde cada
elemento de la tupla tenga una clave numérica incremental, empezando en 1. Imprime
la tupla de colores original y el diccionario resultante. """

def diccionarioTupla(tupla):
    diccionario = {}
    for i in range(len(tupla)):
        diccionario[i+1]=tupla[i]
    return diccionario

colores = ("Rojo","Verde","Azul","Amarillo")
print(f"Diccionario con los colores de la tupla dada: {diccionarioTupla(colores)}")

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Dado el diccionario dic_edades que contiene como llave el nombre de una persona y
como valor su edad, escribe un programa que determine quién es la persona con
mayor edad y lo imprima por pantalla. """

dic_edades={
    "Alejo":20,
    "Lucas":19,
    "Goneveva":81,
    "Roberto":60,
    "Pancrasio":80
}
mayor = ""
flag = 0
for nombre,edad in dic_edades.items():
    if flag==0:
        mayor = nombre
        flag=1
    if(edad>dic_edades[mayor]):
        mayor = nombre
print(f"La persona con mas edad del diccionario es: {mayor}")

seguir = input("Presione ENTER para continuar")
os.system("cls")

""" Dado el diccionario dic_notas que contiene como llave el nombre de un estudiante y
como valor su nota en un examen, escribe un programa que calcule el promedio de
notas y genere una lista con los nombres de los estudiantes que aprobaron (nota
mayor o igual a 7). Imprime por pantalla el promedio de notas y la lista de estudiantes
aprobados. """

dic_notas = {
    "Alejo":4,
    "Lucas":5,
    "Agostina":7,
    "Santiago":10,
    "Ivan":8,
    "Eleazar":10,
}
promedio = 0
aprobados = []
for estudiante,nota in dic_notas.items():
    promedio += nota
    if (dic_notas[estudiante]>=7):
        aprobados.append(estudiante)
promedio = promedio / len(dic_notas)
print(f"El promedio de notas es: {promedio}")
print(f"Los estudiantes aprobados son {aprobados}")









