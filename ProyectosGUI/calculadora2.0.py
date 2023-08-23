from tkinter import *
from tkinter import ttk
import random

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora 2.0")
        self.window.resizable(0,0)
        self.window.geometry("350x250")
        self.createWidgets()
        self.window.mainloop()

    def createWidgets(self):
        label_valor_uno = ttk.Label(self.window, text="Valor 1").grid(row=1,column=0, pady = 30, padx = 10, sticky=E)
        label_valor_dos = ttk.Label(self.window, text="Valor 2").grid(row=2,column=0, sticky=E, padx = 10)
        label_result = ttk.Label(self.window, text="Resultado").grid(row=3,column=0, pady = 30, padx= 10, sticky=E)
        label_oper = ttk.Label(self.window,text="Operaciones").grid(row=0,column=2, padx=30, sticky=W)
        input_valor_uno = ttk.Entry(self.window)
        input_valor_uno.grid(row=1, column=1)
        input_valor_dos = ttk.Entry(self.window)
        input_valor_dos.grid(row=2,column=1)
        input_resultado = ttk.Entry(self.window)
        input_resultado.grid(row=3,column=1)
        rbutton_sum = ttk.Radiobutton(self.window, text ="Sumar", value=1).grid(row=1,column=2,sticky=W, padx=40)
        rbutton_sub = ttk.Radiobutton(self.window, text ="Restar", value=2).grid(row=2,column=2,sticky=W, padx=40)
        rbutton_mult = ttk.Radiobutton(self.window, text ="Multiplicar", value=3).grid(row=3,column=2,sticky=W, padx=40)
        rbutton_div = ttk.Radiobutton(self.window, text ="Dividir", value=4).grid(row=4,column=2,sticky=W, padx=40)
        button_calculate = ttk.Button(self.window, text="Calcular").grid(row=4,column=1)

def run():
    calculadora = Aplicacion()

if __name__ == "__main__":
    run()