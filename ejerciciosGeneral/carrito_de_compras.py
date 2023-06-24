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
    
class ProductoCarrito(Producto):
    def __init__(self,codigo,nombre,marca,precio,stock,color,caracteristicas):
        super().__init__(codigo,nombre,marca,precio,stock,color,caracteristicas)  # Llamada al constructor de la superclase
        self.subtotal = self.precio*self.stock
    
    def getSubtotal(self):
        return self.subtotal
    
    def setSubtotal(self,subtotal):
        self.subtotal = subtotal

    
producto1 = Producto(1,"IPHONE X","APPLE",1000,23,"Rojo","Cámara 20MP, 8GB RAM, IOS 15")
producto2 = Producto(2,"MACBOOK AIR","APPLE",3000,10,"Gris claro","Apple M1 8GB de RAM 256GB SSD, Apple M1 8-Core GPU 60 Hz 2560x1600px")
producto3 = Producto(3,"VISION PRO","APPLE",4000,15,"Gris","Full vision 360°")
producto4 = Producto(4,"S23 ULTRA","SAMSUNG",800,10,"Negro","Cámara 200MP, 12gb RAM, Snapdragon 8 Gen 2")
producto5 = Producto(5,"APPLE WATCH","APPLE",400,33,"Rojo","GPS - Caja de aluminio medianoche 45 mm - Correa deportiva medianoche")
producto6 = Producto(6,"MONITOR GAMER","SAMSUNG",300,7,"Negro","Pantalla led de 22, resolución de 1920px-1080px")
producto7 = Producto(7,"AIR PODS","APPLE",200,55,"Blanco","Cámara 200MP, 12gb RAM, Snapdragon 8 Gen 2")


compras = []

carrito = []
op = 0
menu1 = True
menu2 = False
menu3 = False
menu6 = False
detallado = False
""" os.system("cls") """
while True:

    op = 0

    productos = [producto1,producto2,producto3,producto4,producto5,producto6,producto7]

    if menu1:
        menu = tipoMenu(1,productos)

    flag = False
    
        
    if menu3:
        menu = tipoMenu(3,productos,carrito)


    if menu1:
        opcion = checkOption(input(menu+":"),4,menu)
    else:
        opcion = checkOption(input(menu+":"),6,menu)

    if opcion == 1:

        while True:

            if flag == False:

                productoBuscado = buscarProducto(input("Ingrese código o nombre de producto a buscar: "),productos)

                if productoBuscado != False:

                    mensajeCarrito ="¿Desea añadirlo al carrito? \n1)Si \n2)No"

                    print(f"\nProducto encontrado!!!\n{productosDetallado(productos,productoBuscado, False)}\n{mensajeCarrito}")

                    op=checkOption(input(":"),2,mensajeCarrito)

                    if op == 1:
                        añadido = añadirACarrito(productoBuscado,Producto, ProductoCarrito,carrito)
                        if añadido:
                            menu1 = False
                            menu2 = False
                            menu3 = True
                            menu6 = False

                flag = volverAMenu()
                if flag == True:
                    break
    if opcion == 2:

        while True:

            añadido = añadirACarrito(buscarProducto(input("Ingrese código de producto a agregar: "),productos), Producto, ProductoCarrito, carrito)
            carritoDef = True
            if añadido:
                menu1 = False
                menu2 = False
                menu3 = True
                menu6 = False
            flag = volverAMenu()
            if flag == True:        
                break
  
    if opcion == 3:

        if menu1:
            menu = tipoMenu(2,productos,carrito)
            menu1 = False
            menu2 = True

        elif menu2:
            menu = tipoMenu(1,productos,carrito)
            menu2 = False
            menu1 = True
        
        elif menu6:
            menu = tipoMenu(3, productos, carrito)
            menu6 = False


        else:
            menu = f"""
¿A que información desea acceder?

1) Productos en tienda
2) Productos en carrito
3) Ambos
"""
            opcion = checkOption(input(menu+":"),3,menu)

            if opcion == 1:
                menu = tipoMenu(4,productos,carrito)
                menu3 = False
            elif opcion == 2:
                menu = tipoMenu(5, productos, carrito)
                menu3 = False
            elif opcion == 3:
                menu = tipoMenu(6, productos, carrito)
                menu3 = False
                menu6 = True
    if menu1:
        if opcion == 4:
            break
    else:
        if opcion == 4:
            print(productosBreve(carrito,0,True,True))
            modificarProducto(carrito,productos)
            menu1 = False
            menu2 = False
            menu3 = True
            menu6 = False
            if len(carrito)==0:
                menu1 = True
                menu2 = False
                menu3 = False
                menu6 = False
        if opcion == 5:
            print(productosDetallado(carrito,0,True,True))

            op = checkOption(input("¿Con que desea pagar?\n1) Efectivo\n2) Tarjeta de crédito\n3) Tarjeta de débito\n:"),3,"¿Con que desea pagar?\n1) Efectivo\n2) Tarjeta de crédito\n3) Tarjeta de débito\n:")
            
            if op == 1:

                print("Gracias por comprar!!! La dirección para recibir sus productos y pagar es la siguiente: Av. Cárcano 1290, Tienda de tecnología TecnoBlade")
                carrito.clear()
                volver = checkOption(input("\n¿Desea seguir comprando?\n1) Si\n2) No\n:"),2,"\n¿Desea seguir comprando?\n1) Si\n2) No\n:")
                menu1 = True
                menu2 = False
                menu3 = False
                menu6 = False

            elif op == 2:
                cuotas = checkOption(input("¿En cuantas cuotas desea pagar?\n1) 12 cuotas sin interés\n2) 6 cuotas sin interés\n3) 3 cuotas sin interés\n4) 1 cuota sin interés\n:"),4,"¿En cuantas cuotas desea pagar?\n1) 12 cuotas sin interés\n2) 6 cuotas sin interés\n3) 3 cuotas sin interés\n4) 1 cuota sin interés\n:")
                tarjeta = input("Introduzca número de la tarjeta de crédito: ")
                print("Transacción realizada con éxito! \nGracias por comprar, puede retirar su producto en: Villa Carlos Paz, Av. Cárcano 1290, Tienda de tecnología TecnoBlade")
                carrito.clear()
                volver = checkOption(input("\n¿Desea seguir comprando?\n1) Si\n2) No\n:"),2,"\n¿Desea seguir comprando?\n1) Si\n2) No\n:")
                menu1 = True
                menu2 = False
                menu3 = False
                menu6 = False
                
            elif op == 3:

                tarjeta = input("Introduzca número de la tarjeta de débito: ")
                print("Transacción realizada con éxito! \nGracias por comprar, puede retirar su producto en: Villa Carlos Paz, Av. Cárcano 1290, Tienda de tecnología TecnoBlade")
                carrito.clear()
                volver = checkOption(input("\n¿Desea seguir comprando?\n1) Si\n2) No\n:"),2,"\n¿Desea seguir comprando?\n1) Si\n2) No\n:")
                menu1 = True
                menu2 = False
                menu3 = False
                menu6 = False
                


        if opcion == 6:
            break


        