import os

def validacionEdad(edad):
    if(edad>=18):
        print("Eres mayor")
    elif(edad>=100):
        print("No creo que tengas esa edad")
    elif(edad<0):
        print("No existen edades negativas")
    else:
        print("Eres menor")


def sumaLista(lista):
    i=0
    suma=0
    for i in range (0,len(lista)):
        suma+=lista[i]
    print("El resultado es:" + str(suma)) 

def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    inicio = 0
    fin = 0
    fin = len(palabra) - 1
    while palabra[inicio] == palabra[fin]:
        if inicio == fin:
            return ("Es palindromo")
        inicio +=1
        fin -= 1
    return ("No es palindromo")

def conversionADolar(dinero):
    pais=int(input("""¿De que pais eres?
    1) Argentina
    2) Peru
    3) Mexico
    4) Chile
    5) Venezuela
    6) Otro \n"""))
    if(pais==1):
        dolar = dinero / 470
    elif(pais==2):
        dolar = dinero / 3.7
    elif(pais==3):
        dolar = dinero / 17.76
    elif(pais==4):
        dolar = dinero / 794
    elif(pais==5):
        dolar = dinero / 2497254.94
    elif(pais==6):
        dolar = dinero / int(input("¿Cuanto vale el dolar en su pais? \n")) 
    print("Usted tiene $" + str(round(dolar,6)) + " dolares" )

def tiempoDeViaje(distancia):
    horas = 0
    minutos = 0
    segundos = 0
    dias = 0
    vehiculo= int(input(""" ¿En que va a viajar?
    1)Auto
    2)Avion
    3)Moto
    4)Colectivo
    5)Caminando
    6)Teletransportacion \n"""))
    if(vehiculo==1):
        horas = distancia / 120
    elif(vehiculo==2):
        horas = distancia / 860
    elif(vehiculo==3):
        horas = distancia / 100
    elif(vehiculo==4):
        horas= distancia / 90
    elif(vehiculo==5):
        horas = distancia / 5
    elif(vehiculo==6):
        horas = distancia * 0.000000000000001
    horas = round(horas, 2)
    minutos = round(horas * 60,2)
    segundos = round(minutos * 60,2)
    dias = round(horas / 24,2)
    print(f"""Usted va a tardar en promedio:
    {dias} dias
    {horas} horas
    {minutos} minutos
    {segundos} segundos
    En llegar a su destinto
    """)

validacionEdad(int(input("Ingrese su edad: ")))

op=input("Enter para continuar")
os.system("cls")

print("Sumaremos los valores de una lista conformada por los numeros 1,5,8,6,10,2")
sumaLista([1,5,8,6,10,2])

op=input("Enter para continuar")
os.system("cls")

print(palindromo(input("Un palindromo es una palabra que se lee y se escribe igual al derecho y al reves. \n Ingrese palabra a comprobar: ")))

op=input("Enter para continuar")
os.system("cls")

conversionADolar(int(input("Haremos la conversion de tu dinero a dolares. Ingrese cantidad de dinero a convertir: ")))

op=input("Enter para continuar")
os.system("cls")

tiempoDeViaje(int(input("Ingrese distancia a destino en km: ")))

op=input("Enter para continuar")
os.system("cls")

    




