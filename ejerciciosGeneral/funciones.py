import os

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
                print (f"El valor '{num}' no es un numero")
                num = input("Ingrese un valor valido: ")

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
        except ValueError:
            os.system("cls")
            print(menu)
            print("Valor invalido")
            opcion = input("Ingrese opcion valida: ")

def buscarProducto(codigo,listaProductos):
 
    for i in range(len(listaProductos)):
        
        if codigo == listaProductos[i].getCodigo():
            productoDetallado = f"""
PRODUCTO: {listaProductos[i].getNombre()}

PRECIO: ${listaProductos[i].getPrecio()} 

Marca: {listaProductos[i].getMarca()}

Color: {listaProductos[i].getColor()}

Características: {listaProductos[i].getCaracteristicas()}

Stock: {listaProductos[i].getStock()}
            """
            
            return productoDetallado