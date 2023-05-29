
#Contar las palabras de una oracion y expresarlas en diccionario


def contarPalabras(oracion):
    frecuencias={}
    palabras = oracion.split()
    for palabra in palabras:
        frecuencias[palabra]=palabras.count(palabra)
    print(frecuencias)

contarPalabras(input("Ingrese una oracion: "))


#Llenar un diccionario con nombres y sus respectivas edades, luego mostrar por pantalla el mas joven

def masJoven():
    diccionario = {}
    mayor = 0
    while(True):
        nombre = input("Ingrese nombre de la persona: ")
        edad = int(input("Ingrese edad de la persona: "))
        diccionario[nombre]=edad
        continuar = int(input("¿Desea continuar agregando personas?\n1)Si\n2)No\n"))
        if continuar == 1:
            continue
        elif continuar == 2:
            break     
    menor = 0
    nombreMenor = ""
    b = 0

    for nombre,edad in diccionario.items():
        if b==0:
            menor = edad
            nombreMenor = nombre
            b=1
        if edad < menor:
            menor = edad
            nombreMenor = nombre
    
    print(f"El menor es {nombreMenor} con {menor} años")
            
masJoven()


