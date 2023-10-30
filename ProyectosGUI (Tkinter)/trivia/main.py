import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector
import time
from PIL import Image, ImageTk 
import random
import funciones as f


def run(window):
    font = "Gill Sans MT"

    f.eliminar_widgets(window)
    screen_width = window.winfo_screenwidth()

    bgcolor = "#BCFFCC"
    frcolor = "#ADDAFF"

    for row in range(18):
        for column in range(4):
            f.crear_celda(window, row, column, (screen_width-180)/4, bgcolor)
    
    for i in range(18):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)

    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("TLabel", font=(font, 30)) 
    estilo.configure("TEntry", font=(font, 20)) 
    estilo.configure("Custom.TLabel", font=(font,20))
    estilo.configure("Title.TLabel", font=(font,45))

    window.columnconfigure(0, weight=1)  # Expande la primera columna
    window.columnconfigure(1, weight=1)  # Expande la segunda columna
    window.columnconfigure(2, weight=1)  # Expande la tercera columna
    window.columnconfigure(3, weight=1)  # Expande la cuarta columna

    window.config(bg=bgcolor)
    # Iniciar el bucle principal de tkinter

    clock_label = tk.Label(window, font=(font, 32), bg=bgcolor)
    clock_label.grid(row=17,column=3, sticky="e")

    f.actualizar_reloj(window, clock_label)  # Inicia la actualización

    icon = f.cargar_imagen("logo-isaui.jpg")

    logo = tk.Label(window, image=icon, background=bgcolor)
    logo.grid(row=0,column=0,sticky="w", rowspan=2, pady=(10,0), padx=(10,0))

    title = ttk.Label(text="TRIVIAUI ", background=bgcolor, style="Title.TLabel")
    title.grid(row=0,column=0, columnspan=2, rowspan=3, padx=(100,0), sticky="s", pady=(0,10))

    description = ttk.Label(text="EL JUEGO DE PREGUNTAS Y RESPUESTAS DE LOS 40 AÑOS DEL ISAUI.",style="Custom.TLabel", background=bgcolor)
    description.grid(row=17,column=0, columnspan=4, sticky="w", padx=(10,0))

    form = tk.Frame(window, bg="lightblue", width=450)
    form.grid(row=3,column=0,columnspan=2, rowspan=13, sticky="ns", padx=(100,0))

    name_label = ttk.Label(text="NOMBRE *", background="lightblue", font=(font, 20))
    name_label.grid(row=4, column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    name_entry = ttk.Entry(width=25, font=(font, 16))
    name_entry.grid(row=5,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    ig_label = ttk.Label(text="INSTAGRAM", background="lightblue", font=(font, 20))
    ig_label.grid(row=6, column=0, columnspan=2, rowspan=2, padx=(100,0))

    ig_entry = ttk.Entry(width=25, font=(font, 16))
    ig_entry.grid(row=7,column=0, columnspan=2, rowspan=2, padx=(100,0))

    tel_label = ttk.Label(text="TELEFONO", background="lightblue", font=(font, 20))
    tel_label.grid(row=8, column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    tel_entry = ttk.Entry(width=25, font=(font, 16))
    tel_entry.grid(row=9,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    newGame_button = tk.Button(window, width=20, text="NUEVO JUEGO", bg="#5bd0f0",cursor="hand2",font=(font, 16), relief="flat", command=lambda:[f.empezar_juego(window, name_entry, ig_entry, tel_entry)])
    newGame_button.grid(row=12,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    exit_button = tk.Button(window, width=20, text="SALIR",bg="#eb6781",cursor="hand2",font=(font, 16), relief="flat", command=lambda:window.destroy())
    exit_button.grid(row=13,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    punt_label = ttk.Label(window, text="PUNTAJES", background=bgcolor)
    punt_label.grid(row=1, column=2, columnspan=2, rowspan=2)

    data_button = tk.Button(window, width=10, text="DATOS", bg="#c389f5",cursor="hand2",font=(font, 16), relief="flat", command=lambda:f.ver_datos(window))
    data_button.grid(row=9,column=2, columnspan=2, rowspan=2)

    tree_style = ttk.Style()

    tree_style.configure("Custom.Treeview.Heading", font=(font, 16), background="#fcb34c", margin=(5, 5))  # Cambia la fuente de los headings
    tree_style.configure("Custom.Treeview", font=(font, 16), background="", fieldbackground="#e8eb91", rowheight=30, foreground="black")  # Cambia la fuente de los datos de la grilla
    tree_style.map("Custom.Treeview", background=[("selected", "brown")])

    punt_tree = ttk.Treeview(window, columns=("Nombre", "Tiempo", "Puntaje"), style="Custom.Treeview")
    punt_tree.grid(row=3, column=2, columnspan=2, rowspan=6, sticky="nsew")

    punt_tree.column("#0", width=0, stretch=tk.NO)
    punt_tree.heading("#1", text="Nombre")
    punt_tree.heading("#2", text="Tiempo")
    punt_tree.heading("#3", text="Puntaje")

    punt_tree.column("#1", anchor="center")
    punt_tree.column("#2", anchor="center")
    punt_tree.column("#3", anchor="center")

    punt_tree.bind("<Button-1>", lambda event: punt_tree.selection_remove(punt_tree.selection()) if punt_tree.selection() else None)
      
    f.cargar_jugadores(punt_tree)

    window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Trivia")
    window.attributes('-fullscreen', True)
    window.resizable(0, 0)
    run(window)


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

create table Pregunta(
ID_PREGUNTA INT auto_increment primary key,
NOMBRE VARCHAR (255) NOT NULL,
RESPUESTA_CORRECTA VARCHAR (255) NOT NULL,
RESPUESTA_INCORRECTA1 VARCHAR(255) NOT NULL,
RESPUESTA_INCORRECTA2 VARCHAR(255) NOT NULL,
RESPUESTA_INCORRECTA3 VARCHAR(255) NOT NULL
);

INSERT INTO pregunta(NOMBRE, RESPUESTA_CORRECTA, RESPUESTA_INCORRECTA1, RESPUESTA_INCORRECTA2, RESPUESTA_INCORRECTA3) VALUES 
("¿En qué año se fundó el instituto?", "1983", "1987", "1993", "1980"), 
("¿Cuál fue el nombre del establecimiento educativo cuando se fundó?", "Complejo Facultativo de Enseñanza Superior San Francisco de Asís", "Instituto Educativo Superior Cura Brochero", "Instituto Superior Arturo Umberto Illia", "Escuela Mayor Facultativa Raúl Alfonsin"), 
("¿Cómo se llamaban los fundadores?", "Raúl", "Eduardo", "Claudio", "Graciela"), 
("¿En qué año se convierte en colegio nacional?", "1985", "1989", "1995", "2001"), 
("¿Cuántos directores tuvo el Instituto hasta la fecha?", "4", "7", "9", "12"), 
("¿Cuántas carreras se dictan actualmente en el ISAUI?", "6", "4", "9", "11"), 
("¿Cuál fue el primer número de teléfono del Instituto?", "41164", "52314", "34245", "79845"), 
("¿Qué es el workshop?", "Una técnica de venta", "Un lugar donde comprar cosas", "Una carrera", "Un estilo de vida"), 
("¿Qué carrera fue la pionera con los viajes en las materias de prácticas?", "Técnico y Guía Superior en Turismo", "Tecnicatura en Desarrollo de Software", "Diseño de Espacios", "Trekking"), 
("¿Cómo era el edificio educativo en sus comienzos?", "Una casa con 3 ambientes", "Una cafetería con 2 ambientes", "Una casa con tan solo 1 ambiente", "Una panadería de 5 ambientes"), 
("¿Qué tipo de instituto es el ISAUI?", "Instituto Público", "Instituto Privado", "Instituto Semi-privado", "Instituto Semi-público"), 
("¿A partir de qué año la cooperadora empezó a construir las aulas?", "1986", "1981", "1992", "2001"), 
("¿De dónde provenía el dinero?", "Del bono contribución de los padres", "Del bono contribución de los profesores", "Del gobierno nacional", "Del gobierno provincial"), 
("¿Quién fue el presidente de la cooperadora en el inicio de la institución?", "Sr. Gatica", "Sra. Graciela", "Sr. Augusto", "Carlos"), 
("¿Quién es la presidenta de la cooperadora actualmente?", "Daniela Maschio", "Gabriela Roldan", "Agustina Aperlo", "Elizabeth Afazani"), 
("¿Cómo se logró la nacionalización?", "Mediante la gestión del diputado Anselmo Pelaez", "Mediante la ayuda del gobernador Schiaretti", "Mediante el acuerdo con la UEPC", "Mediante la reunión de las escuelas de Carlos Paz");
"""
