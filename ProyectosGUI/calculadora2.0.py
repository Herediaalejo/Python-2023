from tkinter import *
from tkinter import ttk
import random

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculadora 2.0")
        self.window.resizable(0,0)
        self.window.geometry("450x250")
        self.createWidgets()
        self.window.mainloop()

    def validNum(self, num):
        try:
            num = int(num)
            return num
        except:
            try:
                num = float(num)
                return num
            except:
                return ('Error')
            
    def calculate(self, op):
        try:
            self.input_resultado.config(state= NORMAL)
            self.input_resultado.delete(0, END)
            if op == 1:
                self.input_resultado.insert(0,self.validNum(self.input_valor_uno.get()) + self.validNum(self.input_valor_dos.get()))
            elif op == 2:
                self.input_resultado.insert(0,self.validNum(self.input_valor_uno.get()) - self.validNum(self.input_valor_dos.get()))
            elif op == 3:
                self.input_resultado.insert(0,self.validNum(self.input_valor_uno.get()) * self.validNum(self.input_valor_dos.get()))
            elif op == 4:
                self.input_resultado.insert(0,self.validNum(self.input_valor_uno.get()) / self.validNum(self.input_valor_dos.get()))
            self.input_resultado.config(state='readonly')
        except:
            self.input_resultado.insert(0,'Error')


    def clear(self):
        self.input_resultado.config(state= NORMAL)
        self.input_resultado.delete(0, END)
        self.input_valor_uno.delete(0, END)
        self.input_valor_dos.delete(0,END)
        self.input_resultado.config(state='readonly')
        self.input_valor_uno.focus()

            

    def createWidgets(self):
        self.label_valor_uno = ttk.Label(self.window, text="Valor 1").grid(row=1,column=0, pady = 30, padx = 10, sticky=E)
        self.label_valor_dos = ttk.Label(self.window, text="Valor 2").grid(row=2,column=0, sticky=E, padx = 10)
        self.label_result = ttk.Label(self.window, text="Resultado").grid(row=3,column=0, pady = 30, padx= 10, sticky=E)
        self.label_oper = ttk.Label(self.window,text="Operaciones").grid(row=0,column=2, padx=30, sticky=S)
        self.input_valor_uno = ttk.Entry(self.window)
        self.input_valor_uno.focus()
        self.input_valor_uno.grid(row=1, column=1)
        self.input_valor_dos = ttk.Entry(self.window)
        self.input_valor_dos.grid(row=2,column=1)
        self.input_resultado = ttk.Entry(self.window, state="readonly")
        self.input_resultado.grid(row=3,column=1)
        self.opcion = IntVar()
        self.opcion.set(1)
        self.rbutton_sum = ttk.Radiobutton(self.window, text ="Sumar", value=1, variable=self.opcion).grid(row=1,column=2,sticky=W, padx=40)
        self.rbutton_sub = ttk.Radiobutton(self.window, text ="Restar", value=2, variable=self.opcion).grid(row=2,column=2,sticky=W, padx=40)
        self.rbutton_mult = ttk.Radiobutton(self.window, text ="Multiplicar", value=3, variable=self.opcion).grid(row=3,column=2,sticky=W, padx=40)
        self.rbutton_div = ttk.Radiobutton(self.window, text ="Dividir", value=4, variable=self.opcion).grid(row=4,column=2,sticky=W, padx=40)
        self.button_calculate = ttk.Button(self.window, text="Calcular", command=lambda:self.calculate(self.opcion.get())).grid(row=4,column=1, sticky=W)
        self.button_clear = ttk.Button(self.window, text="Limpiar", command=lambda:self.clear()).grid(row=4,column=1, sticky=E)


def run():
    calculadora = Aplicacion()

if __name__ == "__main__":
    run()