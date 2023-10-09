import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def crear_celda(ventana, row, column, width, height=30):
    celda = tk.Frame(ventana, width=width,height=height, bg=bgcolor)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30), padx=20)
    return celda

root = tk.Tk()
root.title("Trivia")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.resizable(0, 0)
screen_width = root.winfo_screenwidth()

bgcolor = "#BCFFCC"
frcolor = "#ADDAFF"

for row in range(18):
    for column in range(4):
        crear_celda(root, row, column, (screen_width-180)/4)

estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 30)) 
estilo.configure("TEntry", font=("Arial", 20)) 
estilo.configure('newGame.TButton', font=('Helvetica', 16))


root.config(bg="white")
# Iniciar el bucle principal de tkinter

title = ttk.Label(text="TRIVIAUI", background=bgcolor)
title.grid(row=0,column=0, columnspan=2, rowspan=2)

name_label = ttk.Label(text="NOMBRE *", background=bgcolor, font=("Arial", 20))
name_label.grid(row=3, column=0, columnspan=2, rowspan=2)

name_entry = ttk.Entry(width=30, font=("Arial", 16))
name_entry.grid(row=4,column=0, columnspan=2, rowspan=2)

ig_label = ttk.Label(text="INSTAGRAM", background=bgcolor, font=("Arial", 20))
ig_label.grid(row=5, column=0, columnspan=2, rowspan=2)

ig_entry = ttk.Entry(width=30, font=("Arial", 16))
ig_entry.grid(row=6,column=0, columnspan=2, rowspan=2)

tel_label = ttk.Label(text="TELEFONO", background=bgcolor, font=("Arial", 20))
tel_label.grid(row=7, column=0, columnspan=2, rowspan=2)

tel_entry = ttk.Entry(width=30, font=("Arial", 16))
tel_entry.grid(row=8,column=0, columnspan=2, rowspan=2)

newGame_button = ttk.Button(root, width=20, text="NUEVO JUEGO", style='newGame.TButton')
newGame_button.grid(row=9,column=0, columnspan=2, rowspan=2)

punt_label = ttk.Label(root, text="PUNTAJE", background=bgcolor)
punt_label.grid(row=0, column=2, columnspan=2, rowspan=2)

punt_tree = ttk.Treeview(root)
punt_tree.grid(row=2, column=2, columnspan=2, rowspan=6)

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
