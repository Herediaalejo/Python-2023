from tkinter import *

window = Tk()
window.title("Calculator MathMag")
window.configure(bg="#1d1f1e")
window.resizable(0,0)

def calculate(operation):
    if "x" in operation:
        operation=operation.replace("x","*")
    elif "÷" in operation:
        operation=operation.replace("÷", "/")
    try:
        result = eval(operation)
        return result
    except:
        return ("Error de sintaxis")

def get_result(input_camp, result):
    input_camp.delete(0,END)
    input_camp.insert(0,result)

num_input = Entry(window, cursor="arrow", width=32, background="#565c58", foreground="white", font=("Helvetica",18), justify="right")
num_input.grid(row=0,column=0,columnspan=4, padx=5, pady=10, ipady=30)

button_color = "#555956"
button1 = Button(window, bg=button_color, cursor="hand2", fg="white",text="1", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "1"))
button2 = Button(window, bg=button_color, cursor="hand2", fg="white",text="2", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "2"))
button3 = Button(window, bg=button_color, cursor="hand2", fg="white",text="3", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "3"))
button4 = Button(window, bg=button_color, cursor="hand2", fg="white",text="4", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "4"))
button5 = Button(window, bg=button_color, cursor="hand2", fg="white",text="5", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "5"))
button6 = Button(window, bg=button_color, cursor="hand2", fg="white",text="6", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "6"))
button7 = Button(window, bg=button_color, cursor="hand2", fg="white",text="7", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "7"))
button8 = Button(window, bg=button_color, cursor="hand2", fg="white",text="8", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "8"))
button9 = Button(window, bg=button_color, cursor="hand2", fg="white",text="9", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "9"))
button0 = Button(window, bg=button_color, cursor="hand2", fg="white",text="0", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "0"))

buttonAC = Button(window, bg=button_color, cursor="hand2", fg="white",text="AC", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.delete(0, END))
buttonPar1 = Button(window, bg=button_color, cursor="hand2", fg="white",text="(", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "("))
buttonPar2 = Button(window, bg=button_color, cursor="hand2", fg="white",text=")", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, ")"))

buttonSum = Button(window, bg=button_color, cursor="hand2", fg="white",text="+", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "+"))
buttonRest = Button(window, bg=button_color, cursor="hand2", fg="white",text="-", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "-"))
buttonMult = Button(window, bg=button_color, cursor="hand2", fg="white",text="x", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "x"))
buttonDiv = Button(window, bg=button_color, cursor="hand2", fg="white",text="÷", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "÷"))
buttonDec = Button(window, bg=button_color, cursor="hand2", fg="white",text=".", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.insert(END, "."))
buttonDel = Button(window, bg=button_color, cursor="hand2", fg="white",text="⌫", width=6, height=2, font=("Segoe UI",15), command= lambda : num_input.delete(num_input.index(END)-1,END))
buttonEq = Button(window, bg=button_color, cursor="hand2", fg="white",text="=", width=6, height=2, font=("Segoe UI",15), command= lambda : get_result(num_input, calculate(num_input.get())))


buttonAC.grid(row=1,column=0, padx=1, pady=5)
buttonPar1.grid(row=1,column=1, padx=1, pady=5)
buttonPar2.grid(row=1,column=2, padx=1, pady=5)
buttonDiv.grid(row=1,column=3, padx=1, pady=5)
button7.grid(row=2,column=0, padx=1, pady=5)
button8.grid(row=2,column=1, padx=1, pady=5)
button9.grid(row=2,column=2, padx=1, pady=5)
buttonMult.grid(row=2,column=3, padx=1, pady=5)
button4.grid(row=3,column=0, padx=1, pady=5)
button5.grid(row=3,column=1, padx=1, pady=5)
button6.grid(row=3,column=2, padx=1, pady=5)
buttonRest.grid(row=3,column=3, padx=1, pady=5)
button1.grid(row=4,column=0, padx=1, pady=5)
button2.grid(row=4,column=1, padx=1, pady=5)
button3.grid(row=4,column=2, padx=1, pady=5)
buttonSum.grid(row=4,column=3, padx=1, pady=5)
button0.grid(row=5,column=0, padx=1, pady=5)
buttonDec.grid(row=5,column=1, padx=1, pady=5)
buttonDel.grid(row=5,column=2, padx=1, pady=5)
buttonEq.grid(row=5,column=3, padx=1, pady=5)


op = num_input.get()
print(op)
if len(op)>0:
    num_input.delete(0,END)
    num_input.insert(0,calculate(op))


window.mainloop()
