from tkinter import *
from tkinter import ttk

class Aplicacion():
    def __init__(self):
        self.window = Tk()
        self.window.title("Peliculas")
        self.window.resizable(0,0)
        self.window.geometry("650x350")
        self.window.config(bg="#B28BFF")
        self.createWidgets()
        self.window.mainloop()

    def clear(self):
        self.input_uno.delete(0,END)
        self.input_dos.delete(0,END)
        self.input_result.config(state=NORMAL)
        self.input_result.delete(0,END)
        self.input_result.config(state="readonly")
    
    def calculate(self):
        operation = self.input_uno.get() + self.button_inp[0] + self.input_dos.get()
        if "x" in operation:
            operation=operation.replace("x","*")
        elif "÷" in operation:
            operation=operation.replace("÷", "/")
        try:
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
        self.style.configure('TLabel', font=('Segoe UI', 12, "bold"), background="#B28BFF")
        self.style.configure('TButton', font=('Segoe UI', 12, "bold"), background="#B28BFF")
        self.style.configure('TEntry', background="#B28BFF")
        title = ttk.Label(self.window, text="Escribe el titulo de una pelicula").grid(row=0, column=0, pady = 30, padx=50)
        movies = ttk.Label(self.window, text="Peliculas").grid(row=0, column=1, padx= 30)
        title_input = ttk.Entry(self.window, font=('Segoe UI', 12, "bold"), width=30)
        title_input.grid(row=1,column=0, sticky=N)
        movies_box = Listbox(self.window, font=('Segoe UI', 12, "bold"), width=30)
        movies_box.grid(row=1, column=1, rowspan=2)
        add_button = ttk.Button(self.window, text="Añadir", cursor="hand2", command=lambda :[movies_box.insert(END, title_input.get()), title_input.delete(0, END)])
        add_button.grid(row=1,column=0, pady=30)
        clear_button = ttk.Button(self.window, text="Borrar todo", cursor="hand2", command=lambda:movies_box.delete(0,END)).grid(row=1, column=0, sticky=S)
        
def run():
    calculadora = Aplicacion()

if __name__ == "__main__":
    run()