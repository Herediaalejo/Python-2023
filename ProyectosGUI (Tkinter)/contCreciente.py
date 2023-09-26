from tkinter import *
from tkinter import ttk


class Program():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("300x100")
        self.window.title("ContCreciente")
        self.window.config(bg="#EDE25D")
        self.window.resizable(0,0)
        self.createWidgets()
        self.window.mainloop()
    
    def count_sum(self):
        self.count = self.num_inp.get()
        self.count = int(self.count)
        self.count+=1
        self.num_inp.config(state=NORMAL)
        self.num_inp.delete(0,END)
        self.num_inp.insert(0, self.count)
        self.num_inp.config(state="readonly")
        

    def createWidgets(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe UI', 12, "bold"), background="#EDE25D")
        self.style.configure('TButton', font=('Segoe UI', 12, "bold"), background="#EDE25D")
        self.style.configure('TEntry', background="#EDE25D")
        self.cont_lab = ttk.Label(self.window, text="Contador")
        self.cont_lab.grid(row=0, column=0, pady=30, padx=10)

        self.num_inp = ttk.Entry(self.window, font=('Segoe UI', 12, "bold"), width=10)
        self.num_inp.insert(0, 18)
        self.num_inp.config(state="readonly")
        self.num_inp.grid(row=0, column=1,pady=30, padx=20)

        self.add_button = ttk.Button(self.window, cursor="hand2",text="+", width=3)
        self.add_button.grid(row=0,column=3,pady=30)
        self.add_button.config(command=self.count_sum)


def main():
    App = Program()


if __name__ == '__main__':
    main()

