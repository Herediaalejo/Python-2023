import tkinter as tk

def crear_ventana(mensaje, accion):
    ventana = tk.Tk()
    ventana.title("Ejemplo de Navegación de Ventanas")
    ventana.config(bg="lightgreen")
    
    label = tk.Label(ventana, text=mensaje, font=80, bg="lightgreen")
    label.pack(pady=20, padx=20)
    
    siguiente_btn = tk.Button(ventana, font=(40),bg="#66a4fa",text=accion, command=lambda: cambiar_ventana(ventana, accion, mensaje))
    siguiente_btn.pack(pady=(0,10))

def cambiar_ventana(ventana_actual, accion, mensaje):
    ventana_actual.destroy()
    if "Hola" in mensaje:
        crear_ventana("Soy un bot", "Siguiente")
    elif "bot" in mensaje:
        crear_ventana("Y estoy programado para destruir tu PC", "Siguiente")
    elif "destruir" in mensaje:
        crear_ventana("ERA MENTIRA, espero no te hayas asustado", "Finalizar")   

# Crear la ventana inicial
crear_ventana("Hola", "Siguiente")

# Iniciar el bucle principal de tkinter
tk.mainloop()
