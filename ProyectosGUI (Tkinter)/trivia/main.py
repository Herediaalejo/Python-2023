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
    f.conectar()
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

    tel_label = ttk.Label(text="TELÉFONO", background="lightblue", font=(font, 20))
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