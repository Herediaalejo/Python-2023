import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector
import time
import random
from PIL import Image, ImageTk

conexion = mysql.connector.connect(
host="localhost",
user="root",
password="estudiantes2020",
database="trivia",
port=3306
)

#pip install pillow

def crear_celda(ventana, row, column, width, color ,height=30):
    celda = tk.Frame(ventana, width=width,height=height, bg=color)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30), padx=20)
    return celda

def update_clock():
    current_time = time.strftime("%H:%M")  # Obtiene la hora actual en formato HH:MM:SS
    clock_label.config(text=current_time)      # Actualiza el texto del label
    root.after(1000, update_clock)            # Programa la actualización cada segundo (1000 ms)

def getQuestion():
    cursor = conexion.cursor()
    cursor.execute("SELECT ID_PREGUNTA, PREGUNTA, RESPUESTA FROM PREGUNTAS")
    cantidad = 0
    listaPreguntas = []
    for row in cursor.fetchall():
        listaPreguntas.append(row)
    fila_elegida = random.choice(listaPreguntas)
    pregunta = fila_elegida[1]
    respuesta = fila_elegida[2]
    return pregunta, respuesta


def create_window():
    window = tk.Toplevel(root)
    window.title("Pregunta")
    window.attributes('-fullscreen', True)
    colors = ["red", "orange", "blue", "yellow", "purple"]
    bgcolor_pregunta = random.choice(colors)
    window.config(bg=bgcolor_pregunta)
    pregunta, respuesta = getQuestion()
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor_pregunta)
    preguntaLabel = tk.Label(window, text=pregunta, background=bgcolor_pregunta, font=(font, 30))
    preguntaLabel.grid(row=1,column=1, columnspan=2,rowspan=4)
    opcion1 = tk.Button(window, width=50, bg="black", relief="flat")
    opcion1.grid(row=7, column=1, sticky="nsew", padx=(0,50))
    opcion2 = tk.Button(window, width=50, bg="black", relief="flat")
    opcion2.grid(row=7, column=2, sticky="nsew", padx=(50,0))
    opcion3 = tk.Button(window, width=50, bg="black", relief="flat")
    opcion3.grid(row=10, column=1, sticky="nsew", padx=(0,50))
    opcion4= tk.Button(window, width=50, bg="black", relief="flat")
    opcion4.grid(row=10, column=2, sticky="nsew", padx=(50,0))



root = tk.Tk()
root.title("Trivia")

# Maximiza la ventana para que cubra toda la pantalla
root.attributes('-fullscreen', True)
root.resizable(0, 0)
screen_width = root.winfo_screenwidth()

bgcolor = "#BCFFCC"
frcolor = "#ADDAFF"
font = "Gill Sans MT"


for row in range(18):
    for column in range(4):
        crear_celda(root, row, column, (screen_width-180)/4, bgcolor)


estilo = ttk.Style()
estilo.configure("TLabel", font=(font, 30)) 
estilo.configure("TEntry", font=(font, 20)) 
estilo.configure("Custom.TLabel", font=(font,20))


root.config(bg=bgcolor)
# Iniciar el bucle principal de tkinter

clock_label = tk.Label(root, font=(font, 32), bg=bgcolor)
clock_label.grid(row=14,column=3, sticky="e")

update_clock()  # Inicia la actualización

# Obtén la ruta del directorio actual donde se encuentra tu archivo .py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Combina el directorio actual con el nombre de la imagen
ruta_imagen = os.path.join(directorio_actual, "isaui.jpg")

# Abre una imagen
image = Image.open(ruta_imagen)

# Convierte la imagen a un formato compatible con tkinter
photo = ImageTk.PhotoImage(image)

logo = tk.Label(root, image=photo, background=bgcolor)
logo.grid(row=0,column=0,sticky="w", rowspan=2)

title = ttk.Label(text="TRIVIAUI ", background=bgcolor)
title.grid(row=0,column=0, columnspan=2, rowspan=2)

description = ttk.Label(text="EL JUEGO DE PREGUNTAS Y RESPUESTAS DE LOS 40 AÑOS DEL ISAUI.",style="Custom.TLabel", background=bgcolor)
description.grid(row=14,column=0, columnspan=4, sticky="w", padx=(10,0))

name_label = ttk.Label(text="NOMBRE *", background=bgcolor, font=(font, 20))
name_label.grid(row=2, column=0, columnspan=2, rowspan=2)

name_entry = ttk.Entry(width=25, font=(font, 16))
name_entry.grid(row=3,column=0, columnspan=2, rowspan=2)

ig_label = ttk.Label(text="INSTAGRAM", background=bgcolor, font=(font, 20))
ig_label.grid(row=4, column=0, columnspan=2, rowspan=2)

ig_entry = ttk.Entry(width=25, font=(font, 16))
ig_entry.grid(row=5,column=0, columnspan=2, rowspan=2)

tel_label = ttk.Label(text="TELEFONO", background=bgcolor, font=(font, 20))
tel_label.grid(row=6, column=0, columnspan=2, rowspan=2)

tel_entry = ttk.Entry(width=25, font=(font, 16))
tel_entry.grid(row=7,column=0, columnspan=2, rowspan=2)

newGame_button = tk.Button(root, width=20, text="NUEVO JUEGO", bg="#5bd0f0",cursor="hand2",font=(font, 16), relief="flat", command=lambda:create_window())
newGame_button.grid(row=9,column=0, columnspan=2, rowspan=2, sticky="n")

exit_button = tk.Button(root, width=20, text="SALIR",bg="#eb6781",cursor="hand2",font=(font, 16), relief="flat", command=lambda:root.destroy())
exit_button.grid(row=10,column=0, columnspan=2, rowspan=2)

punt_label = ttk.Label(root, text="PUNTAJES", background=bgcolor)
punt_label.grid(row=1, column=2, columnspan=2, rowspan=2)

data_button = tk.Button(root, width=10, text="DATOS", bg="#be77ed",cursor="hand2",font=(font, 16), relief="flat")
data_button.grid(row=9,column=2, columnspan=2, rowspan=2)

tree_style = ttk.Style()
tree_style.configure("Custom.Treeview.Heading", font=(font, 12))  # Cambia la fuente de los headings
tree_style.configure("Custom.Treeview", font=(font, 10))  # Cambia la fuente de los datos de la grilla

punt_tree = ttk.Treeview(root, columns=("Nombre", "Tiempo", "Puntaje"), style="Custom.Treeview")
punt_tree.grid(row=3, column=2, columnspan=2, rowspan=6, sticky="nsew")

punt_tree.column("#0", width=0, stretch=tk.NO)
punt_tree.heading("#1", text="Nombre")
punt_tree.heading("#2", text="Tiempo")
punt_tree.heading("#3", text="Puntaje")

tk.mainloop()


"""
create database trivia;

use trivia;

create table Jugador(
ID_JUGADOR int auto_increment primary key,
NOMBRE VARCHAR(255) NOT NULL,
INSTAGRAM varchar(255),
TELEFONO varchar(255),
PUNTAJE INT NOT NULL,
TIEMPO DOUBLE NOT NULL
);

create table Preguntas(
ID_PREGUNTA INT auto_increment primary key,
PREGUNTA VARCHAR (255) NOT NULL,
RESPUESTA VARCHAR (255) NOT NULL
);

"""
