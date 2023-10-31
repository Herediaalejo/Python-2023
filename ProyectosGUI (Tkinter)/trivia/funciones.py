import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector
import time
from PIL import Image, ImageTk 
import random
from main import run

def conectar():
    global conexion
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="trivia")
    

def crear_celda(ventana, row, column, width, color ,height=30):
    celda = tk.Frame(ventana, width=width,height=height, bg=color)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30), padx=20)
    return celda

tarea_programada_reloj = None

def actualizar_reloj(ventana, label):
    current_time = time.strftime("%H:%M")  # Obtiene la hora actual en formato HH:MM:SS
    label.config(text=current_time)
    # Programa la siguiente llamada y guarda el identificador
    global tarea_programada_reloj
    tarea_programada_reloj = ventana.after(1000, lambda: actualizar_reloj(ventana, label))

# Función para detener el reloj
def detener_reloj(ventana):
    global tarea_programada_reloj
    if tarea_programada_reloj:
        ventana.after_cancel(tarea_programada_reloj)
        tarea_programada_reloj = None# Programa la actualización cada segundo (1000 ms)

def actualizar_cronometro(ventana, label):
    global tiempo_transcurrido
    tiempo_actual = time.strftime("%M:%S", time.gmtime(tiempo_transcurrido))
    label.config(text=tiempo_actual)
    tiempo_transcurrido += 1
    global tarea_programada_cronometro
    tarea_programada_cronometro = ventana.after(1000, lambda: actualizar_cronometro(ventana, label))

# Función para detener el cronómetro
def detener_cronometro(ventana):
    global tarea_programada_cronometro
    if tarea_programada_cronometro:
        ventana.after_cancel(tarea_programada_cronometro)
        tarea_programada_cronometro = None

def cargar_imagen(name_imagen):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Combina el directorio actual con el nombre de la imagen
    ruta_imagen = os.path.join(directorio_actual, name_imagen)

    # Abre una imagen
    imagen = Image.open(ruta_imagen)

    # Convierte la imagen a un formato compatible con tkinter
    imagen = ImageTk.PhotoImage(imagen)
    return imagen


# Función para reiniciar el contador de tiempo
def reiniciar_tiempo(label):
    global tiempo_transcurrido
    tiempo_transcurrido = 0
    label.config(text="00:00")

def min_to_sec(tiempo):
  minutos, segundos = tiempo.split(":")
  minutos = int(minutos)
  segundos = int(segundos)

  segundos = minutos * 60 + segundos

  return segundos

def sec_to_min(segundos):

  minutos = segundos // 60 #division entera, devuelve numero entero
  segundos_restantes = segundos % 60 #el resto de la division
  minutos = int(minutos)
  segundos_restantes = int(segundos_restantes)

  tiempo = f"{minutos:02}:{segundos_restantes:02}" #02 hace que el numero se vea con dos digitos por mas que tenga uno solo, es decir agrega un 0 a la izquierda cuando hay tan solo un caracter

  return tiempo

# Función para cargar y mostrar información en el Treeview
def cargar_jugadores(tree):
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT NOMBRE, TIEMPO, PUNTAJE FROM JUGADOR")
    datos = cursor.fetchall()
    jugadores = []
    for jugador in datos:
        jugadores.append(list(jugador))

    jugadores.sort(key=lambda jugador: (-jugador[2], jugador[1])) #Ordena los jugadores primero por puntaje poniendo el mas alto primero, luego por tiempo poniendo el mas bajo primero

    for i in range(len(jugadores)):
        jugadores[i][1] = sec_to_min(jugadores[i][1])
    for row in jugadores:
        tree.insert("", "end", values=row)
    cursor.close()

def cargar_preguntas():
    cursor = conexion.cursor()
    cursor.execute("SELECT ID_PREGUNTA, NOMBRE, RESPUESTA_CORRECTA, RESPUESTA_INCORRECTA1, RESPUESTA_INCORRECTA2, RESPUESTA_INCORRECTA3 FROM PREGUNTA")
    preguntas = cursor.fetchall()
    cursor.close()
    return preguntas

def guardar_jugador():
    cursor = conexion.cursor()
    tiempo = min_to_sec(tiempo_logrado)
    cursor.execute("INSERT INTO JUGADOR (NOMBRE, INSTAGRAM, TELEFONO, PUNTAJE, TIEMPO) values (%s,%s,%s,%s,%s)", (nombre, instagram, telefono, puntaje, tiempo))
    conexion.commit()
    cursor.close()

def seleccionar_pregunta(listaPreguntas):
    if not listaPreguntas:
        return None

    fila_elegida = random.choice(listaPreguntas)
    pregunta = fila_elegida[1]
    respuestaCor = fila_elegida[2]
    respuestaInc1 = fila_elegida[3]
    respuestaInc2 = fila_elegida[4]
    respuestaInc3 = fila_elegida[5]
    listaPreguntas.remove(fila_elegida)
    return pregunta, respuestaCor, respuestaInc1, respuestaInc2, respuestaInc3

def insertar_salto_de_linea(texto, limite):
    if len(texto) <= limite:
        return texto  # No es necesario un salto de línea, el texto es lo suficientemente corto

    palabras = texto.split()  # Dividir el texto en palabras
    conteo_caracteres = 0
    indice_ultima_palabra = 0

    for i, palabra in enumerate(palabras):
        conteo_caracteres += len(palabra) + 1  # +1 para contar el espacio en blanco
        if conteo_caracteres > limite:
            palabras[indice_ultima_palabra] += '\n'  # Agregar el salto de línea a la última palabra
            conteo_caracteres = len(palabra)  # Reiniciar el conteo con la longitud de la palabra actual
        else:
            indice_ultima_palabra = i

    return ' '.join(palabras)

def sumar_puntos():
    global puntaje, totalAcertado
    puntaje+=100
    totalAcertado +=1

def nueva_pregunta(window, totalPreguntas, listaPreguntas):
    pregunta_seleccionada = seleccionar_pregunta(listaPreguntas)
    if pregunta_seleccionada:
        rojo = "#f54254"
        azul = "#4287f5"
        verde = "#42f57b"
        amarillo = "#f5e342"
        button_color = [rojo, azul, verde, amarillo]
        random.shuffle(button_color)
        #fila, columna, padx(primervalor), padx(segundovalor)
        button_grid = [(9,1,0,50),(9,2,50,0),(12,1,0,50),(12,2,50,0)]
        random.shuffle(button_grid)
        # Actualizamos el contenido de la ventana actual
        pregunta = insertar_salto_de_linea(pregunta_seleccionada[0], 40)
        respuestaCor = insertar_salto_de_linea(pregunta_seleccionada[1], 22)
        respuestaInc1 = insertar_salto_de_linea(pregunta_seleccionada[2], 22)
        respuestaInc2 = insertar_salto_de_linea(pregunta_seleccionada[3], 22)
        respuestaInc3 = insertar_salto_de_linea(pregunta_seleccionada[4], 22)
        preguntaLabel.config(text=pregunta)
        opcion1.config(text=respuestaCor, background=button_color[0])
        opcion2.config(text=respuestaInc1, background=button_color[1])
        opcion3.config(text=respuestaInc2, background=button_color[2])
        opcion4.config(text=respuestaInc3, background=button_color[3])
        opcion1.grid(row=button_grid[0][0], column=button_grid[0][1], sticky="nsew", padx=(button_grid[0][2],button_grid[0][3]))
        opcion2.grid(row=button_grid[1][0], column=button_grid[1][1], sticky="nsew", padx=(button_grid[1][2],button_grid[1][3]))
        opcion3.grid(row=button_grid[2][0], column=button_grid[2][1], sticky="nsew", padx=(button_grid[2][2],button_grid[2][3]))
        opcion4.grid(row=button_grid[3][0], column=button_grid[3][1], sticky="nsew", padx=(button_grid[3][2],button_grid[3][3]))
        puntaje_label.config(text=f"Puntaje: {puntaje}")
    
    else:
        fin_juego(window, totalPreguntas)

def eliminar_widgets(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def empezar_juego(window,name_entry, ig_entry, tel_entry):
    global nombre, telefono, instagram, tiempo_transcurrido, puntaje, totalAcertado
    conectar()
    detener_reloj(window)
    nombre = name_entry.get()
    nombre = nombre.title()
    instagram = ig_entry.get()
    telefono = tel_entry.get()
    tiempo_transcurrido = 0
    totalAcertado = 0
    puntaje = 0
    listaPreguntas = cargar_preguntas()
    totalPreguntas = len(listaPreguntas)
    if len(instagram) == 0:
        instagram=None
    if len(telefono) == 0:
        telefono=None
    if nombre:
        if len(nombre)>=3 and len(nombre)<=20:
            #Verifico si alguno de los caracteres de nombre es un número
            nombre_valido = not any(c.isdigit() for c in nombre)
        else:
            messagebox.showwarning("Error", "El nombre debe tener entre 3 y 20 caractéres.")
            return
    else:
        messagebox.showwarning("Error", "Debe ingresar un nombre")
        return

    if nombre_valido:
        crear_juego(window, totalPreguntas, listaPreguntas)
    else:
        messagebox.showwarning("Error", "El nombre no puede contener números")
        return

def mostrar_respuesta(window, op, totalPreguntas, listaPreguntas):
    opcion1.grid_forget()
    opcion2.grid_forget()
    opcion3.grid_forget()
    opcion4.grid_forget()

    respuesta_label.grid(row=6,column=1,columnspan=2, rowspan=8)
    if op == 1:
        respuesta_label.config(image=check, bg="#4a4949") 
    elif op == 2:
        respuesta_label.config(image=nocheck, bg="#4a4949")
    
    window.after(1000, lambda: [respuesta_label.grid_forget(), nueva_pregunta(window, totalPreguntas, listaPreguntas)])


def fin_juego(window, totalPreguntas):
    global tiempo_logrado
    detener_cronometro(window)
    screen_width = window.winfo_screenwidth()
    bgcolor = "#3cc985"
    tiempo_logrado = time_label.cget('text')
    reiniciar_tiempo(time_label)
    eliminar_widgets(window)
    window.config(bg=bgcolor)
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor)

    fin_label = tk.Label(window, text=f"Felicidades {nombre}! Finalizaste el juego.", font=(font,60), bg="white")
    fin_label.grid(row=3,column=0,columnspan=4)

    preguntasT_label = tk.Label(window, font=(font,40), text=f"Contestaste correctamente {totalAcertado} de {totalPreguntas} preguntas", bg="white")
    preguntasT_label.grid(row=5,column=0,columnspan=4)

    punt_label = tk.Label(window, text=f"Tu puntaje fue: {puntaje}", font=(font,40), bg="white")
    punt_label.grid(row=6,column=0,columnspan=4)

    tiempoT_label = tk.Label(window, text=f"Tu tiempo fue de: {tiempo_logrado}", font=(font,40), bg="white")
    tiempoT_label.grid(row=7,column=0,columnspan=4)

    regresar_button = tk.Button(window, text="REGRESAR", cursor="hand2", bg="#eb6781", font=(font,20), relief="flat", command=lambda:[run(window)])
    regresar_button.grid(row=12,column=0,columnspan=4, ipadx=10, ipady=10)

    guardar_jugador()

def ver_datos(window):
    data_window = tk.Toplevel(window, bg="#536363")
    data_window.geometry("1200x600")
    data_window.resizable(0,0)
    user_tree = ttk.Treeview(data_window, columns=("Nombre", "Tiempo", "Puntaje", "Teléfono", "Instagram"), style="Custom.Treeview")
    user_tree.grid(row=0, column=0, padx=100)
    data_window.columnconfigure(0, weight=1)  # Expande la columna 0
    data_window.rowconfigure(0, weight=1)  # Expande la fila 0
    data_window.rowconfigure(1, weight=1)  # Expande la fila 1


    user_tree.column("#0", width=0, stretch=tk.NO)
    user_tree.heading("#1", text="Nombre")
    user_tree.heading("#2", text="Tiempo")
    user_tree.heading("#3", text="Puntaje")
    user_tree.heading("#4", text="Teléfono")
    user_tree.heading("#5", text="Instagram")

    user_tree.column("#1", anchor="center")
    user_tree.column("#2", anchor="center")
    user_tree.column("#3", anchor="center")
    user_tree.column("#4", anchor="center")
    user_tree.column("#5", anchor="center")

    user_tree.delete(*user_tree.get_children())  # Borrar datos existentes en el Treeview
    
    cursor = conexion.cursor()
    cursor.execute("SELECT NOMBRE, TIEMPO, PUNTAJE, TELEFONO, INSTAGRAM FROM JUGADOR")
    datos = cursor.fetchall()
    jugadores = []
    for jugador in datos:
        jugadores.append(list(jugador))

    jugadores.sort(key=lambda jugador: (-jugador[2], jugador[1])) #Ordena los jugadores primero por puntaje poniendo el mas alto primero, luego por tiempo poniendo el mas bajo primero

    for i in range(len(jugadores)):
        jugadores[i][1] = sec_to_min(jugadores[i][1])
    for row in jugadores:
        user_tree.insert("", "end", values=row)
    cursor.close()

    user_tree.bind("<Button-1>", lambda event: user_tree.selection_remove(user_tree.selection()) if user_tree.selection() else None)

    regresar_button = tk.Button(data_window, width=8, text="SALIR", cursor="hand2", bg="#eb6781", font=(font,20), relief="flat", command=lambda:[data_window.destroy()])
    regresar_button.grid(row=1,column=0) 



def crear_juego(window, totalPreguntas, listaPreguntas):
    global font, time_label, preguntaLabel, opcion1, opcion2, opcion3, opcion4, user_label, puntaje_label, respuesta_label, check, nocheck

    font = "Gill Sans MT"

    check = cargar_imagen("check.jpg")
    nocheck = cargar_imagen("nocheck.jpg")

    screen_width = window.winfo_screenwidth()

    bgcolor = "#4a4949"

    eliminar_widgets(window)
    
    window.config(bg=bgcolor)
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor)

    user_frame = tk.Frame(window, bg="orange")
    user_frame.grid(row=1,column=0,sticky="nsew", rowspan=4, padx=(30,80), pady=25)
    user_frame.columnconfigure(0, weight=1)  # Expande la columna 0
    user_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    user_frame.rowconfigure(1, weight=1)  # Expande la fila 1

    user_label = tk.Label(user_frame, font=(font, 20), text=f"Jugador: {insertar_salto_de_linea(nombre,13)}", bg="orange")
    user_label.grid(row=0, column=0, sticky="w", padx=(10,0))

    puntaje_label = tk.Label(user_frame, font=(font, 20), bg="orange")
    puntaje_label.grid(row=1, column=0, sticky="w", padx=(10,0))

    time_frame = tk.Frame(window, bg="#4a4949")
    time_frame.grid(row=1,column=3,sticky="nsew", rowspan=4)
    time_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    time_frame.columnconfigure(0, weight=1)  # Expande la columna 0

    time_label = tk.Label(time_frame, text="00:00", font=(font, 60), bg="orange")
    time_label.grid(column=0, row=0)

    actualizar_cronometro(window, time_label)

    pregunta_frame = tk.Frame(window, background="white")
    pregunta_frame.grid(row=1,column=1, columnspan=2,rowspan=4, sticky="nsew")
    pregunta_frame.grid_rowconfigure(0, weight=1)  # Expande la fila 0
    pregunta_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    pregunta_frame.columnconfigure(0, weight=1)  # Expande la columna 0
    preguntaLabel = tk.Label(pregunta_frame, background="white", font=(font, 30))
    preguntaLabel.grid(row=0,column=0, sticky="nsew")
    opcion1 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[sumar_puntos(), mostrar_respuesta(window,1, totalPreguntas, listaPreguntas)])
    opcion2 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[mostrar_respuesta(window,2, totalPreguntas, listaPreguntas)])
    opcion3 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[ mostrar_respuesta(window,2, totalPreguntas, listaPreguntas)])
    opcion4= tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[ mostrar_respuesta(window,2, totalPreguntas, listaPreguntas)])
    
    respuesta_label = tk.Label(window, font=(font, 80))  

    exitP_button = tk.Button(window, width=20, text="SALIR",bg="#eb6781",cursor="hand2",font=(font, 16), relief="flat", command=lambda:[detener_cronometro(window),reiniciar_tiempo(time_label),run(window)])
    exitP_button.grid(row=15,column=0, rowspan=2)

    nueva_pregunta(window, totalPreguntas, listaPreguntas)



tarea_programada_cronometro = None
