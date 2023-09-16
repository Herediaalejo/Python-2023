import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(host="localhost", user="root", password="", database="escuela")

# Función para cargar y mostrar información en el Treeview
def cargar_datos(op=0):
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT NOMBRE FROM ESTADOALUMNO")
    estados = cursor.fetchall()
    cursor.execute("SELECT NOMBRE FROM Carreras ORDER BY NOMBRE")
    carreras = cursor.fetchall()
    filtro = filtros_combobox.get()
    es_carrera = any(filtro in tupla for tupla in carreras)
    es_estado = any(filtro in tupla for tupla in estados)
    limpiar_button.config(state="normal")
    
    if op == 0:
        filtros_combobox.set("")
        filtrar_button.config(state="disabled")
        cursor.execute("SELECT Alumnos.APELLIDO, Alumnos.NOMBRE, Alumnos.DNI, Carreras.NOMBRE, EstadoAlumno.nombre FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN EstadoAlumno ON Alumnos.IDESTADOALUMNO = EstadoAlumno.IDESTADOALUMNO ORDER BY APELLIDO;")
    elif op == 1:

        if es_estado:
            cursor.execute("SELECT IDESTADOALUMNO FROM ESTADOALUMNO WHERE ESTADOALUMNO.NOMBRE = %s", (filtro,))
            idfiltro = cursor.fetchall()[0][0]
            cursor.execute("SELECT Alumnos.APELLIDO, Alumnos.NOMBRE, Alumnos.DNI, Carreras.NOMBRE, EstadoAlumno.nombre FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN EstadoAlumno ON Alumnos.IDESTADOALUMNO = EstadoAlumno.IDESTADOALUMNO WHERE ALUMNOS.IDESTADOALUMNO = %s ORDER BY APELLIDO;", (idfiltro,))
        
        elif es_carrera:
            cursor.execute("SELECT IDCARRERA FROM CARRERAS WHERE CARRERAS.NOMBRE = %s", (filtro,))
            idfiltro = cursor.fetchall()[0][0]
            cursor.execute("SELECT Alumnos.APELLIDO, Alumnos.NOMBRE, Alumnos.DNI, Carreras.NOMBRE, EstadoAlumno.nombre FROM Alumnos JOIN Carreras ON Alumnos.IDCARRERA = Carreras.IDCARRERA JOIN EstadoAlumno ON Alumnos.IDESTADOALUMNO = EstadoAlumno.IDESTADOALUMNO WHERE ALUMNOS.IDCARRERA = %s ORDER BY APELLIDO;", (idfiltro,))

    else:
        return
    
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
    cursor.execute("SELECT IDALUMNO, NOMBRE FROM ALUMNOS;")
    alumnos = cursor.fetchall()  # Devolver también la lista de carreras con sus IDs
    return alumnos

# Función para mostrar una ventana de alerta
def mostrar_alerta(mensaje):
    messagebox.showwarning("Alerta", mensaje)

# Función para guardar un nuevo registro de alumno
def guardar_alumno():
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = validar_dni(dni_entry.get())
    carrera_nombre = carrera_combobox.get()
    estado_nombre = estado_combobox.get()

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
        cursor = conexion.cursor()
        # Insertar un nuevo registro en la tabla Alumnos con el ID de carrera y el valor predeterminado para IDESTADOALUMNO
        cursor.execute("INSERT INTO Alumnos (NOMBRE, APELLIDO, DNI, IDCARRERA, IDESTADOALUMNO) VALUES (%s, %s, %s, %s, %s);", (nombre, apellido, dni, carrera_id, estado_id))
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        messagebox.showinfo("Exito!", "El alumno ha sido guardado con exito.")
        # Limpiar los campos después de insertar
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        estado_combobox.set("")  # Limpiar la selección del ComboBox
        guardar_button.config(state="disabled")

    elif dni != False:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

def validar_dni(dni):
    if "." in dni:
        dni = dni.replace(".", "")
    if len(dni) == 8:
        for caracter in dni:
            if caracter.isalpha():
                mostrar_alerta("El dni no puede contener letras.")
                return False
        return dni
    else:
        mostrar_alerta("El dni debe poseer 8 caracteres (sin contar puntos).")
        return False


alumno_id = None

def modificar_alumno():
    global alumno_id
    guardar_button.config(state="disabled")
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("")  # Limpiar la selección del ComboBox
    estado_combobox.set("")  # Limpiar la selección del ComboBox
    cursor = conexion.cursor()
    seleccion = tree.selection()
    if seleccion:
        apellido = tree.item(seleccion, "values")[0]
        nombre = tree.item(seleccion, "values")[1]
        dni = tree.item(seleccion, "values")[2]
        carrera_nombre = tree.item(seleccion, "values")[3]
        estado_nombre = tree.item(seleccion, "values")[4]
        alumnos = cargar_alumno()
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
        for alumno in alumnos:
            if alumno[1] == nombre:
                alumno_id = alumno[0]
                break
        nombre_entry.insert(0, nombre)
        apellido_entry.insert(0, apellido)
        dni_entry.insert(0, dni)
        carrera_combobox.set(carrera_nombre)
        estado_combobox.set(estado_nombre)
        guardar_button.config(text="Modificar", command=actualizar_alumno)
        tree.selection_remove(tree.selection())
        modificar_button.config(state="disabled")


def actualizar_alumno():
    global alumno_id
    nombre = nombre_entry.get().upper()
    apellido = apellido_entry.get().upper()
    dni = validar_dni(dni_entry.get())
    carrera_nombre = carrera_combobox.get()
    estado_nombre = estado_combobox.get()
    # Obtener el ID de la carrera y el estado
    carreras, estados = cargar_carreras_estados()
    carrera_id = None
    if nombre and apellido and dni and carrera_nombre and estado_nombre:
        for carrera in carreras:
            if carrera[1] == carrera_nombre:
                carrera_id = carrera[0]
                break
        for estado in estados:
            if estado[1] == estado_nombre:
                estado_id = estado[0]
                break   
        cursor = conexion.cursor()
        cursor.execute("UPDATE ALUMNOS SET NOMBRE = %s, APELLIDO = %s, DNI = %s, IDCARRERA = %s, IDESTADOALUMNO =%s WHERE IDALUMNO=%s;", (nombre, apellido, dni, carrera_id, estado_id, alumno_id))
        conexion.commit()
        cargar_datos()  # Actualizar la vista
        # Limpiar los campos después de insertar
        messagebox.showinfo("Exito", "El alumno ha sido modificado con exito.")
        nombre_entry.delete(0, tk.END)
        apellido_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        carrera_combobox.set("")  # Limpiar la selección del ComboBox
        estado_combobox.set("")  # Limpiar la selección del ComboBox
        guardar_button.config(text="Guardar", command=guardar_alumno)
        guardar_button.config(state="disabled")
        
    elif dni != False:
        mostrar_alerta("Los campos son obligatorios. Debe completarlos.")

def eliminar_alumno():
    cursor = conexion.cursor()
    seleccion = tree.selection()
    dni = tree.item(seleccion, "values")[2]
    respuesta = messagebox.askyesno("Confirmación", f"¿Seguro que deseas eliminar al alumno '{tree.item(seleccion, 'values')[0]} {tree.item(seleccion, 'values')[1]}'?")
    if respuesta:
        cursor.execute("DELETE FROM ALUMNOS WHERE ALUMNOS.DNI=%s",(dni,))
        conexion.commit()
        cargar_datos()
        messagebox.showinfo("Exito!", "El alumno ha sido eliminado con exito.")
    else:
        return
    
def limpiar_pantalla():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    dni_entry.delete(0, tk.END)
    carrera_combobox.set("") 
    estado_combobox.set("")  
    filtros_combobox.set("")
    tree.delete(*tree.get_children()) 
    guardar_button.config(text="Guardar", command=guardar_alumno)
    guardar_button.config(state="disabled")
    limpiar_button.config(state="disabled")
    filtrar_button.config(state="disabled")

def verificar_contenido(event):
    contenido = event.widget.get()
    if contenido:
        guardar_button.config(state="normal")
        limpiar_button.config(state="normal")  # Habilita el botón si hay contenido en el Entry
    else:
        limpiar_button.config(state="disabled")  # Deshabilita el botón si no hay elementos ni contenido
        guardar_button.config(state="disabled")

def verificar_filtro(event):
    contenido = event.widget.get()
    if contenido:
        limpiar_button.config(state="normal")  # Habilita el botón si hay contenido en el Entry
    else:
        limpiar_button.config(state="disabled")  # Deshabilita el botón si no hay elementos ni contenido

# Crear ventana
root = tk.Tk()
root.title("Consulta de Alumnos")
root.resizable(0,0)

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
guardar_button.config(state="disabled")

# Crear Treeview para mostrar la información
tree = ttk.Treeview(root, columns=( "Apellido","Nombre", "DNI", "Carrera", "Estado"))
tree.heading("#1", text="Apellido")
tree.heading("#2", text="Nombre")
tree.heading("#3", text="DNI")
tree.heading("#4", text="Carrera")
tree.heading("#5", text="Estado")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar la columna #0 que habitualmente muestra las primary key de los objetos
tree.column("#1", anchor="center", width=200)
tree.column("#2", anchor="center", width=200)
tree.column("#3", anchor="center", width=200)
tree.column("#4", anchor="center", width=200)
tree.column("#5", anchor="center", width=200)
tree.pack(padx=10, pady=10)

tree.bind("<Button-1>", lambda event: tree.selection_remove(tree.selection()) if tree.selection() else None)

# Función para crear una celda vacía con borde
def crear_celda(ventana, row, column):
    celda = tk.Frame(ventana, width=100,height=30)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30))
    return celda

footer = tk.Frame(root)
footer.pack(fill="both", expand=True, padx=10)


for column in range(10):
    crear_celda(footer, 0, column)


modificar_button = ttk.Button(footer,text="Modificar", command=modificar_alumno)
modificar_button.grid(row=0, column=3)
modificar_button.config(state="disabled")

# Botón para cargar datos
cargar_button = ttk.Button(footer, width=30,text="Cargar Alumnos (Todos)", command=cargar_datos)
cargar_button.grid(row=0, column=4, columnspan=2)

filtros_lab = ttk.Label(footer,text="Filtros")
filtros_lab.grid(row=0, column=6, padx=(0,10), sticky="E")

filtros_combobox = ttk.Combobox(footer, width=30,state="readonly")
filtros_combobox.grid(row=0, column=7, columnspan=2)

filtrar_button = ttk.Button(footer, text="Filtrar", command=lambda:cargar_datos(1))
filtrar_button.config(state="disabled")
filtrar_button.grid(row=0,column=9)

eliminar_button = ttk.Button(footer, text="Eliminar", command=eliminar_alumno)
eliminar_button.config(state="disabled")
eliminar_button.grid(row=0,column=2)

limpiar_button = ttk.Button(footer, text="Limpiar pantalla", command=limpiar_pantalla)
limpiar_button.config(state="disabled")
limpiar_button.grid(row=0,column=1, padx=(0,15))

tree.bind("<<TreeviewSelect>>", lambda event:(modificar_button.config(state="normal"), eliminar_button.config(state="normal")) if tree.selection() else (modificar_button.config(state="disabled"), eliminar_button.config(state="disabled")))

cursor = conexion.cursor()
cursor.execute("SELECT IDESTADOALUMNO, NOMBRE FROM ESTADOALUMNO")
estados = cursor.fetchall()

# Obtener los datos de las carreras
cursor.execute("SELECT IDCARRERA, NOMBRE FROM Carreras ORDER BY NOMBRE")
carreras = cursor.fetchall()

# Crear una lista combinada de estados y carreras
valores_combinados = [row[1] for row in estados] + [row[1] for row in carreras]

# Configurar los valores del Combobox
filtros_combobox['values'] = valores_combinados

filtros_combobox.bind("<<ComboboxSelected>>", lambda event: (filtrar_button.config(state="normal"), verificar_filtro(event)))

nombre_entry.bind("<KeyRelease>", verificar_contenido)
apellido_entry.bind("<KeyRelease>", verificar_contenido)
dni_entry.bind("<KeyRelease>", verificar_contenido)
carrera_combobox.bind("<<ComboboxSelected>>", lambda event: verificar_contenido(event))
estado_combobox.bind("<<ComboboxSelected>>", lambda event: verificar_contenido(event))



# Ejecutar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
conexion.close()