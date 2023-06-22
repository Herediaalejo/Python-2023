import random
import os
from fractions import Fraction
from math import sqrt
opcion = 0
valor_pendiente=0
valor_lineal=0
valor_ordenada=0
pendiente = ""
raiz = 0
delta=0
tipo_raiz=0
vertice_x=0
vertice_y=0
intervalo_crecimiento = ""
intervalo_decrecimiento = ""
b=0
raices = []
continuar = ""
valor_coheficiente_principal = 0
valor_ordenada_distinto = 0
valor_pendiente_perpendicular = 0
valores_independientes_distintos = []
comportamiento_recta=""
ecuacion = ""
con = 0
flag=0
op = ""
signo = ""

def checkOption(opcion,cantidad,menu=""):
    while True:
        try:
            opcion = int(opcion)
            for op in range(cantidad+1):
                if op == 0:
                    continue
                if opcion==op:
                    return opcion
            os.system("cls")
            print(menu)
            print("Valor fuera de rango")
            opcion = input("Ingrese opcion valida: ")
            os.system("cls")
        except ValueError:
            os.system("cls")
            print(menu)
            print("Valor invalido")
            opcion = input("Ingrese opcion valida: ")
            os.system("cls")

def checkNum(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            try:
                num = float(num)
                return num
            except ValueError:
                try:
                    num = Fraction(num)
                    return num
                except ValueError:
                    print (f"El valor '{num}' no es un numero")
                    num = input("Ingrese un valor valido: ")

def checkCant(cantidad,cantidadMinima, cantidadMaxima=0):
    while True:
        try:
            cantidad = int(cantidad)
            if cantidad < cantidadMinima:
                cantidad = input("Valor fuera de rango. Ingrese cantidad: ")
            else:
                return cantidad
        except ValueError:
            cantidad = input("El valor debe ser entero. Ingrese cantidad: ")


def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)

while(True):

    os.system("cls")

    if(flag==0):
        opcion = input("¡Bienvenidos al programa de operación de ecuaciones matemáticas! \n Elija la opción que desee: \n 1) Rectas paralela y perpendicular a una dada \n 2) Análisis de una función lineal\n 3) Análisis de una función cuadrática \n 4) Sucesiones\n 5) Salir\n:")
    else:
        opcion = input("Ingrese una opción valida \n 1) Rectas paralela y perpendicular a una dada \n 2) Análisis de una función lineal\n 3) Análisis de una función cuadrática \n 4) Sucesiones\n 5) Salir\n:")

    if(opcion.isnumeric()):
        opcion=int(opcion)
        if(opcion>4 or opcion<0):
            flag=1
    else:
        flag=1

    os.system("cls") 

    if opcion == 1 or opcion==2:

        flag = 0
        
        while(True):

            valor_pendiente= input("Ingrese el valor del coeficiente principal (siendo ax + b, ingrese el valor de a):")

            if valor_pendiente == "0":
                print("Valor invalido")
                continue
                
            try:
                valor_pendiente = Fraction(valor_pendiente)
                break                   
            except ValueError:
                print("Valor invalido")
                
        
        while(True):
    
            valor_ordenada= input("Ingrese el valor del término independiente (siendo ax + b, ingrese el valor de b):")    
            try:
                valor_ordenada = Fraction(valor_ordenada)
                break     
            except ValueError:
                print("Valor invalido")
        
        if(flag==0):

            if opcion==1:

                valores_independientes_distintos=[]
                con = 0
               
                while(con<3):

                    #Busco valores aleatorios para darle a los valores independientes
                    valor_ordenada_distinto = 0
                    valor_ordenada_distinto = random.randint(-20,20)

                    #Agrego valores aleatorios a una lista que va a guardar los tres valores distintos
                    if(valor_ordenada_distinto!=valor_ordenada):
                        if(len(valores_independientes_distintos)==0):
                            valores_independientes_distintos.append(valor_ordenada_distinto)
                            con+=1
                        else:
                            for valor in valores_independientes_distintos:
                                if(valor!=valor_ordenada_distinto):
                                    valores_independientes_distintos.append(valor_ordenada_distinto)
                                    con+=1
                                    break

                print("\nLa condición de paralelismo es que el coeficiente principal se mantenga y el termino independiente sea el que cambie. \nEcuaciones con rectas paralelas a la dada:")
                con = 0
                
                while(con<3):
                    
                    #Construyo la ecuacion para luego imprimirla
                    if(valores_independientes_distintos[con]>0):
                        ecuacion = f"y = {Fraction(valor_pendiente)}x + {Fraction(valores_independientes_distintos[con])}"
                    else:
                        ecuacion = f"y = {Fraction(valor_pendiente)}x - {Fraction(valores_independientes_distintos[con])*(-1)} "
                    print(ecuacion)
                    con+=1

                print("\nLa condición de perpendicularidad es que la pendiente debe ser inversa y opuesta, el termino independiente puede cambiar o no hacerlo. \nEcuaciones con rectas perpendiculares a la dada:")
                
                valor_pendiente_perpendicular = (1 / valor_pendiente) * (-1)
                
                con = 0
                if(valor_ordenada>=0):     
                    ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)}x + {Fraction(valor_ordenada)}"
                else:
                    ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)}x - {Fraction(valor_ordenada) * (-1)}"
                print (ecuacion)

                while(con<2):
                    if(valores_independientes_distintos[con]>=0):
                        ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)}x + {Fraction(valores_independientes_distintos[con])}"
                    else:
                        ecuacion = f"y = {Fraction(valor_pendiente_perpendicular)}x - {Fraction(valores_independientes_distintos[con]) *(-1)}"
                    print(ecuacion)
                    con+=1
                    

                op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")
                if (op=="n" or op=="N"):
                    break
                
        #Analisis ecuacion lineal
        
            if opcion==2:
                
                if(valor_pendiente>0):
                    pendiente = "Creciente"
                else:
                    pendiente = "Decreciente"

                if(valor_ordenada==0): 
                    raiz=0
                else:
                    # ax + b = 0
                    # -b/a = x
                    raiz = (valor_ordenada * -1) / valor_pendiente
                    
                print("Corte en x = " + str(raiz))
                print("Corte en y = " + str(valor_ordenada))
                print("Pendiente = " + str(pendiente))

                op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")
                if (op=="n" or op=="N"):
                    break   
        
#Analisis ecuacion cuadratica

    if opcion==3:

        raices = []

        while(True):
 
            valor_pendiente = input("Ingrese el coeficiente principal (Siendo ax² + bx + c ingrese el valor de a) \n :")
            
            if valor_pendiente == "0":
                print("Valor Invalido")
                continue

            try:
                valor_pendiente = Fraction(valor_pendiente)
                break      
            except ValueError:
                print("Valor invalido")
            
        while(True):
            valor_lineal = input("Ingrese el termino lineal (Siendo ax² + bx + c ingrese el valor de b) \n :")

            try:
                valor_lineal = Fraction(valor_lineal)
                break      
            except ValueError:
                print("Valor invalido")
            
        while(True):

            valor_ordenada = input("Ingrese el termino independiente (Siendo ax² + bx + c ingrese el valor de c) \n :")
        
            try:
                valor_ordenada = Fraction(valor_ordenada)
                break      
            except ValueError:
                print("Valor invalido")
                                
        if(flag==0):

            #Concava hacia arriba o hacia abajo

            if(valor_pendiente>0):
                pendiente = 1
            else:
                pendiente = -1

            #b^2 -4 * a * c

            delta = valor_lineal**2 - 4 * valor_pendiente * valor_ordenada
                

            if(delta>=0):

                #(-b +- √(b² - 4 * a * c)) / 2 * a

                raiz = ((valor_lineal * (-1)) + sqrt(delta)) / (2 * valor_pendiente)

                raices.append(raiz)

                raiz = ((valor_lineal * (-1)) - sqrt(delta)) / (2 * valor_pendiente)

                raices.append(raiz)


            vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

            vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada

            if(delta >= 0):

                print("Corte con el eje x: x1 = " + str(Fraction(raices[0])) + " x2 = " + str(Fraction(raices[1])))
                    
            print(f"Corte con el eje y: {valor_ordenada}")


            if(pendiente==1):
                
                intervalo_decrecimiento = "(-∞, " + str(vertice_x) + ")"  
                intervalo_crecimiento = "(" + str(vertice_x) + ", +∞)"
                
                print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
                print("El intervalo de crecimiento es " + intervalo_crecimiento)
            
            elif(pendiente==-1):
                
                intervalo_crecimiento = "(-∞, " + str(vertice_x) + ")"  
                intervalo_decrecimiento = "(" + str(vertice_x) + ", +∞)"
                
                print("El intervalo de crecimiento es " + intervalo_crecimiento)
                print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
            
    
            print("Los vértices son: Vx = " + str(vertice_x) + " Vy = " + str(vertice_y))

            print(f"La coordenada del vértice es ({vertice_x},{vertice_y})")

            if(valor_pendiente>0):
                print("La concavidad es hacia arriba ")

            elif(valor_pendiente<0):
                print("La concavidad es hacia abajo ")
        
            
            if(delta<0):
                print("Las raíces son complejas ")

            elif(delta==0):
                print("Las raíces son dobles ")

            elif(delta>0):
                print("Las raíces son reales ")

            op=input("\n¿Desea seguir realizando operaciones con el programa? \nS/n \n:")

            if (op == "n" or op =="N"):
                break
    if opcion == 4:
        
        opcion = checkOption(input("¿Que tipo de sucesiones desea calcular?\n 1) Sucesiones aritméticas\n 2) Sucesiones geométricas\n 3) Regresar a menu principal\n:"),3," 1) Sucesiones aritméticas\n 2) Sucesiones geométricas\n 3) Regresar a menu principal\n:")
        
        if opcion == 1:

            while True:

                terminoSucesion = checkNum(input("Ingrese primer término de la sucesión: "))

                diferencia = checkNum(input("Ingrese diferencia de la sucesión: "))

                cantidadTermino = checkCant(input("Ingrese cantidad de términos que desea obtener(mínimo 5): "),5)

                sucesion = ""

                tipoSucesion = ""

                if diferencia > 0:
                    tipoSucesion = "creciente"
                elif diferencia < 0:
                    tipoSucesion = "decreciente"
                elif diferencia == 0:
                    tipoSucesion = "constante"
                
                calculo = f"a₁ = {terminoSucesion}\n"

                terminoSiguiente = terminoSucesion

                for i in range(cantidadTermino-1):
                    sucesion += str(terminoSiguiente) + ", "
                    calculo += f"a{get_sub(str(i+1))}{get_sub('+1')} = {terminoSiguiente} + {diferencia}\n"  
                    terminoSiguiente = terminoSiguiente + diferencia
                sucesion += str(terminoSiguiente) + ", ..."
                print(f"\nSUCESIÓN ARITMÉTICA\n-------------------\nPrimer término: {terminoSucesion}\nDiferencia: {diferencia}\nFórmula: aₙ₊₁ = aₙ + d\n\nCálculo: \n{calculo}\nResultado: {sucesion}\nLa sucesión es {tipoSucesion}")
                
                op=checkOption(input("\n¿Desea seguir realizando sucesiones aritméticas? \n1)Si\n2)No \n:"),2,"\n¿Desea seguir realizando sucesiones aritméticas? \n1)Si\n2)No \n:")
                if op ==1:
                    continue
                if op == 2:
                    break
        if opcion == 2:

            while True:

                terminoSucesion = checkNum(input("Ingrese primer termino de la sucesión: "))

                razon = checkNum(input("Ingrese razón de la sucesión: "))

                cantidadTermino = checkCant(checkNum(input("Ingrese cantidad de términos que desea obtener(mínimo 5): ")),5)

                sucesion = ""
                
                calculo = f"a₁ = {terminoSucesion}\n"

                terminoSiguiente = terminoSucesion

                tipoSucesion = ""
                if terminoSucesion > 0:
                    if razon > 1:
                        tipoSucesion = "creciente"
                    elif  razon > 0 and razon < 1:
                        tipoSucesion = "decreciente"
                    elif razon == 1:
                        tipoSucesion = "constante"
                    elif razon < 0:
                        tipoSucesion = "alternante"
                elif terminoSucesion < 0:
                    if razon > 1:
                        tipoSucesion = "decreciente"
                    elif  razon > 0 and razon < 1:
                        tipoSucesion = "creciente"
                    elif razon == 1:
                        tipoSucesion = "constante"
                    elif razon < 0:
                        tipoSucesion = "alternante"
                else:
                    tipoSucesion = "constante"


                for i in range(1,cantidadTermino):
                    sucesion += str(terminoSiguiente) + ", "
                    calculo += f"a{get_sub(str(i+1))} = {terminoSucesion} * {razon}{get_super(str(i+1))}{get_super(str(-1))}\n"  
                    terminoSiguiente = terminoSucesion * (razon ** (i+1-1))
                sucesion += str(terminoSiguiente) + ", ..."
                print(f"\nSUCESIÓN GEOMÉTRICA\n-------------------\nPrimer término: {terminoSucesion}\nRazón: {razon}\nFórmula: aₙ = a₁ * rⁿ⁻¹\n\nCálculo: \n{calculo}\nResultado: {sucesion}\nLa sucesión es {tipoSucesion}")
                
                op=checkOption(input("\n¿Desea seguir realizando sucesiones geométricas? \n1)Si\n2)No \n:"),2,"\n¿Desea seguir realizando sucesiones geométricas? \n1)Si\n2)No \n:")
                if op ==1:
                    continue
                if op == 2:
                    break
        if opcion == 3:
            break

    if opcion == 5:
        break


        
        
        
        
    