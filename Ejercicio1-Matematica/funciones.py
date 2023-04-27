import random
from fractions import Fraction
opcion = 0
valor_pendiente=0
valor_ordenada=0
valor_coheficiente_principal = 0
valor_ordenada_distinto = 0
valor_pendiente_perpendicular = 0

valores_independientes_distintos = []

ecuacion = ""
con = 0

start=True
op = ""
while(start==True):
    opcion = int(input("Bienvenidos al programa de operacion de ecuaciones matematicas! \n elija la opcion que desee: \n 1) Rectas paralela y perpendicular a una dada. \n 2) Análisis de una función lineal.\n 3) Análisis de una función cuadrática. \n:"))
    if opcion == 1 or opcion==2:
        valor_pendiente= Fraction(str(input("Ingrese el valor del coheficiente principal (siendo ax + b, ingrese el valor de a): ")))
        valor_ordenada= Fraction(str(input("Ingrese el valor del termino independiente (siendo ax + b, ingrese el valor de b): ")))
        if opcion==1:

            while(con<3):
                valor_ordenada_distinto = 0
                valor_pendiente_perpendicular = valor_pendiente * (1 / (valor_pendiente * valor_pendiente))
                valor_pendiente_perpendicular = valor_pendiente_perpendicular * (-1)
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
            print("La condicion de perpendicularidad es que la pendiente debe ser inversa y reciproca, el termino independiente puede cambiar o no hacerlo. \n Ejemplos de ecuacion con rectas perpendiculares a la dada son:")
            
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

        
        

"""         ecuacion=str(valor_pendiente) + "x "  + str(valor_pendiente_paralela2)
        print(ecuacion) """

"""     if opcion==2:
        valor_ordenada_perpendicular1 = 
        valor_pendiente_perpendicular2 = 0 """
        
        
        
        
        
    