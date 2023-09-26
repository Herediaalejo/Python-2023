from tkinter import *
from tkinter import ttk
import random

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Generador de números")
        self.window.resizable(0,0)
        self.window.geometry("350x250")
        self.window.config(bg="#00D9BB")
        self.createWidgets()
        self.window.mainloop()

    def createWidgets(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe UI', 12, "bold"), background="#00D9BB")
        self.style.configure('TButton', font=('Segoe UI', 12, "bold"), background="#00D9BB")
        self.style.configure('TEntry', background="#00D9BB")
        num_label_uno = ttk.Label(self.window, text="Número 1").grid(row=0,column=0,pady=30, padx = 30, sticky=E)
        num_label_dos = ttk.Label(self.window, text="Número 2").grid(row=1,column=0, padx = 30, sticky=E)
        num_label_gen = ttk.Label(self.window, text="Número generado").grid(row=2,column=0, padx = 30, pady=30, sticky=E)
        num_spin_uno = ttk.Spinbox(self.window, cursor="hand2",from_=-50, to=50, font=('Segoe UI', 12, "bold"), width=9)
        num_spin_uno.insert(0,1)
        num_spin_uno.config(state="readonly")
        num_spin_uno.grid(row=0,column=1)
        num_spin_dos = ttk.Spinbox(self.window, cursor="hand2",from_=51, to=150, font=('Segoe UI', 12, "bold"), width=9)
        num_spin_dos.insert(0,51)
        num_spin_dos.config(state="readonly")
        num_spin_dos.grid(row=1,column=1)
        num_generated = ttk.Entry(self.window, font=('Segoe UI', 12, "bold"), width=10, state="readonly")
        num_generated.grid(row=2, column=1)
        button_generate = ttk.Button(self.window, cursor="hand2", text="Generar", command=lambda:[num_generated.config(state=NORMAL),num_generated.delete(0,END), num_generated.insert(0,random.randint(int(num_spin_uno.get()), int(num_spin_dos.get()))), num_generated.config(state="readonly")]).grid(row=3, column=1)
   
        
def run():
    generador = Aplicacion()

if __name__ == "__main__":
    run()