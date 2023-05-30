from funciones import checkOption
# Crear un carrito de compras en Python que funcione únicamente en la consola. El programa debe presentar un menú con las siguientes opciones:Mostrar productos en detalle: Muestra el código del producto, nombre, marca, precio, stock, color y características de cada producto en la tienda.Mostrar información breve del producto: Muestra el código del producto, nombre, precio y cantidad disponible de cada producto en la tienda.Buscar producto por código: Permite al usuario ingresar un código de producto y muestra la información detallada de ese producto.Realizar compra: Permite al usuario agregar productos al carrito de compras. Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, el precio unitario y el costo total por cada item añadido.Finalizar compra: Cierra la compra y muestra un detalle de los productos comprados, incluyendo el nombre, la cantidad, el precio unitario y el costo total.Salir: Permite al usuario salir del programa.
productosDetallados = {
    

}

menu = """

Bienvenido a la tienda!!!!
Ingrese la opción que desee:

1) Mostrar productos en detalle
2) Mostrar información breve del producto
3) Buscar producto por código
4) Realizar compra
5) Finalizar compra
6) Salir
"""
opcion = checkOption(input(menu),6,menu)











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


