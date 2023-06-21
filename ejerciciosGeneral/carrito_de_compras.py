from funciones import *
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
    
producto1 = Producto(1,"IPHONE X","APPLE",1000,23,"Rojo","Cámara 20MP, 8GB RAM, IOS 15")
producto2 = Producto(2,"MACBOOK AIR","APPLE",3000,10,"Gris claro","Apple M1 8GB de RAM 256GB SSD, Apple M1 8-Core GPU 60 Hz 2560x1600px")
producto3 = Producto(3,"VISION PRO","APPLE",4000,15,"Gris","Full vision 360°")
producto4 = Producto(4,"S23 ULTRA","SAMSUNG",800,10,"Negro","Cámara 200MP, 12gb RAM, Snapdragon 8 Gen 2")

carrito = []
op = 0

""" os.system("cls") """
while True:
    productos = [producto1,producto2,producto3,producto4]

    mensajeProductosBreve = productosBreve(productos, 0, True)

    mensajeProductosDetallado = productosDetallado(productos, 0, True)

    mensajeCarritoBreve = productosBreve(carrito,0,True)

    """ mensajeCarritoDetallado = productosDetallado(carrito,0,True) """

    menu2 = False
    

    menu = f"""
Bienvenido a la tienda!!!!

Estos son nuestros productos disponibles actualmente:

{mensajeProductosBreve}
Todos los precios están expresados en dólares

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Salir
"""
    if len(carrito)>0:
        menu = f"""
Bienvenido a la tienda!!!!

Estos son nuestros productos disponibles actualmente:

{mensajeProductosBreve}

Todos los precios están expresados en dólares

Su carrito:

{mensajeCarritoBreve}

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información detallada de productos
4) Modificar compra
5) Finalizar compra
6) Salir
"""
        menu2 = True

    flag = False
    if menu2 == False:
        opcion = checkOption(input(menu+":"),3,menu)
    else:
        opcion = checkOption(input(menu+":"),6,menu)

    if opcion == 1:

        while True:

            if flag == False:

                productoBuscado = buscarProducto(input("Ingrese código o nombre de producto a buscar: "),productos)

                if productoBuscado != False:

                    mensajeCarrito ="¿Desea añadirlo al carrito? \n1) Si \n2) No"

                    print(f"\nProducto encontrado!!!\n{productosDetallado(productos,productoBuscado, False)}\n{mensajeCarrito}")

                    op=checkOption(input(":"),2,mensajeCarrito)

                    if op == 1:
                        añadirACarrito(productoBuscado,Producto,carrito)

                else:
                    print("Producto no encontrado")

                flag = volverAMenu()
                if flag == True:
                    break
    if opcion == 2:

        while True:

            carrito = añadirACarrito(buscarProducto(input("Ingrese código de producto a agregar: "),productos), Producto, carrito)
            continuar = input("Ingrese ENTER para continuar")
            flag = volverAMenu()
            if flag == True:        
                break
    
    if opcion == 3 and menu2==False:
        break

    if opcion == 3 and menu2==True:
        menu = f"""
        ¿A que información desea acceder?

        1) Productos en tienda

        2) Productos en carrito
        """
        opcion = checkOption(input(menu+":"),3,menu)