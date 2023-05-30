numeros = (9,12,18,12,15,9,12,18,15)
num = 0
cont=0
b=0

num = input("Ingrese un número: ")

while(True):
    try:
        int(num)
        break
    except ValueError:
        num=(input("Ingrese un numero correcto: "))
    

for numero in numeros:
    if(num==numero):
        cont+=1
print(f"El número {num} se repite {cont} veces en la tupla")
