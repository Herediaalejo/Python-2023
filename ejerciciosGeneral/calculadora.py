import funciones
import os


suma = lambda a,b : a + b
resta = lambda a,b : a - b
multip = lambda a,b : a * b
div = lambda a,b : a / b
potencia = lambda a,b : a ** b
raizCuad = lambda a : a ** 1/2
raizCub = lambda a : a ** 1/3


def validNum(value):
    while True:
        if value == "r":
            return value
        try: 
            value = int(value)
            return value
        except:
            try:
                value = float(value)
                return value
            except:
                if value == "z" or value == "x":
                    return value
                value = input(f"El valor {value} no es valido. \nIngrese un número valido:")

def calculate(op):
    result = 0
    value = 0
    flag = False
    if op > 0 and op < 6:
        while value != "z":
            print("Resultado: ", result)
            if not flag:
                value = validNum(input("Ingrese valor a operar: "))
                if value == "x" or value == "z":
                    break
                result = value
                flag = True
            else:
                value2 = validNum(input("Ingrese siguiente valor: "))
                os.system("cls")
                print("Ingrese 'x' para volver atras o 'z' para salir ")
                if value2 != "z" and value2 != "x":
                    result = getResult(result, value2, op)
                elif value2 == "x" or value2 == "z":
                    break
        return value2
    else:
        value = validNum(input("Ingrese valor a operar: "))
        result = getResult(value, result, op)
        print("Resultado: ", result)
        sig = input("Ingrese ENTER para volver atras")
    return


def getResult(value, value2, op):
    if op == 1:
        result = suma(value, value2)
    if op == 2:
        result = resta(value, value2)
    if op == 3:
        result = multip(value, value2)
    if op == 4:
        result = div(value, value2)
    if op == 5:
        result = potencia(value, value2)
    if op == 6:
        result = raizCuad(value)
    if op == 7:
        result = raizCub(value)
    return result



menu = """
Que operacion desea realizar?
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia
6) Raiz Cuadrada
7) Raiz Cubica
: """
def main():
    while True:
        numList = []
        opList = []
        op = 0
        operation = ""
        op = 0
        print("Bienvenido a la calculadora MathMag")
        op = funciones.checkOption(input(menu),7,menu)
        if calculate(op) == "z":
            break

            



            

if __name__ == "__main__":
    main()