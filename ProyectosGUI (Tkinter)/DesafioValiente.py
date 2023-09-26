from tkinter import *
from tkinter import ttk
from tkinter import font
import random


class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("El juego de los números")
        self.window.resizable(0,0)
        self.window.geometry("550x350")
        self.window.config(bg="#82C7FF")
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

    def random_signAbut(self):
        self.signs = ["+","-","*","/"]
        self.sign_choosed = random.choice(self.signs)
        self.sign_lab.config(text=self.sign_choosed)
        self.rbutton_sum.config(state=NORMAL)
        self.rbutton_sub.config(state=NORMAL)
        self.rbutton_mult.config(state=NORMAL)
        self.rbutton_div.config(state=NORMAL)
        self.calculo.set(random.randint(1,4))
        self.sign.pop(0) 
        self.sign.append(self.sign_choosed)
        self.rbutton_sum.config(state=DISABLED)
        self.rbutton_sub.config(state=DISABLED)
        self.rbutton_mult.config(state=DISABLED)
        self.rbutton_div.config(state=DISABLED)

    def verify_result(self):
        try:
            self.operation = self.numero_uno_inp.get() + self.sign[0] + self.numero_dos_inp.get()
            result_pc = eval(self.operation)
            result_user = self.validNum(self.resultado_inp.get())
            if result_pc == result_user:
                self.games[0]+=1
                self.wins[0]+=1
                self.games_lab.config(text=f"Juegos :      {self.games[0]}")
                self.wins_lab.config(text=f"Ganados :      {self.wins[0]}")
                self.numero_uno_inp.config(state=NORMAL)
                self.numero_dos_inp.config(state=NORMAL)
                self.numero_uno_inp.delete(0,END)
                self.numero_dos_inp.delete(0,END)
                self.numero_uno_inp.config(state="readonly")
                self.numero_dos_inp.config(state="readonly")
                self.resultado_but.config(state=DISABLED)
            else:
                self.games[0]+=1
                self.loses[0]+=1
                self.games_lab.config(text=f"Juegos :      {self.games[0]}")
                self.loses_lab.config(text=f"Perdidos :      {self.loses[0]}")
            self.resultado_inp.delete(0,END)
        except:
            pass
    
    def clear_all(self):
        self.numero_uno_inp.config(state= NORMAL)
        self.numero_uno_inp.delete(0, END)
        self.numero_dos_inp.config(state= NORMAL)
        self.numero_dos_inp.delete(0, END)
        self.numero_uno_inp.config(state="readonly")
        self.numero_dos_inp.config(state="readonly")
        self.resultado_inp.delete(0,END)
    
    def clear_gwl(self):
        self.wins.pop(0)
        self.wins.append(0)
        self.games.pop(0)
        self.games.append(0)
        self.loses.pop(0)
        self.loses.append(0)


    def createWidgets(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe UI', 12), background="#82C7FF")
        self.style.configure('TButton', font=('Segoe UI', 12), background="#82C7FF")
        self.style.configure('TEntry', font=('Segoe UI', 20), background="#82C7FF")
        self.style.configure('TRadiobutton', font=('Segoe UI', 12, "bold"), background="#82C7FF")
        self.sign=["?"]
        self.calculo=IntVar()
        self.difficult = IntVar()
        self.numero_uno_inp=ttk.Entry(self.window, state="readonly", justify=RIGHT, font=(18), width=10)
        self.numero_uno_inp.grid(row=0, column=0, pady=15, padx=(15,15))
        self.sign_lab=ttk.Label(self.window, text=f"{self.sign[0]}")
        self.sign_lab.grid(row=0,column=1, padx=(0,10))
        self.numero_dos_inp=ttk.Entry(self.window, state="readonly", font=(18), width=10)
        self.numero_dos_inp.grid(row=0, column=2, padx=(15,40))
        self.eq_lab=ttk.Label(self.window, text="=")
        self.eq_lab.grid(row=0,column=2, sticky=E, padx=(0,5))

        self.num_new_but=ttk.Button(self.window, cursor="hand2",text="Nuevo juego", state=DISABLED,command=lambda:[self.random_signAbut(),self.calculate(self.difficult.get(), self.calculo.get()), self.resultado_inp.focus(), self.resultado_inp.delete(0,END), self.resultado_but.config(state=NORMAL), self.num_new_but.config(text="Nuevo número"), self.resultado_inp.config(state=NORMAL)])

        self.num_new_but.grid(row=6,column=3, ipadx=10)

        self.rbutton_sum = ttk.Radiobutton(self.window,state=DISABLED,text ="Sumar", value=1, variable=self.calculo)

        self.rbutton_sum.grid(row=2,column=0,sticky=W, padx=(40,0))
        
        self.rbutton_sub = ttk.Radiobutton(self.window,state=DISABLED, text ="Restar", value=2, variable=self.calculo)

        self.rbutton_sub.grid(row=3,column=0,sticky=W, padx=(40,0), pady=(0,10))
        
        self.rbutton_mult = ttk.Radiobutton(self.window,state=DISABLED, text ="Multiplicar", value=3, variable=self.calculo)

        self.rbutton_mult.grid(row=4,column=0,sticky=W, padx=(40,0), pady=(0,10))
        
        self.rbutton_div = ttk.Radiobutton(self.window,state=DISABLED, text ="Dividir", value=4, variable=self.calculo)

        self.rbutton_div.grid(row=5,column=0,sticky=NW, padx=(40,0))

        self.rbutton_easy = ttk.Radiobutton(self.window, value=1, cursor="hand2", text ="Facil", variable=self.difficult, command=lambda :[self.games_lab.config(text="Juegos :      "),self.wins_lab.config(text="Ganados :   "),self.loses_lab.config(text="Perdidos :   "), self.num_new_but.config(state=NORMAL), self.num_new_but.config(text="Nuevo juego"), self.clear_all(), self.num_new_but.focus(), self.clear_gwl(), self.resultado_but.config(state=DISABLED), self.resultado_inp.config(state=DISABLED), self.calculo.set(0)])

        self.rbutton_easy.grid(row=7,column=2, pady=(20,0), sticky=E)

        self.rbutton_medium = ttk.Radiobutton(self.window, cursor="hand2", text ="Medio", value=2, variable=self.difficult, command=lambda:[self.games_lab.config(text="Juegos :      "),self.wins_lab.config(text="Ganados :   "),self.loses_lab.config(text="Perdidos :   "), self.num_new_but.config(state=NORMAL), self.num_new_but.config(text="Nuevo juego"), self.clear_all(), self.num_new_but.focus(), self.clear_gwl(), self.resultado_but.config(state=DISABLED), self.resultado_inp.config(state=DISABLED), self.calculo.set(0) ])
        
        self.rbutton_medium.grid(row=7,column=3, pady=(20,0))

        self.rbutton_hard = ttk.Radiobutton(self.window, cursor="hand2", text ="Dificil", value=3, variable=self.difficult, command=lambda:[self.games_lab.config(text="Juegos :      "),self.wins_lab.config(text="Ganados :   "),self.loses_lab.config(text="Perdidos :   "), self.num_new_but.config(state=NORMAL), self.num_new_but.config(text="Nuevo juego"), self.clear_all(), self.num_new_but.focus(), self.clear_gwl(), self.resultado_but.config(state=DISABLED), self.resultado_inp.config(state=DISABLED), self.calculo.set(0) ])
        
        self.rbutton_hard.grid(row=7,column=4, pady=(20,0))
        self.resultado_inp = ttk.Entry(self.window, state=DISABLED, font=(18), width=10)
        self.resultado_inp.grid(row=0,column=3)
        self.games=[0]
        self.wins=[0]
        self.loses=[0]
        self.resultado_but = ttk.Button(self.window, cursor="hand2", text="Resultado", state=DISABLED,command=lambda:[self.verify_result(), self.random_signAbut(),self.calculate(self.difficult.get(), self.calculo.get()), self.resultado_inp.focus(), self.resultado_inp.delete(0,END), self.resultado_but.config(state=NORMAL)])
        self.resultado_but.grid(row=1,column=3, pady=(10,0))
        self.games_lab = ttk.Label(self.window, text="Juegos :      ")
        self.games_lab.grid(row=2,column=3, sticky=W, pady=(20,0), padx=(20,0))
        self.wins_lab = ttk.Label(self.window, text="Ganados :   ")
        self.wins_lab.grid(row=3,column=3, sticky=W, pady=(10,0), padx=(20,0))
        self.loses_lab = ttk.Label(self.window, text="Perdidos :   ")
        self.loses_lab.grid(row=4,column=3, sticky=W, pady=(10,0), padx=(20,0))
        
        


def run():
    juego = Aplicacion()

if __name__ == "__main__":
    run()