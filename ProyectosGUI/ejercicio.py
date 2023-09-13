import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost", user="root", password="estudiantes2020", database="escuela")

# Función para cargar y mostrar información en el Treeview
def cargar_datos():
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT Alumnos.NOMBRE, Alumnos.APELLIDO, Alumnos.DNI, Carreras.NOMBRE, EstadoAlumno.nombre FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN EstadoAlumno ON Alumnos.IDESTADOALUMNO = EstadoAlumno.IDESTADOALUMNO")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Función para obtener las carreras desde la base de datos y cargarlas en el ComboBox
def cargar_carreras_estados():
    cursor = conexion.cursor()
    cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    cursor.execute("SELECT IDESTADOALUMNO, NOMBRE FROM ESTADOALUMNO")
    estados = cursor.fetchall()
    carrera_combobox['values'] = [row[1] for row in carreras]
    estado_combobox['values'] = [row[1] for row in estados]
    return carreras, estados  # Devolver también la lista de carreras con sus IDs

def cargar_alumno():
    cursor = conexion.cursor()
    cursor.execute("SELECT DNI FROM ALUMNOS")
    alumnos = cursor.fetchall()  # Devolver también la lista de carreras con sus IDs
    return alumnos

# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = dni_entry.get()
    carrera_nombre = carrera_combobox.get()
    estado_nombre = estado_combobox.get()
    flag = 0

    if nombre and apellido and dni and carrera_nombre:
        # Obtener el ID de la carrera seleccionada
        carreras, estados = cargar_carreras_estados()
        carrera_id = None
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break
        for estado in estados:
            if estado[1] == estado_nombre:
                estado_id = estado[0]
                break
        alumnos = cargar_alumno()
        for dni in alumnos:
            if dni == dni_entry.get():
                cursor = conexion.cursor()
                cursor.execute("UPDATE ALUMNO SET NOMBRE = %s SET APELLIDO = %s SET DNI = %s SET IDCARRERA = %s SET IDESTADOALUMNO =%s", (nombre, apellido, dni, carrera_id, estado_id))
                cursor.commit()
                flag = 1
                break              
        if flag == 0:
            cursor = conexion.cursor()
            # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO
            cursor.execute("INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, IDCARRERA, IDESTADOALUMNO) VALUES (%s, %s, %s, %s, %s);", (nombre, apellido, dni, carrera_id, estado_id))
            conexion.commit()
            cargar_datos()  # Actualizar la vista
            # Limpiar los campos después de insertar
            nombre_entry.delete(0, tk.END)
            apellido_entry.delete(0, tk.END)
            dni_entry.delete(0, tk.END)
            carrera_combobox.set("")  # Limpiar la selección del ComboBox
            estado_combobox.set("")  # Limpiar la selección del ComboBox
    else:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")


def modificar_alumno():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")  # Limpiar la selección del ComboBox
    estado_combobox.set("")  # Limpiar la selección del ComboBox
    cursor = conexion.cursor()
    seleccion = tree.selection()
    if seleccion:
        nombre = tree.item(seleccion, "values")[0]
        apellido = tree.item(seleccion, "values")[1]
        dni = tree.item(seleccion, "values")[2]
        carrera_nombre = tree.item(seleccion, "values")[3]
        estado_nombre = tree.item(seleccion, "values")[4]
        if nombre and apellido and dni and carrera_nombre:
            # Obtener el ID de la carrera seleccionada
            carreras, estados = cargar_carreras_estados()
            carrera_id = None
            for carrera in carreras:
                if carrera[1] == carrera_nombre:
                    carrera_id = carrera[0]
                    break
            for estado in estados:
                if estado[1] == estado_nombre:
                    estado_id = estado[0]
                    break
        nombre_entry.insert(0, nombre)
        apellido_entry.insert(0, apellido)
        dni_entry.insert(0, dni)
        carrera_combobox.set(carrera_nombre)
        estado_combobox.set(estado_nombre)
    
        

# Crear ventana
root = tk.Tk()
root.title("Consulta de Alumnos")

# Crear un frame con un borde visible para el formulario de inscripción
formulario_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
formulario_frame.pack(padx=10, pady=10)

# Título del formulario
titulo_label = tk.Label(formulario_frame, text="Formulario Inscripción", font=("Helvetica", 14))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campos de entrada para nombre, apellido y DNI con el mismo ancho que el ComboBox
nombre_label = tk.Label(formulario_frame, text="Nombre:")
nombre_label.grid(row=1, column=0)
nombre_entry = tk.Entry(formulario_frame)
nombre_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

apellido_label = tk.Label(formulario_frame, text="Apellido:")
apellido_label.grid(row=2, column=0)
apellido_entry = tk.Entry(formulario_frame)
apellido_entry.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

dni_label = tk.Label(formulario_frame, text="DNI:")
dni_label.grid(row=3, column=0)
dni_entry = tk.Entry(formulario_frame)
dni_entry.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Combo box para la carrera
carrera_label = tk.Label(formulario_frame, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_combobox = ttk.Combobox(formulario_frame,  state="readonly")# Configurar el ComboBox como de solo lectura
carrera_combobox.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

estado_label = tk.Label(formulario_frame, text="Estado:")
estado_label.grid(row=5, column=0)
estado_combobox = ttk.Combobox(formulario_frame,  state="readonly")# Configurar el ComboBox como de solo lectura
estado_combobox.grid(row=5, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

# Cargar las carreras al inicio de la aplicación y obtener la lista de carreras con sus IDs
carreras = cargar_carreras_estados()

# Botón para guardar un nuevo registro de alumno
guardar_button = ttk.Button(formulario_frame, text="Guardar", command=guardar_alumno)
guardar_button.grid(row=6, columnspan=2, pady=10, sticky="ew")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=("Nombre", "Apellido", "DNI", "Carrera", "Estado"))
tree.heading("#1", text="Nombre")
tree.heading("#2", text="Apellido")
tree.heading("#3", text="DNI")
tree.heading("#4", text="Carrera")
tree.heading("#5", text="Estado")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.column("#1", anchor="center")
tree.column("#2", anchor="center")
tree.column("#3", anchor="center")
tree.column("#4", anchor="center")
tree.column("#5", anchor="center")
tree.pack(padx=10, pady=10)

# Botón para cargar datos
cargar_button = ttk.Button(root, text="Cargar Datos", command=cargar_datos)
cargar_button.pack(pady=5)

modificar_button = ttk.Button(root,text="Modificar", command=modificar_alumno)
modificar_button.pack(pady=(0,10))

# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()