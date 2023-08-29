from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(bg="#CA74FF")
        self.window.resizable(0,0)
        self.window.geometry("350x400")
        self.createWidgets()
        self.window.mainloop()

    def clear(self):
        self.input_uno.delete(0,END)
        self.input_dos.delete(0,END)
        self.input_result.config(state=NORMAL)
        self.input_result.delete(0,END)
        self.input_result.config(state="readonly")
    
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
    
    def calculate(self):
        operation = self.input_uno.get() + self.button_inp[0] + self.input_dos.get()
        if "x" in operation:
            operation=operation.replace("x","*")
        elif "÷" in operation:
            operation=operation.replace("÷", "/")
        try:
            if "%" in operation:
                result = self.validNum(self.input_uno.get()) * self.validNum(self.input_dos.get()) / 100
            else:
                result = eval(operation)
        
            self.input_result.config(state=NORMAL)
            self.input_result.delete(0,END)
            self.input_result.insert(0,result)
            self.input_result.config(state="readonly")
        except:
            self.input_result.config(state=NORMAL)
            self.input_result.delete(0,END)
            self.input_result.insert(0,"ERROR")
            self.input_result.config(state="readonly")

    def createWidgets(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe UI', 12, "bold"), background="#CA74FF")
        self.style.configure('TButton', font=('Segoe UI', 12, "bold"), background="#CA74FF")
        self.style.configure('TEntry', background="#82C7FF")
        self.style.configure('TRadiobutton', font=('Segoe UI', 12, "bold"), background="#CA74FF")
        self.button_inp = []
        self.style=ttk.Style()
        self.num_lab_uno = ttk.Label(self.window, text="Primer número").grid(row=0, column=0, pady=15, padx=20, sticky=W)
        self.input_uno = ttk.Entry(self.window, font=('Segoe UI', 12), width=15)
        self.input_uno.grid(row=0, column=1, pady=15)
        self.num_lab_dos = ttk.Label(self.window, text="Segundo número").grid(row=1, column=0, pady=15, padx=20, sticky=W)
        self.input_dos = ttk.Entry(self.window, font=('Segoe UI', 12), width=15)
        self.input_dos.grid(row=1, column=1, pady=15)
        self.result_lab = ttk.Label(self.window, text="Resultado").grid(row=2, column=0, pady=15, padx=20, sticky=W)
        self.input_result = ttk.Entry(self.window, font=('Segoe UI', 12), width=15, state="readonly")
        self.input_result.grid(row=2, column=1, pady=15)
        self.button_sum= ttk.Button(self.window, cursor="hand2", width=15, text="+", command=lambda:[self.button_inp.insert(0,"+"), self.calculate()]).grid(row=3, column=0, pady=15, padx=10, ipady=5)
        self.button_sub= ttk.Button(self.window, cursor="hand2", width=15, text="-", command=lambda:[self.button_inp.insert(0,"-"), self.calculate()]).grid(row=3, column=1, pady=15, padx=10, ipady=5)
        self.button_mult= ttk.Button(self.window, cursor="hand2", width=15, text="x", command=lambda:[self.button_inp.insert(0,"*"), self.calculate()]).grid(row=4, column=0, pady=15, padx=10, ipady=5)
        self.button_div= ttk.Button(self.window, cursor="hand2", width=15, text="÷", command=lambda:[self.button_inp.insert(0,"/"), self.calculate()]).grid(row=4, column=1, pady=15, padx=10, ipady=5)
        self.button_por= ttk.Button(self.window, cursor="hand2", width=15, text="%", command=lambda:[self.button_inp.insert(0,"%"), self.calculate()]).grid(row=5, column=0, pady=15, padx=10, ipady=5)
        self.button_clear= ttk.Button(self.window, cursor="hand2", width=15, text="CLEAR", command=lambda : self.clear()).grid(row=5, column=1, pady=15, padx=10, ipady=5)
def run():
    calculadora = Aplicacion()

if __name__ == "__main__":
    run()