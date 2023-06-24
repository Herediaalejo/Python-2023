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

def listarProductos(productos,carritoFlag=False):
    productosListados = []

    if carritoFlag:
        for i in range(len(productos)):
            productosListados.append([0]*8)

        for i in range(len(productos)):
            productosListados[i][0] = productos[i].getNombre()
            productosListados[i][1] = productos[i].getPrecio()
            productosListados[i][2] = productos[i].getMarca()
            productosListados[i][3] = productos[i].getColor()
            productosListados[i][4] = productos[i].getStock()
            productosListados[i][5] = productos[i].getCaracteristicas()
            productosListados[i][6] = productos[i].getCodigo()
            productosListados[i][7] = productos[i].getSubtotal()
    else:

        for i in range(len(productos)):
            productosListados.append([0]*7)

        for i in range(len(productos)):
            productosListados[i][0] = productos[i].getNombre()
            productosListados[i][1] = productos[i].getPrecio()
            productosListados[i][2] = productos[i].getMarca()
            productosListados[i][3] = productos[i].getColor()
            productosListados[i][4] = productos[i].getStock()
            productosListados[i][5] = productos[i].getCaracteristicas()
            productosListados[i][6] = productos[i].getCodigo()
    
    return productosListados

def buscarProducto(codigo,listaProductos):
    cont = 0

    if codigo.isnumeric():
        codigo = int(codigo)
    else:
        codigo = codigo.lower()
        palabraBuscada = list(codigo)
    

    for i in range(len(listaProductos)):
        palabraEncontrada =  list(listaProductos[i].getNombre().lower())

        if codigo == listaProductos[i].getCodigo() or codigo == (listaProductos[i].getNombre()).lower():
            productoEncontrado = listaProductos[i]
            return productoEncontrado
        
        for k in range(len(palabraBuscada)):
            if palabraBuscada[k]==palabraEncontrada[k]:
                cont += 1

        if cont > 2:
            productoEncontrado = listaProductos[i]
            return productoEncontrado

    print("Producto no encontrado")
    return False
        
def añadirACarrito(producto, clase, subclase, carrito):

    if isinstance(producto, clase):
        cantidad = checkNum(input(f"¿Que cantidad desea añadir?\nDisponibles: {producto.getStock()}\n:"))

        if cantidad <= producto.getStock() and cantidad>0:
            productoCarrito = subclase(producto.getCodigo(),producto.getNombre(),producto.getMarca(),producto.getPrecio(),cantidad,producto.getColor(),producto.getCaracteristicas())
            carrito.append(productoCarrito)
            producto.setStock(producto.getStock()-cantidad)
            print("\nProducto agregado al carrito!")
            return True
        
        elif cantidad == 0:
            print("La cantidad no puede ser 0")
            return False
        
        elif cantidad < 0 :
            print("La cantidad no puede ser negativa")
            return False
        
        else:
            print("La cantidad supera el stock disponible")
            return False

def volverAMenu():
    op = ""
    menu="""
¿Desea volver al menu?
1)Si
2)No
"""
    print(menu)
    op = checkOption(input(":"),2,menu)

    if op == 1:
        return True
    else:
        return False


def productosBreve(productos=[],producto="",todos=True,carritoFlag=False):

    longitud = []

    total = 0

    if carritoFlag:

        infoProductos = listarProductos(productos, True)

        for i in range(8):
            longitud.append([0]*len(productos))

        for i in range(8):
            for k in range(len(productos)):
                longitud[i][k]=len(str(infoProductos[k][i]))
        
        for i in range(8):
            longitud[i] = max(longitud[i])
        
    
        totalGuion = longitud[6] + 8 + longitud[0] + 4  + longitud[1] + 4 + longitud[4] + 8 + longitud[7] + 4 + 5

        if todos:

            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Subtotal", longitud[7]+5)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            for producto in productos:
                if producto.getStock()>0:
                    tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, "$"+str(producto.getSubtotal()), longitud[7]+5)
                    total = total + producto.getSubtotal()
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            tabla =  tabla + "\n" + "|  {:<{}}|".format(f"Total: ${total}",totalGuion-2)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

        else:
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Subtotal", longitud[7]+5)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            
            if producto.getStock()>0:
                tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, "$"+str(producto.getSubtotal()), longitud[7]+5)
                total = total + producto.getSubtotal()
        
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            tabla =  tabla + "\n" + "|  {:<{}}|".format(f"Total: ${total}",totalGuion-2)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

    else:

        infoProductos = listarProductos(productos)

        for i in range(7):
            longitud.append([0]*len(productos))

        for i in range(7):
            for k in range(len(productos)):
                longitud[i][k]=len(str(infoProductos[k][i]))
        
        for i in range(7):
            longitud[i] = max(longitud[i])
        
        totalGuion = longitud[6] + 8 + longitud[0] + 4  + longitud[1] + 4 + longitud[4] + 8 + 3
        if todos:
            
            
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            for producto in productos:
                if producto.getStock()>0:
                    tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

        else:
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8)
                
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"
    
    if len(productos)>0:
        return tabla
    else:
        return "No hay producto disponibles en este momento"

def productosDetallado(productos=[],producto="",todos=True, carritoFlag=False):

    total = 0

    if carritoFlag:
        infoProductos = listarProductos(productos,True)

        longitud = []

        for i in range(8):
            longitud.append([0]*len(productos))

        for i in range(8):
            for k in range(len(productos)):
                longitud[i][k]=len(str(infoProductos[k][i]))
        
        for i in range(8):
            longitud[i] = max(longitud[i])
        
        totalGuion = longitud[6] + 8 + longitud[0] + 4 + longitud[2] + 4 + longitud[3] + 4 + longitud[1] + 4 + longitud[4] + 8 + longitud[5] + longitud[7] + 4 + 12

        if todos:
            
            
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Marca",longitud[2]+4, "Color",longitud[3]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Características",longitud[5], "Subtotal", longitud[7]+5)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            for producto in productos:
                if producto.getStock()>0:
                    tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, producto.getMarca(),longitud[2]+4, producto.getColor(),longitud[3]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, producto.getCaracteristicas(),longitud[5], "$"+str(producto.getSubtotal()), longitud[7]+5)
                    total = total + producto.getSubtotal()

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            tabla =  tabla + "\n" + "|  {:<{}}|".format(f"Total: ${total}",totalGuion-2)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

        else:
            
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |{:^{}}|".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Marca",longitud[2]+4, "Color",longitud[3]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Características",longitud[5], "Subtotal", longitud[7]+5)

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |{:^{}}|".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, producto.getMarca(),longitud[2]+4, producto.getColor(),longitud[3]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, producto.getCaracteristicas(),longitud[5], "$"+str(producto.getSubtotal()), longitud[7]+5)
                
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

    else:

        infoProductos = listarProductos(productos)

        longitud = []

        for i in range(7):
            longitud.append([0]*len(productos))

        for i in range(7):
            for k in range(len(productos)):
                longitud[i][k]=len(str(infoProductos[k][i]))
        
        for i in range(7):
            longitud[i] = max(longitud[i])
        
        totalGuion = longitud[6] + 8 + longitud[0] + 4 + longitud[2] + 4 + longitud[3] + 4 + longitud[1] + 4 + longitud[4] + 8 + longitud[5] + 10

        if todos:
            
            
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Marca",longitud[2]+4, "Color",longitud[3]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Características",longitud[5])

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

            for producto in productos:
                if producto.getStock()>0:
                    tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, producto.getMarca(),longitud[2]+4, producto.getColor(),longitud[3]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, producto.getCaracteristicas(),longitud[5])
                
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

        else:
            tabla = "+" + "-"*totalGuion + "+"
        
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |".format("Código",longitud[6]+8,"Producto", longitud[0]+4, "Marca",longitud[2]+4, "Color",longitud[3]+4, "Precio", longitud[1]+4, "Cantidad", longitud[4]+8, "Características",longitud[5])

            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"
            
            tabla = tabla + "\n" + "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|{:^{}}|  {:<{}}  |".format(producto.getCodigo(),longitud[6]+8,producto.getNombre(), longitud[0]+4, producto.getMarca(),longitud[2]+4, producto.getColor(),longitud[3]+4, "$" + str(producto.getPrecio()), longitud[1]+4, producto.getStock(), longitud[4]+8, producto.getCaracteristicas(),longitud[5])
                
            tabla = tabla + "\n" + "+" + "-"*totalGuion + "+"

    
    return tabla

def tipoMenu(op,productos,carrito=[]):
    menu = ""
    if op == 1:
        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosBreve(productos, 0, True)}

Todos los precios están expresados en dólares

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información detallada de productos
4) Salir
"""
    elif op == 2:

        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosDetallado(productos, 0, True)}

Todos los precios están expresados en dólares

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información breve de productos
4) Salir
"""
        
    elif op == 3:
        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosBreve(productos, 0, True)}

Todos los precios están expresados en dólares

Su carrito:

{productosBreve(carrito,0,True,True)}

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información detallada de productos
4) Modificar compra
5) Finalizar compra
6) Salir
"""
    elif op == 4:
        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosDetallado(productos,0,True)}

Todos los precios están expresados en dólares

Su carrito:

{productosBreve(carrito,0,True,True)}

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información detallada de productos
4) Modificar compra
5) Finalizar compra
6) Salir
"""
    elif op == 5:
        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosBreve(productos, 0, True)}

Todos los precios están expresados en dólares

Su carrito:

{productosDetallado(carrito,0,True,True)}

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información detallada de productos
4) Modificar compra
5) Finalizar compra
6) Salir
"""
        
    elif op == 6:
        menu = f"""
Bienvenido a la tienda TecnoBlade!!!!

Estos son nuestros productos disponibles actualmente:

{productosDetallado(productos,0,True)}

Todos los precios están expresados en dólares

Su carrito:

{productosDetallado(carrito,0,True,True)}

¿Que desea realizar? Ingrese una opción:

1) Buscar producto
2) Añadir a carrito
3) Información breve de productos
4) Modificar compra
5) Finalizar compra
6) Salir
"""
    return menu


def modificarProducto(carrito,productos):
    cod=input("Ingrese codigo o nombre de producto a modificar: ")
    productoCarrito= buscarProducto(cod,carrito)
    producto = buscarProducto(cod,productos)
    op = checkOption(input("¿Que desea modificar del producto?\n1)Agregar cantidad\n2)Reducir cantidad\n3)Eliminar de carrito\n:"),3,"¿Que desea modificar del producto?\n1)Agregar cantidad\n2)Reducir cantidad\n3)Eliminar de carrito\n:")
    if op == 1:
        cantidad = checkNum(input(f"¿Que cantidad desea añadir?\nDisponibles: {producto.getStock()}\n:"))
        if cantidad <= producto.getStock():
            producto.setStock(producto.getStock()-cantidad)
            productoCarrito.setStock(productoCarrito.getStock()+cantidad)
            productoCarrito.setSubtotal(productoCarrito.getSubtotal()+cantidad*productoCarrito.getPrecio())
            return False
    elif op == 2:
        cantidad = checkNum(input(f"¿En cuanto desea reducir la cantidad?\nCantidad actual: {productoCarrito.getStock()}\n:"))
        if cantidad <= productoCarrito.getStock():
            producto.setStock(producto.getStock()+cantidad)
            productoCarrito.setStock(productoCarrito.getStock()-cantidad)
            productoCarrito.setSubtotal(productoCarrito.getSubtotal()-cantidad*productoCarrito.getPrecio())
            return False
    elif op == 3:
        producto.setStock(productoCarrito.getStock()+producto.getStock())
        carrito.remove(buscarProducto(cod,carrito))
        return True
    





