import os
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
num = 0
flag = 1
continuar = ""

while flag==1:
    num = int(input("Introduce un número: "))
    if num >= 1 and num <= len(meses):
        print(meses[num-1])
        continuar=input("\nPresione enter para continuar")
        os.system("cls")
    elif num==0:
        flag = 0
    else:
        print("Error, ese numero no pertence a ningun mes")
        continuar=input("Presione enter para continuar")
        os.system("cls")
            
