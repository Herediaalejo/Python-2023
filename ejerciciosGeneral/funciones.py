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

def listarProductos(productos):
    productosListados = []

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
 
    for i in range(len(listaProductos)):
        
        if codigo == listaProductos[i].getCodigo():
            productoEncontrado = listaProductos[i]
            return productoEncontrado
    return False
        
def añadirACarrito(producto, clase, carrito):
    if isinstance(producto, clase):
        carrito.append(producto)
        return carrito
    print("Producto no encontrado")
    return carrito

def volverAMenu():
    op = ""
    menu="""
    ¿Desea volver al menu?
    1)Si
    2)No
    """
    op = checkOption(input(":"),2,menu)

    if op == 1:
        return False
    else:
        return True


def productosBreve(productos,producto="",todos=True):

    productoBreve = ""

    if todos:

        infoProductos = listarProductos(productos)
        
        for i in range(len(infoProductos)):
            for k in range(4):
                if k==0:
                    productoBreve = productoBreve + str(infoProductos[i][k]) + (" " * (14 - len(str(infoProductos[i][k])))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
                elif k==1:
                    productoBreve = productoBreve + "$ " + str(infoProductos[i][k]) + (" " * (6 - len(str(infoProductos[i][k]))))
                elif k==2:
                    productoBreve = productoBreve + "Stock: " + str(infoProductos[i][4]) + (" " * (4 - len(str(infoProductos[i][4]))))
                elif k==3:
                        productoBreve = productoBreve + "Cod: " + str(infoProductos[i][6]) + (" " * (4 - len(str(infoProductos[i][6]))))
            productoBreve = productoBreve + "\n"
    else:
        
        productoBreve = productoBreve + str(producto.getNombre()) + (" " * (14 - len(str(producto.getNombre())))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
                
        productoBreve = productoBreve + "$ " + str(producto.getPrecio()) + (" " * (6 - len(str(producto.getPrecio()))))
                 
        productoBreve = productoBreve + "Stock: " + str(producto.getStock()) + (" " * (4 - len(str(producto.getStock()))))
                
        productoBreve = productoBreve + "Cod: " + str(producto.getCodigo()) + (" " * (4 - len(str(producto.getCodigo()))))
        
    return productoBreve

def productosDetallado(productos=[],producto="",todos=True):
            
        if todos:
        
            for i in range(len(productos)):
                    
                productoDetallado = f"""
            PRODUCTO: {productos[i].getNombre()}

            PRECIO: ${productos[i].getPrecio()}

            Marca: {productos[i].getMarca()}

            Color: {productos[i].getColor()}

            Características: {productos[i].getCaracteristicas()}

            Stock: {productos[i].getStock()}


                        """
        else:
            
            productoDetallado = f"""
            PRODUCTO: {producto.getNombre()}

            PRECIO: ${producto.getPrecio()}

            Marca: {producto.getMarca()}

            Color: {producto.getColor()}

            Características: {producto.getCaracteristicas()}

            Stock: {producto.getStock()}
                        """
   
        return productoDetallado





