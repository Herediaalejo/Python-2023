from funciones import checkOption, buscarProducto, checkNum
import os
# Crear un carrito de compras en Python que funcione únicamente en la consola. El programa debe presentar un menú con las siguientes opciones:Mostrar productos en detalle: Muestra el código del producto, nombre, marca, precio, stock, color y características de cada producto en la tienda.Mostrar información breve del producto: Muestra el código del producto, nombre, precio y cantidad disponible de cada producto en la tienda.Buscar producto por código: Permite al usuario ingresar un código de producto y muestra la información detallada de ese producto.Realizar compra: Permite al usuario agregar productos al carrito de compras. Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, el precio unitario y el costo total por cada item añadido.Finalizar compra: Cierra la compra y muestra un detalle de los productos comprados, incluyendo el nombre, la cantidad, el precio unitario y el costo total.Salir: Permite al usuario salir del programa.

class Producto():

    def __init__(self,codigo,nombre,marca,precio,stock,color,caracteristicas):
        self.codigo=codigo
        self.nombre=nombre
        self.marca=marca
        self.precio=precio
        self.stock=stock
        self.color=color
        self.caracteristicas=caracteristicas
    
    def setStock(self,stock):
        self.stock=stock

    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre
    
    def getMarca(self):
        return self.marca
        
    def getPrecio(self):
        return self.precio
        
    def getStock(self):
        return self.stock
        
    def getColor(self):
        return self.color
    
    def getCaracteristicas(self):
        return self.caracteristicas
    
producto1 = Producto(1,"IPHONE X","APPLE",1000,23,"Rojo","Camara 20MP, 8GB RAM, IOS 15")
producto2 = Producto(2,"MACBOOK AIR","APPLE",3000,10,"Gris claro","Apple M1 8GB de RAM 256GB SSD, Apple M1 8-Core GPU 60 Hz 2560x1600px")
producto3 = Producto(3,"VISION PRO","APPLE",4000,15,"Gris","Full vision 360°")
producto4 = Producto(4,"S23 ULTRA","SAMSUNG",800,10,"Negro","Camara 200MP, 12gb RAM, Snapdragon 8 Gen 2")

productos = [producto1,producto2,producto3,producto4]

infoProductos = []

for i in range(len(productos)):
    infoProductos.append([0]*7)

for i in range(len(productos)):
        infoProductos[i][0] = productos[i].getNombre()
        infoProductos[i][1] = productos[i].getPrecio()
        infoProductos[i][2] = productos[i].getMarca()
        infoProductos[i][3] = productos[i].getColor()
        infoProductos[i][4] = productos[i].getStock()
        infoProductos[i][5] = productos[i].getCaracteristicas()
        infoProductos[i][6] = productos[i].getCodigo()

mensajeProductosBreve = ""
for i in range(len(infoProductos)):
    for k in range(4):
        if k==0:
            mensajeProductosBreve = mensajeProductosBreve + str(infoProductos[i][k]) + (" " * (14 - len(str(infoProductos[i][k])))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
        elif k==1:
            mensajeProductosBreve = mensajeProductosBreve + "$ " + str(infoProductos[i][k]) + (" " * (6 - len(str(infoProductos[i][k]))))
        elif k==2:
            mensajeProductosBreve = mensajeProductosBreve + "Stock: " + str(infoProductos[i][4]) + (" " * (4 - len(str(infoProductos[i][4]))))
        elif k==3:
                mensajeProductosBreve = mensajeProductosBreve + "Cod: " + str(infoProductos[i][6]) + (" " * (4 - len(str(infoProductos[i][6]))))
    mensajeProductosBreve = mensajeProductosBreve + "\n"


menu = f"""
Bienvenido a la tienda!!!!

Estos son nuestros productos disponibles actualmente:

{mensajeProductosBreve}

Todos los precios están expresados en dólares

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Acceder a carrito
4) Salir
"""
os.system("cls")
while True:

    opcion = checkOption(input(menu),4,menu)

    if opcion == 1:
        productoBuscado = buscarProducto(checkNum(input("Ingrese nombre o código de producto a buscar: ")),productos)
        print(f"""
              
Producto encontrado!!!
{productoBuscado}             
""")