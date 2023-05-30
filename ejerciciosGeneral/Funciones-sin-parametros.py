import random
import os

def fibonacci():
    lista = [0]
    num1 = 0
    num2 = 1
    resultado = 0
    con = 0
    while con < 30:
        resultado = num1 + num2
        lista.append(resultado)
        num1 = num2
        num2 = resultado
        con +=1
    print(lista)

def chisteMalo():
    opcion = random.randint(1,5)
    if(opcion==1):
        print("Si se muere una pulga, ¿a dónde va? Al pulgatorio.")
    elif(opcion==2):
        print("¿Cómo se dice pelo sucio en chino? Chin cham pu.")
    elif(opcion==3):
        print("El otro día vendí mi aspiradora. Lo único que hacía era acumular polvo.")
    elif(opcion==4):
        print("¿Cuál es el colmo de un jardinero? Que siempre le dejen plantado.")
    elif(opcion==5):
        print("— Eres un fanático de la informática, ¿verdad? \n — Sí... mouse o menos.")

def sorteo():
    listaParticipante = []
    cantParticipantes = int(input("Introduzca cantidad de participantes: "))
    con = 0
    while con < cantParticipantes:
        participante = input("Introduzca nombre del participante: ")
        listaParticipante.append(participante)
        con+=1
    ganador = listaParticipante[random.randint(0, len(listaParticipante) -1)]
    print("El ganador es: " + ganador + " FELICIDADES")

def datosRandom():
    opcion = random.randint(1,5)
    if(opcion==1):
        print("La Torre Eiffel puede ser 15 cm más alta durante el verano. Se debe a la expansión térmica, que significa que el hierro se calienta, las partículas ganan energía cinética y ocupan más espacio.")
    elif(opcion==2):
        print("Los dientes humanos son la única parte del cuerpo que no puede curarse por sí misma. Los dientes están recubiertos de esmalte, que no es un tejido vivo.")
    elif(opcion==3):
        print("La gente es más creativa en la ducha. Cuando nos duchamos con agua caliente, experimentamos un mayor flujo de dopamina que nos hace más creativos.")
    elif(opcion==4):
        print("Se puede escuchar el latido de una ballena azul a más de 3 kilómetros de distancia. Las ballenas azules pesan una media de entre 130.000 y 150.000 kg, y su corazón pesa aproximadamente 180 kg.")
    elif(opcion==5):
        print("La Luna tiene terremotos lunares. Se producen debido a las tensiones de las mareas relacionadas con la distancia entre la Luna y la Tierra.")

    
def eleccion():
    print("Ingrese dos opciones, escojere una: ")
    op1 = input("opcion 1: ")
    op2 = input("opcion 2: ")
    escogida = random.randint(1,2)
    if(escogida==1):
        print("La opcion escogida fue: " + op1)
    if(escogida==2):
        print("La opcion escogida fue: " + op2)


print("Esta es la escala fibonacci: " )
fibonacci()

op=input("Enter para continuar")
os.system("cls")

print("Te contare un chiste malo: ")
chisteMalo()

op=input("Enter para continuar")
os.system("cls")

print("Hagamos un sorteo: ")
sorteo()

op=input("Enter para continuar")
os.system("cls")

print("Te tiro este dato: ")
datosRandom()

op=input("Enter para continuar")
os.system("cls")

eleccion()

op=input("Enter para continuar")
os.system("cls")


