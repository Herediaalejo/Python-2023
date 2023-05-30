
productos = [("Mouse", 3000, 10, "Redragon"), ("Smartwatch", 8900, 15, "Samsung"),
("Teclado", 30000, 5, "Razer"), ("Auriculares", 10000, 3, "Logitech")]

precio_maximo = 10000

marca_buscada = "Samsung"

lista_productos_filtrados = []

for producto in productos:
    if producto[1] <= precio_maximo and producto[3] == marca_buscada:
        lista_productos_filtrados.append(producto)
print(lista_productos_filtrados)