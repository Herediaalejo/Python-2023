from tkinter import *
from tkinter import ttk
import random

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Desafio para valientes")
        self.window.resizable(0,0)
        self.window.geometry("400x330")
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
            
    def calculate(self, difficult, op):
        try:
            self.numero_uno_inp.config(state= NORMAL)
            self.numero_uno_inp.delete(0, END)
            self.numero_dos_inp.config(state= NORMAL)
            self.numero_dos_inp.delete(0, END)
            if difficult == 1 and op != 0:
                self.numero_uno_inp.insert(0, random.randint(0,10))
                self.numero_dos_inp.insert(0,random.randint(0,10))
            elif difficult == 2 and op != 0:
                self.numero_uno_inp.insert(0,random.randint(0,100))
                self.numero_dos_inp.insert(0,random.randint(0,100))
            elif difficult == 3 and op != 0:
                self.numero_uno_inp.insert(0,random.randint(0,1000))
                self.numero_dos_inp.insert(0,random.randint(0,1000))
            self.numero_uno_inp.config(state= "readonly")
            self.numero_dos_inp.config(state= "readonly")
        except:
            return("Error")
        
    def clear(self):
        self.input_resultado.config(state= NORMAL)
        self.input_resultado.delete(0, END)
        self.input_valor_uno.delete(0, END)
        self.input_valor_dos.delete(0,END)
        self.input_resultado.config(state='readonly')
        self.input_valor_uno.focus()
    
    def verify_result(self):
        try:
            self.operation = self.numero_uno_inp.get() + self.sign[0] + self.numero_dos_inp.get()
            print(self.operation)
            result_pc = eval(self.operation)
            result_user = self.validNum(self.resultado_inp.get())
            if result_pc == result_user:
                self.games+=1
                self.wins+=1
                self.games_lab.config(text=f"Juegos :      {self.games}")
                self.wins_lab.config(text=f"Ganados :      {self.wins}")
                self.numero_uno_inp.config(state=NORMAL)
                self.numero_dos_inp.config(state=NORMAL)
                self.numero_uno_inp.delete(0,END)
                self.numero_dos_inp.delete(0,END)
                self.numero_uno_inp.config(state="readonly")
                self.numero_dos_inp.config(state="readonly")
                self.resultado_but.config(state=DISABLED)
            else:
                self.games+=1
                self.loses+=1
                self.games_lab.config(text=f"Juegos :      {self.games}")
                self.loses_lab.config(text=f"Perdidos :      {self.loses}")
            self.resultado_inp.delete(0,END)
        except:
            pass




    def createWidgets(self):
        self.sign=["?"]
        self.calculo=IntVar()
        self.difficult = IntVar()
        self.numero_uno_inp=ttk.Entry(self.window, width=15, state="readonly", justify=RIGHT)
        self.numero_uno_inp.grid(row=0, column=0, pady=15, padx=(15,15))
        self.sign_lab=ttk.Label(self.window, text=f"{self.sign[0]}")
        self.sign_lab.grid(row=0,column=1)
        self.numero_dos_inp=ttk.Entry(self.window, width=15, state="readonly")
        self.numero_dos_inp.grid(row=0, column=2, padx=(15,0))
        self.num_new_but=ttk.Button(self.window, text="Nuevo número", command=lambda:[self.calculate(self.difficult.get(), self.calculo.get()), self.resultado_inp.focus(), self.resultado_inp.delete(0,END), self.resultado_but.config(state=NORMAL)])
        self.num_new_but.grid(row=1,column=3, padx=(15,0), ipadx=10)

        self.rbutton_sum = ttk.Radiobutton(self.window, text ="Sumar", value=1, variable=self.calculo, command=lambda:[self.sign_lab.config(text="+"), self.sign.pop(0), self.sign.append("+")]).grid(row=2,column=0,sticky=W, padx=(40,0), pady=(0,10))
        
        self.rbutton_sub = ttk.Radiobutton(self.window, text ="Restar", value=2, variable=self.calculo, command=lambda:[self.sign_lab.config(text="-"), self.sign.pop(0), self.sign.append("-")]).grid(row=3,column=0,sticky=W, padx=(40,0), pady=(0,10))
        
        self.rbutton_mult = ttk.Radiobutton(self.window, text ="Multiplicar", value=3, variable=self.calculo, command=lambda:[self.sign_lab.config(text="*"), self.sign.pop(0), self.sign.append("*")]).grid(row=4,column=0,sticky=W, padx=(40,0), pady=(0,10))
        
        self.rbutton_div = ttk.Radiobutton(self.window, text ="Dividir", value=4, variable=self.calculo, command=lambda:[self.sign_lab.config(text="/"), self.sign.pop(0), self.sign.append("/")]).grid(row=5,column=0,sticky=NW, padx=(40,0))

        self.rbutton_easy = ttk.Radiobutton(self.window, value=1, text ="Facil", variable=self.difficult)
        self.rbutton_easy.grid(row=3,column=2, sticky=E, padx=(0,15))
        self.rbutton_medium = ttk.Radiobutton(self.window, text ="Medio", value=2, variable=self.difficult)
        self.rbutton_medium.grid(row=3,column=3, sticky=W)
        self.rbutton_hard = ttk.Radiobutton(self.window, text ="Dificil", value=3, variable=self.difficult)
        self.rbutton_hard.grid(row=3,column=3, sticky=E)
        self.resultado_inp = ttk.Entry(self.window)
        self.resultado_inp.grid(row=4,column=3)
        self.games=0
        self.wins=0
        self.loses=0
        self.resultado_but = ttk.Button(self.window, text="Resultado", state=DISABLED,command=lambda:[self.verify_result()])
        self.resultado_but.grid(row=5,column=3, pady=(10,0))
        self.games_lab = ttk.Label(self.window, text="Juegos :      ")
        self.games_lab.grid(row=6,column=3, sticky=W, pady=(20,0), padx=(20,0))
        self.wins_lab = ttk.Label(self.window, text="Ganados :   ")
        self.wins_lab.grid(row=7,column=3, sticky=W, pady=(10,0), padx=(20,0))
        self.loses_lab = ttk.Label(self.window, text="Perdidos :   ")
        self.loses_lab.grid(row=8,column=3, sticky=W, pady=(10,0), padx=(20,0))
        
        


def run():
    calculadora = Aplicacion()

if __name__ == "__main__":
    run()