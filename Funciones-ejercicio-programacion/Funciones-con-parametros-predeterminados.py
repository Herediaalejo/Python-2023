import os

def recordatorio(mes="Enero", nro="1", dia = "lunes", hora="00:01"):
    recordatorios=[]
    fin = False
    op = 0
    while fin==False:
        tarea = input(f"¿Que desea recordar el dia {dia} {nro} de {mes}?\n")
        recordatorios.append([ "hora: " + hora , "dia: " + dia , "nro: " + nro , "mes: " + mes , "tarea: " +tarea])
        op = int(input("""¿Desea registrar algo mas?
        1)Si
        2)No
        """))
        if(op==1):
            hora = input("¿A que hora?\n")
            dia = input("¿Que dia?\n")
            nro = input("¿Que número de dia?\n")
            mes = input("¿Que mes?\n")
        elif(op==2):
            fin=True
    print(recordatorios)

def resolverEcuacionLineal(coheficiente_principal, termino_independiente = 0):
    pendiente="inexistente"
    raiz=0
    if(coheficiente_principal>0):
        pendiente="Creciente"
    elif(coheficiente_principal<0):
        pendiente="Decreciente"
    if(termino_independiente==0):
        raiz=0
    else:
        raiz = (termino_independiente * -1) / coheficiente_principal
    print(f"""La pendiente es {pendiente}
    La raiz es {raiz}
    La ordenada al origen es {termino_independiente}""")

def tiempoDeHoy(dia="lunes"):
    tiempo=""
    dia = dia.lower()
    dia = dia.replace(" ", "")
    dia = dia.replace("á", "a")
    dia = dia.replace("é", "e")
    dia = dia.replace("í", "i")
    dia = dia.replace("ó", "o")
    dia = dia.replace("ú", "u")
    if(dia=="lunes"):
        tiempo="nublado"
    elif(dia=="martes"):
        tiempo="lluvioso"
    elif(dia=="miercoles"):
        tiempo="nublado"
    elif(dia=="jueves"):
        tiempo="soleado y humedo"
    elif(dia=="viernes"):
        tiempo="lluvioso y con tormenta"
    elif(dia=="sabado"):
        tiempo="soleado"
    elif(dia=="domingo"):
        tiempo="lluvioso"
    else:
        print("Dia invalido")
        return
    print(f"El tiempo para el {dia} va a estar {tiempo} ")

def piedraPapelTijera(juego="tijera"):

    if(juego=="tijera"):
        print("Elijo..... piedra, perdiste")
    elif(juego=="papel"):
        print("Elijo..... tijera, perdiste")
    elif(juego=="piedra"):
        print("Elijo..... papel, perdiste")

def prediccionMundial(pais="argentina"):
    pais = pais.lower()
    pais = pais.replace(" ", "")
    pais = pais.replace("á", "a")
    pais = pais.replace("é", "e")
    pais = pais.replace("í", "i")
    pais = pais.replace("ó", "o")
    pais = pais.replace("ú", "u")
    if pais=="argentina":
        print("FELICIDADES, van a salir campeones, muchaaachos")
    else:
        print(f"Lo lamento... , {pais} se queda en fase de grupos, el ganador es Argentina, tierra de Messi y Maradona")


recordatorio(input("Bienvenido al sistema de recordatorios. Ingrese mes: "), input("Ingrese nro de dia: "), input("Ingrese dia: "), input("Ingrese hora: "))

op=input("Enter para continuar")

os.system("cls")

resolverEcuacionLineal(int(input("Bienvenido al sistema de resolucion de ecuaciones lineales. Ingrese coheficiente principal: ")), int(input("Ingrese termino independiente: ")))

op=input("Enter para continuar")

os.system("cls")

tiempoDeHoy(input("Comprobando tiempo..., introduzca el dia a comprobar: "))

op=input("Enter para continuar")

os.system("cls")

piedraPapelTijera(input("Bienvenido a piedra, papel o tijera. Introduzca su jugada: "))

op=input("Enter para continuar")

os.system("cls")

prediccionMundial(input("Bienvenido a la prediccion del mundial. Ingrese su pais: "))

op=input("Enter para continuar")

os.system("cls")