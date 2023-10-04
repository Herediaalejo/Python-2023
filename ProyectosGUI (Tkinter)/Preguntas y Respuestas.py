import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def crear_celda(ventana, row, column, width=100, height=30):
    celda = tk.Frame(ventana, width=width,height=height, bg=bgcolor)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30))
    return celda

root = tk.Tk()
root.title("Trivia")
root.attributes('-fullscreen', not root.attributes('-fullscreen'))
root.resizable(0,0)

bgcolor = "#BCFFCC"
frcolor = "#ADDAFF"

for row in range(4):
    for column in range(2):
        crear_celda(root, row, column)

estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 40)) 



root.config(bg="white")
# Iniciar el bucle principal de tkinter

title = ttk.Label(text="TRIVIAUI", background=bgcolor)
title.grid(row=0,column=0)
tk.mainloop()
