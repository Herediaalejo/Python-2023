from tkinter import *
from tkinter import ttk


class Program():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("450x100")
        self.window.title("Factorial")
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
    
    def calc_fact(self,num):
        self.fact = num
        if num==1:
            self.fact = 1
        else:
            while num!=1:
                self.fact = self.fact*(num-1)
                num -= 1
        self.fact_inp.config(state="normal")
        self.fact_inp.delete(0, END)
        self.fact_inp.insert(0,self.fact)
        self.fact_inp.config(state="readonly")
        

    def createWidgets(self):
        self.num_label = ttk.Label(self.window, text="n")
        self.num_label.grid(row=0, column=0, pady=30, padx=10)

        self.num_inp = ttk.Entry(self.window, width=10)
        self.num_inp.insert(0, 1)
        self.num_inp.config(state="readonly")
        self.num_inp.grid(row=0, column=1,pady=30, padx=10)

        self.fact_label = ttk.Label(self.window, text="Factorial(n)")
        self.fact_label.grid(row=0, column=2, pady=30, padx=10)

        self.fact_inp = ttk.Entry(self.window, width=20)
        self.fact_inp.insert(0, 1)
        self.fact_inp.config(state="readonly")
        self.fact_inp.grid(row=0, column=3,pady=30, padx=10)

        self.sig_button = ttk.Button(self.window,text="Siguiente", width=10)
        self.sig_button.grid(row=0,column=4,pady=30, padx=10)
        self.sig_button.config(command=lambda:[self.count_sum(), self.calc_fact(int(self.num_inp.get()))])


def main():
    App = Program()


if __name__ == '__main__':
    main()