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

    codigo = codigo.lower()

    if codigo.isnumeric():
        codigo = int(codigo)
 
    for i in range(len(listaProductos)):
        
        if codigo == listaProductos[i].getCodigo() or codigo == (listaProductos[i].getNombre()).lower():
            productoEncontrado = listaProductos[i]
            return productoEncontrado
    return False
        
def añadirACarrito(producto, clase, carrito):
    if isinstance(producto, clase):
        cantidad = checkNum(input(f"¿Que cantidad desea añadir?\nDisponibles: {producto.getStock()}\n:"))
        if cantidad <= producto.getStock():
            productoCarrito = clase(producto.getCodigo(),producto.getNombre(),producto.getMarca(),producto.getPrecio(),cantidad,producto.getColor(),producto.getCaracteristicas())
            carrito.append(productoCarrito)
            producto.setStock(producto.getStock()-cantidad)
            print("Producto agregado al carrito!")
            return carrito
        else:
            print("La cantidad supera el stock disponible")
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
    print(menu)
    op = checkOption(input(":"),2,menu)

    if op == 1:
        return True
    else:
        return False


def productosBreve(productos,producto="",todos=True):

    productoBreve = "------------------------------------------------\n"

    if todos:

        infoProductos = listarProductos(productos)

        for i in range(len(infoProductos)):
            for k in range(4):
                if infoProductos[i][4]>0:
                    if k==0:
                        productoBreve = productoBreve + str(infoProductos[i][k]) + (" " * (14 - len(str(infoProductos[i][k])))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
                    elif k==1:
                        productoBreve = productoBreve + "$ " + str(infoProductos[i][k]) + (" " * (6 - len(str(infoProductos[i][k]))))
                    elif k==2:
                        productoBreve = productoBreve + "Cantidad: " + str(infoProductos[i][4]) + (" " * (4 - len(str(infoProductos[i][4]))))
                    elif k==3:
                        productoBreve = productoBreve + "Cod: " + str(infoProductos[i][6]) + (" " * (4 - len(str(infoProductos[i][6]))))
            productoBreve = productoBreve + "\n"
    else:
        
        productoBreve = productoBreve + str(producto.getNombre()) + (" " * (14 - len(str(producto.getNombre())))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
                
        productoBreve = productoBreve + "$ " + str(producto.getPrecio()) + (" " * (6 - len(str(producto.getPrecio()))))
                 
        productoBreve = productoBreve + "Cantidad: " + str(producto.getStock()) + (" " * (4 - len(str(producto.getStock()))))
                
        productoBreve = productoBreve + "Cod: " + str(producto.getCodigo()) + (" " * (4 - len(str(producto.getCodigo()))))
        
    if len(productoBreve)>0:
        productoBreve = productoBreve + "------------------------------------------------"
        return productoBreve
    else:
        return ("No hay productos disponibles")

def productosDetallado(productos=[],producto="",todos=True):


    if todos:

        infoProductos = listarProductos(productos)

        longitud = []

        for i in range(7):
            longitud.append([0]*len(productos))

        for i in range(7):
            for k in range(len(productos)):
                longitud[i][k]=len(str(infoProductos[k][i]))
        
        for i in range(7):
            longitud[i] = max(longitud[i])

        print(longitud)

        Tabla = """\
+---------------------------------------------------------------------------+
| Cod   Producto    Marca     Precio     Color    Cantidad   Caracteristicas|
|---------------------------------------------------------------------------|
{}
+---------------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>23} |".format(*fila)
 for fila in infoProductos)))
print (Tabla)

        
        print(productoDetallado)



        """productoDetallado = "Codigo" + (" " * 3) + "Producto" + (" " * (longitud[0]-8)) + "Marca" + (" " * (longitud[2]-5)) + "Precio" + (" " * (longitud[1]-6)) + "Color" + (" " * (longitud[3]-5)) + "Cantidad" + (" " * (longitud[4]-8)) + "Características" + (" " * (longitud[5]-15)) + "\n"

        for i in range(len(infoProductos)):
            for k in range(7):
                if i != 0:
                    if infoProductos[i-1][4]>0:
                        if k==0:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][6]) + (" " * 9)
                        elif k==1:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][0]) + (" " * (longitud[0]-len(str(infoProductos[i-1][0]))))
                        elif k==2:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][2]) + (" " * (longitud[2]-len(str(infoProductos[i-1][2]))))
                        elif k==3:
                            productoDetallado = productoDetallado + "$ " + str(infoProductos[i-1][1]) + (" " * (longitud[1]-len(str(infoProductos[i-1][1]))))
                        elif k==4:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][3]) + (" " * (longitud[3]-len(str(infoProductos[i-1][3]))))
                        elif k==5:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][4]) + (" " * (longitud[4]-len(str(infoProductos[i-1][4]))))
                        elif k==6:
                            productoDetallado = productoDetallado + str(infoProductos[i-1][5]) + (" " * (longitud[5]-len(str(infoProductos[i-1][5]))))
            productoDetallado = productoDetallado + "\n"
    else:
        
        productoDetallado = productoDetallado + str(producto.getNombre()) + (" " * (14 - len(str(producto.getNombre())))) #Formula para alinear los caracteres, en este caso 14 es el máximo de caracteres
                
        productoDetallado = productoDetallado + "$ " + str(producto.getPrecio()) + (" " * (6 - len(str(producto.getPrecio()))))
                
        productoDetallado = productoDetallado + "Cantidad: " + str(producto.getStock()) + (" " * (4 - len(str(producto.getStock()))))
                
        productoDetallado = productoDetallado + "Cod: " + str(producto.getCodigo()) + (" " * (4 - len(str(producto.getCodigo()))))
        
    if len(productoDetallado)>0:
        productoDetallado = productoDetallado + "------------------------------------------------"
        print(productoDetallado) 
    else:
        return ("No hay productos disponibles")"""









