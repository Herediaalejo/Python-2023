from funciones import checkOption
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

producto = [producto1,producto2,producto3,producto4]

for i in range(len(producto)):
        infoProducto = înfoProducto + "\n" + (f"{producto[i].getCodigo()} {producto[i].getNombre()} {producto[i].getPrecio()} {producto[i].getStock()}")

menu = """

Bienvenido a la tienda!!!!





Ingrese la opción que desee:

1) Buscar producto
2) Añadir a carrito
3) Acceder a carrito
4) Salir
"""
os.system("cls")
while True:
    for i in range(len(producto)):
        print(f"{producto[i].getCodigo()} {producto[i].getNombre()} {producto[i].getPrecio()} {producto[i].getStock()}")

    opcion = checkOption(input(menu),4,menu)

    if opcion == 1:
        codigo = input("Ingrese nombre o codigo de producto a buscar: ")

        for codigo, i in enumerate(producto):
            if codigo == producto[i].getCodigo():
                print("")









        
    



    

    










# Crear un carrito de compras en Python que funcione únicamente en la consola. El programa debe presentar un menú con las siguientes opciones:Mostrar productos en detalle: Muestra el código del producto, nombre, marca, precio, stock, color y características de cada producto en la tienda.Mostrar información breve del producto: Muestra el código del producto, nombre, precio y cantidad 
# 
# 
# 
# 
# disponible de cada producto en la tienda.Buscar producto por código: Permite al usuario ingresar un código de producto y muestra la información detallada de ese producto.Realizar compra: Permite al usuario agregar productos al carrito de compras. Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, el precio unitario y el costo total por cada item añadido.Finalizar compra: Cierra la compra y muestra un detalle de los productos comprados, incluyendo el nombre, la cantidad, el precio unitario y el costo total.Salir: Permite al usuario salir del programa.
# El programa debe mostrar al usuario un diccionario con la información de los productos disponibles en la tienda.
# Debe validar las opciones seleccionadas por el usuario en el menú.
# Mientras el usuario esté navegando en el carrito de compras, los datos deben permanecer disponibles. 
# Deberá contar el programa con una visualización previa de los productos añadidos en el carrito en la cual se le consulte al usuario si está conforme o no con los productos añadidos , teniendo en cuenta el desarrollo que pueda desencadenar si el usuario desea MODIFICAR lo que tiene en el carrito , es decir que si desea modificar lo que tiene en el carrito pueda modificar la cantidad de un producto determinado , para aumentar o disminuir la cantidad o eliminar del carrito completamente algún producto.
# El programa debe incluir una opción en el menú para cerrar la compra y mostrar un detalle de los productos comprados.
# Además, se debe actualizar permanentemente el stock de los productos y validar la existencia de la cantidad de productos antes de realizar una compra. 
# También se debe validar que el resultado total de la compra pueda incluir números decimales.
# Para buscar productos, se debe validar el ingreso del ID del producto.
# Por cada acción que el usuario seleccione, se debe validar si la respuesta es 'SI' o 'NO'."
# Se validará todos los ingresos y egresos de información del sistema.
# Este programa debe ser una réplica de  todas las aplicaciones de compras en línea conocidas. 


