import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

"""
SQL

create database Almacen;
Use Almacen;

create table Marca(
->Id_Marca int auto_increment,
->marca varchar(150),
->primary key(Id_Marca));

create table Categoria(
->Id_Categoria int auto_increment,
->nombre varchar(150),
->primary key(Id_Categoria));

create table Producto(
->Id_Producto int auto_increment,
->nombre varchar(150),
->Id_Categoria int,
->Id_Marca int,
->primary key(Id_Producto),
->foreign key Id_Marca references Marca(Id_Marca),
->foreign key Id_Categoria references Categoria(Id_Categoria));

create table Precio(
->Id_Precio int auto_increment,
->precio float,
->Id_Producto int,
->primary key(Id_Precio),
->foreign key Id_Producto references Producto(Id_Producto));

create table Stock(
->Id_Stock int auto_increment,
->stock int,
->Id_Producto int,
->primary key(Id_Stock),
->foreign key Id_Producto references Producto(Id_Producto));

insert into Producto(nombre, Id_Categoria, Id_Marca)
->values("Notebook", 1 , 1);

insert into Categoria(nombre)
->values("Tecnológico");

insert into Marca(marca)
->values("Hp");

insert into Precio(precio, Id_Producto)
->values(150000, 1);

insert into Stock(stock, Id_Producto)
->values(24, 1);

insert into Producto(nombre, Id_Categoria, Id_Marca)
->values("Buzo", 2 , 2);

insert into Categoria(nombre)
->values("Vestimenta");

insert into Marca(marca)
->values("Gucci");

insert into Precio(precio, Id_Producto)
->values(17000, 2);

insert into Stock(stock, Id_Producto)
->values(12, 2);

"""

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="Almacen"
)

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children()) # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("select P.Id_Producto, P.nombre, C.nombre as 'categoria', M.Marca, Pr.Precio, S.stock From Producto P inner join Categoria C on C.Id_Categoria = P.Id_Categoria inner join Marca M on M.Id_Marca = P.Id_Marca inner join Precio Pr on Pr.Id_Producto = P.Id_Producto inner join Stock S on S.Id_Producto = P.Id_Producto;")
    for row in cursor.fetchall():
        row = list(row)
        if row[4] == int(row[4]):
            row[4] = "$" + str(int(row[4]))
        else:
            row[4] = "$" + str(row[4])
        row = tuple(row)
        tree.insert("", "end", values=row)
    
def crear_ventana():
    global name_inp,cat_inp,mar_inp,pri_inp,stock_inp,cursor
    ventana = tk.Toplevel(root)
    ventana.title("Agregar datos")
    name_lab = ttk.Label(ventana, text="Nombre").grid(row=0,column=0, pady=20, sticky="E", padx=(0,15))
    name_inp = ttk.Entry(ventana)
    name_inp.grid(row=0,column=1, pady=20, padx=(0,40))

    cat_lab = ttk.Label(ventana, text="Categoria").grid(row=1,column=0, pady=(0,20), sticky="E", padx=(20,15))
    cat_inp = ttk.Entry(ventana)
    cat_inp.grid(row=1,column=1, pady=(0,20), padx=(0,40))

    mar_lab = ttk.Label(ventana, text="Marca").grid(row=2,column=0, pady=(0,20), sticky="E", padx=(0,15))
    mar_inp = ttk.Entry(ventana)
    mar_inp.grid(row=2,column=1, pady=(0,20), padx=(0,40))

    pri_lab = ttk.Label(ventana, text="Precio").grid(row=3,column=0, pady=(0,20), sticky="E", padx=(0,15))
    pri_inp = ttk.Entry(ventana)
    pri_inp.grid(row=3,column=1, pady=(0,20), padx=(0,40))

    stock_lab = ttk.Label(ventana, text="Stock").grid(row=4,column=0, pady=(0,20), sticky="E", padx=(0,15))
    stock_inp = ttk.Entry(ventana)
    stock_inp.grid(row=4,column=1, pady=(0,20), padx=(0,40))

    style_button = ttk.Style()
    style_button.configure("add.TButton", font=("Helvetica", 10))

    add2_button = ttk.Button(ventana, text="Agregar", style="add.TButton")
    add2_button.grid(row=5,column=1, pady=(0,20))
    
"""
AUN NO FUNCIONA BIEN

def agregar_datos():
    global name_inp,cat_inp,mar_inp,pri_inp,stock_inp
    nombre=name_inp.get()
    categoria=cat_inp.get()
    marca=mar_inp.get()
    precio=pri_inp.get()
    stock=stock_inp.get()
    if nombre!="" and categoria!="" and marca!="" and precio!=""and stock!="":
        if precio.isnumeric() and stock.isnumeric():
            cursor = conexion.cursor()

            # Definir los valores que se utilizarán en las consultas SQL
            valores = (nombre, categoria, marca)

            sentencia_sql = [
                "INSERT INTO Producto(nombre) VALUES (%s);",
                "INSERT INTO Categoria(nombre) VALUES (%s);",
                "INSERT INTO Marca(marca) VALUES (%s);"
            ]

            # Ejecutar las consultas SQL con sus respectivos valores
            for i, sentencia in enumerate(sentencia_sql):
                if "nombre" in sentencia:
                    cursor.execute(sentencia, (valores[0],))
                elif "categoria" in sentencia:
                    cursor.execute(sentencia, (valores[1],))
                elif "marca" in sentencia:
                    cursor.execute(sentencia, (valores[2],))
                else:
                    cursor.execute(sentencia)


            cursor.execute("SELECT Id_Producto FROM Producto WHERE nombre = %s;", (nombre,))
            id_producto = cursor.fetchone()[0]  # Obtener el ID del producto

            cursor.execute("SELECT Id_Categoria FROM Categoria WHERE nombre = %s;", (categoria,))
            id_categoria = cursor.fetchone()[0]  # Obtener el ID de la categoría

            cursor.execute("SELECT Id_Marca FROM Marca WHERE marca = %s;", (marca,))
            id_marca = cursor.fetchone()[0]  # Obtener el ID de la marca

            # Definir las consultas SQL con marcadores de posición
            sentencia_sql = [
                "INSERT INTO Precio(precio, Id_Producto) VALUES (%s, %s);",
                "INSERT INTO Stock(stock, Id_Producto) VALUES (%s, %s);",
                "UPDATE Producto SET Id_Categoria=%s WHERE Id_Producto=%s;",
                "UPDATE Producto SET Id_Marca=%s WHERE Id_Producto=%s;"
            ]

            # Ejecutar las consultas SQL con marcadores de posición y valores correspondientes
            for sentencia in sentencia_sql:
                if "Id_Categoria" in sentencia:
                    cursor.execute(sentencia, (id_categoria, id_producto))
                elif "Id_Marca" in sentencia:
                    cursor.execute(sentencia, (id_marca, id_producto))
                elif "Precio" in sentencia:
                    cursor.execute(sentencia, (float(precio), id_producto))
                elif "Stock" in sentencia:
                    cursor.execute(sentencia, (int(stock), id_producto))

            conexion.commit()

            messagebox.showerror("Exito!", "Datos agregados correctamente.")

        else:
            messagebox.showerror("Error", "Por favor, ingrese datos validos.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
"""

def eliminar_fila():
    cursor = conexion.cursor()
    seleccion = tree.selection()

    if seleccion:
        # Obtener el ID de la fila seleccionada
        id_seleccionado = tree.item(seleccion, "values")[0]

        # Desactivar las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

        # Eliminar los registros relacionados en las tablas "Precio" y "Stock"
        sentencia_sql = [
            "DELETE FROM Precio WHERE Id_Producto = %s;",
            "DELETE FROM Stock WHERE Id_Producto = %s;",
        ]
        for sentencia in sentencia_sql:
            cursor.execute(sentencia, (id_seleccionado,))
            
        conexion.commit()

        # Reactivar las restricciones de clave externa
        cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

        # Eliminar la fila de la tabla "Producto," "Categoria," y "Marca"
        sentencia_sql = [
            "DELETE FROM Producto WHERE Id_Producto = %s;",
            "DELETE FROM Categoria WHERE Id_Categoria = %s;",
            "DELETE FROM Marca WHERE Id_Marca = %s;"
        ]

        for sentencia in sentencia_sql:
            cursor.execute(sentencia, (id_seleccionado,))

        conexion.commit()

        # Eliminar la fila del TreeView
        tree.delete(seleccion)

# Crear ventana
root = tk.Tk()
root.title("Consulta de Productos")
root.config(bg="Black")
style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 12), background="red")
style.configure('Treeview', font=("Helvetica", 12), background="#3549C1", foreground="White")
style.configure('TButton', font=("Helvetica", 12), background="white")
style.map("Treeview", background=[('selected', 'red')])



f1 = tk.Frame(root, width=50, bg=root.cget("bg"))
f1.grid(row=0,column=0)

f2 = ttk.Frame(root)
f2.grid(row=0,column=1)

f3 = tk.Frame(root, width=50, bg=root.cget("bg"))
f3.grid(row=0,column=2)

f4 = tk.Frame(root, height=50,bg=root.cget("bg"))
f4.grid(row=1,column=0, columnspan=3)

# Crear Treeview para mostrar la información
tree = ttk.Treeview(f2, columns=("ID", "Nombre", "Categoria", "Marca", "Precio", "Stock"))

tree['show'] = 'headings'
tree.heading("#1", text="ID")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Categoria")

tree.heading("#4", text="Marca")
tree.heading("#5", text="Precio")
tree.heading("#6", text="Stock")

tree.column("#1", anchor="center")
tree.column("#2", anchor="center")
tree.column("#3", anchor="center")
tree.column("#4", anchor="center")
tree.column("#5", anchor="center")
tree.column("#6", anchor="center")
tree.grid(row=0, column=1)

# Botón para cargar datos
consulta_button = ttk.Button(f4, text="Consultar",command=cargar_datos)
consulta_button.grid(row=0, column=0)

add_button = ttk.Button(f4, text="Agregar", command=lambda:crear_ventana())
add_button.grid(row=0, column=1, padx=40, pady=20)

sub_button = ttk.Button(f4, text="Eliminar", command=lambda:eliminar_fila())
sub_button.grid(row=0, column=2)

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()