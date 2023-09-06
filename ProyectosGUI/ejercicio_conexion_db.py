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
database="Almacen",
port=3306
)

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT P.CodProducto, P.nombre, M.nombre, C.nombre, P.precio, P.stock FROM Producto P INNER JOIN Categoria C ON P.CodCategoria = C.CodCategoria INNER JOIN Marca M ON P.CodMarca = M.CodMarca;")
    for row in cursor.fetchall():
        row = list(row)
        if row[4] == int(row[4]):
            row[4] = "$" + str(int(row[4]))
        else:
            row[4] = "$" + str(row[4])
        row = tuple(row)
        tree.insert("", "end", values=row)
    # cerrar el cursor después de usarlo
    cursor.close()
    
def crear_ventana():
    global name_inp,cat_inp,mar_inp,pri_inp,stock_inp,ventana
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

    add2_button = ttk.Button(ventana, text="Agregar", style="add.TButton", command=lambda:agregar_datos())
    add2_button.grid(row=5,column=1, pady=(0,20))
    


def agregar_datos():
    global name_inp, cat_inp, mar_inp, pri_inp, stock_inp, ventana
    cursor = conexion.cursor()
    nombre = name_inp.get()
    categoria = cat_inp.get()
    marca = mar_inp.get()
    precio = pri_inp.get()
    stock = stock_inp.get()
    
    if nombre != "" and categoria != "" and marca != "" and precio != "" and stock != "":
        if precio.isnumeric() and stock.isnumeric():
            try:
                sentencia_sql = [
                    "INSERT INTO Producto(nombre, precio, stock) VALUES (%s, %s, %s);",
                    "INSERT INTO Categoria(nombre) VALUES (%s);",
                    "INSERT INTO Marca(nombre) VALUES (%s);"
                ]
    
                # Ejecutar las consultas SQL con sus respectivos valores
                for sentencia in sentencia_sql:
                    if "Producto" in sentencia:
                        cursor.execute(sentencia, (nombre, float(precio), int(stock)))
                    elif "Categoria" in sentencia:
                        cursor.execute(sentencia, (categoria,))
                    elif "Marca" in sentencia:
                        cursor.execute(sentencia, (marca,))
                    else:
                        cursor.execute(sentencia)
                
                conexion.commit()
    
                # Obtener los IDs después de la inserción
                cursor.execute("SELECT CodProducto FROM Producto WHERE nombre = %s;", (nombre,))
                CodProducto = cursor.fetchone()[0]
    
                cursor.execute("SELECT CodCategoria FROM Categoria WHERE nombre = %s;", (categoria,))
                CodCategoria = cursor.fetchone()[0]
    
                cursor.execute("SELECT CodMarca FROM Marca WHERE nombre = %s;", (marca,))
                CodMarca = cursor.fetchone()[0]
    
                # Definir las consultas SQL con marcadores de posición
                sentencia_sql = [
                    "UPDATE Producto SET CodCategoria=%s WHERE CodProducto=%s;",
                    "UPDATE Producto SET CodMarca=%s WHERE CodProducto=%s;"
                ]
    
                # Ejecutar las consultas SQL con marcadores de posición y valores correspondientes
                for sentencia in sentencia_sql:
                    if "CodCategoria" in sentencia:
                        cursor.execute(sentencia, (CodCategoria, CodProducto))
                    elif "CodMarca" in sentencia:
                        cursor.execute(sentencia, (CodMarca, CodProducto))


                conexion.commit()
    
                messagebox.showinfo("Éxito", "Datos agregados correctamente.")

                ventana.destroy()
    
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos.")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
    cursor.close()



def eliminar_fila():
    cursor = conexion.cursor()
    seleccion = tree.selection()

    if seleccion:
        # Obtener el ID de la fila seleccionada
        codproducto = tree.item(seleccion, "values")[0]

        # Eliminar la fila de la tabla "Producto," "Categoria," y "Marca"
        sentencia_sql = [
            "DELETE FROM Producto WHERE CodProducto = %s;"
        ]

        for sentencia in sentencia_sql:
            if "Producto" in sentencia:
                cursor.execute(sentencia, (codproducto,))


        conexion.commit()
        cursor.close()

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
tree = ttk.Treeview(f2, columns=("ID", "Nombre", "Marca", "Categoria", "Precio", "Stock"))

tree['show'] = 'headings'
tree.heading("#1", text="ID")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="Marca")
tree.heading("#4", text="Categoria")
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