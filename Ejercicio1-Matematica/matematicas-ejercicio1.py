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

#Ejercicio 1

valor_coheficiente_principal = 0
valor_ordenada_distinto = 0
valor_pendiente_perpendicular = 0

valores_independientes_distintos = []

comportamiento_recta=""
ecuacion = ""
con = 0

start=True
op = ""


while(start==True):

    opcion = int(input("Bienvenidos al programa de operacion de ecuaciones matematicas! \n Elija la opcion que desee: \n 1) Rectas paralela y perpendicular a una dada. \n 2) Análisis de una función lineal.\n 3) Análisis de una función cuadrática. \n:"))

    #os.system("cls") 

    if opcion == 1 or opcion==2:

        valor_pendiente= Fraction(str(input("Ingrese el valor del coheficiente principal (siendo ax + b, ingrese el valor de a): ")))

        valor_ordenada= Fraction(str(input("Ingrese el valor del termino independiente (siendo ax + b, ingrese el valor de b): ")))

        if opcion==1:

            valor_pendiente_perpendicular = valor_pendiente * (1 / (valor_pendiente * valor_pendiente))
            valor_pendiente_perpendicular = valor_pendiente_perpendicular * (-1)

            while(con<3):

                valor_ordenada_distinto = 0
                valor_ordenada_distinto = random.randint(-20,20)

                if(valor_ordenada_distinto!=valor_ordenada):
                    valores_independientes_distintos.append(valor_ordenada_distinto)
                    con+=1

            print("La condicion de paralelismo es que el coheficiente principal se mantenga y el termino independiente sea el que cambie. \n Ejemplos de ecuaciones con rectas paralelas a la dada son:")
            con = 0
            
            while(con<3):
                
                if(valores_independientes_distintos[con]>0):
                    ecuacion= str(Fraction(str(valor_pendiente))) + "x + "  + str(Fraction(str(valores_independientes_distintos[con])))
                else:
                    ecuacion= str(Fraction(str(valor_pendiente))) + "x - "  + str(Fraction(str(valores_independientes_distintos[con] * -1)))
                print(ecuacion)
                con+=1

            print("La condicion de perpendicularidad es que la pendiente debe ser inversa y opuesta, el termino independiente puede cambiar o no hacerlo. \n Ejemplos de ecuacion con rectas perpendiculares a la dada son:")
            
            con = 0
            ecuacion= str(Fraction(str(valor_pendiente_perpendicular))) + "x + "  + str(Fraction(str(valor_ordenada)))
            print (ecuacion)

            while(con<2):
                if(valores_independientes_distintos[con]>0):
                    ecuacion= str(Fraction(str(valor_pendiente_perpendicular))) + "x + "  + str(Fraction(str(valores_independientes_distintos[con])))
                else:
                    ecuacion= str(Fraction(str(valor_pendiente_perpendicular))) + "x - "  + str(Fraction(str(valores_independientes_distintos[con]*-1)))
                print(ecuacion)
                con+=1

            op=input("\n ¿Desea seguir realizando operaciones con el programa? \n S/n \n:")
            if (op=="s" or op=="S"):
                start
            else:
                start=False
    
        if opcion==2:
            
            if(valor_pendiente>0):
                pendiente = "Creciente"
            else:
                pendiente = "Decreciente"
                
            raiz = (valor_ordenada * -1) / valor_pendiente

            print("Corte en x = " + str(raiz))
            print("Corte en y = " + str(valor_ordenada))
            print("Pendiente = " + str(pendiente))

    
        
#Ejercicio 3

    if(opcion==3):

        valor_pendiente = Fraction(input("Ingrese el coheficiente principal. Siendo ax2 + bx + c ingrese el valor de a \n :"))
        valor_lineal = Fraction(input("Ingrese el termino lineal. Siendo ax2 + bx + c ingrese el valor de b \n :"))
        valor_ordenada = Fraction(input("Ingrese el termino independiente. Siendo ax2 + bx + c ingrese el valor de c \n :"))

        if(valor_pendiente>0):
            pendiente = 1
        else:
            pendiente = -1

        try:
            delta = sqrt(valor_lineal**2 - 4 * valor_pendiente * valor_ordenada)
        except ValueError:
            b = 1

        if(b==0):

            raiz = ((valor_lineal * (-1)) + delta) / (2 * valor_pendiente)

            raices.append(raiz)

            raiz = ((valor_lineal * (-1)) - delta) / (2 * valor_pendiente)

            raices.append(raiz)


        vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

        vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada

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
        
        if(b==0):
            print("Las raices son: x1 = " + str(Fraction(raices[0])) + " x2 = " + str(Fraction(raices[1])))
        
        print("Los vertices son: Vx = " + str(vertice_x) + " Vy = " + str(vertice_y))
        
        if(delta<0):
            print("Las raices son complejas")
        elif(delta==0):
            tipo_raiz = 2
        elif(delta>0):
            tipo_raiz = 3
        
        
        
        
        
    