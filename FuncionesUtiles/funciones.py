def checkNum(num):
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            try:
                num = float(num)
            except ValueError:
                print (f"El valor '{num}' no es un numero")
                num = input("Ingrese un numero valido: ")