import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector
import time
from PIL import Image, ImageTk 
import random


def crear_celda(ventana, row, column, width, color ,height=30):
    celda = tk.Frame(ventana, width=width,height=height, bg=color)#,borderwidth=1, relief='solid'
    celda.grid(row=row, column=column, pady=(0,30), padx=20)
    return celda

def actualizar_reloj(ventana, label):
    current_time = time.strftime("%H:%M")  # Obtiene la hora actual en formato HH:MM:SS
    label.config(text=current_time)      # Actualiza el texto del label
    ventana.after(1000, lambda: actualizar_reloj(ventana, label)) # Programa la actualización cada segundo (1000 ms)

def actualizar_cronometro(ventana, label):
    global tiempo_transcurrido
    tiempo_actual = time.strftime("%M:%S", time.gmtime(tiempo_transcurrido))
    label.config(text=tiempo_actual)
    tiempo_transcurrido += 1
    ventana.after(1000, lambda: actualizar_cronometro(ventana,label))  # Actualiza cada segundo (1000 ms)

# Función para reiniciar el contador de tiempo
def reiniciar_tiempo(label):
    global tiempo_transcurrido
    tiempo_transcurrido = 0
    label.config(text="00:00")

def min_to_sec(tiempo):
  minutos, segundos = tiempo.split(":")
  minutos = int(minutos)
  segundos = int(segundos)

  segundos = minutos * 60 + segundos

  return segundos

def sec_to_min(segundos):

  minutos = segundos // 60 #division entera, devuelve numero entero
  segundos_restantes = segundos % 60 #el resto de la division
  minutos = int(minutos)
  segundos_restantes = int(segundos_restantes)

  tiempo = f"{minutos:02}:{segundos_restantes:02}" #02 hace que el numero se vea con dos digitos por mas que tenga uno solo, es decir agrega un 0 a la izquierda cuando hay tan solo un caracter

  return tiempo

# Función para cargar y mostrar información en el Treeview
def cargar_jugadores(tree):
    tree.delete(*tree.get_children())  # Borrar datos existentes en el Treeview
    cursor = conexion.cursor()
    cursor.execute("SELECT NOMBRE, TIEMPO, PUNTAJE FROM JUGADOR")
    datos = cursor.fetchall()
    jugadores = []
    for jugador in datos:
        jugadores.append(list(jugador))
    for i in range(len(jugadores)):
        jugadores[i][1] = sec_to_min(jugadores[i][1])
    for row in jugadores:
        tree.insert("", "end", values=row)
    cursor.close()

def cargar_preguntas():
    cursor = conexion.cursor()
    cursor.execute("SELECT ID_PREGUNTA, NOMBRE, RESPUESTA_CORRECTA, RESPUESTA_INCORRECTA1, RESPUESTA_INCORRECTA2, RESPUESTA_INCORRECTA3 FROM PREGUNTA")
    preguntas = cursor.fetchall()
    cursor.close()
    return preguntas

def guardar_jugador():
    cursor = conexion.cursor()
    tiempo = min_to_sec(tiempo_logrado)
    cursor.execute("INSERT INTO JUGADOR (NOMBRE, INSTAGRAM, TELEFONO, PUNTAJE, TIEMPO) values (%s,%s,%s,%s,%s)", (nombre, instagram, telefono, puntaje, tiempo))
    conexion.commit()
    cursor.close()

def seleccionar_pregunta():
    if not listaPreguntas:
        return None

    fila_elegida = random.choice(listaPreguntas)
    pregunta = fila_elegida[1]
    respuestaCor = fila_elegida[2]
    respuestaInc1 = fila_elegida[3]
    respuestaInc2 = fila_elegida[4]
    respuestaInc3 = fila_elegida[5]
    listaPreguntas.remove(fila_elegida)
    return pregunta, respuestaCor, respuestaInc1, respuestaInc2, respuestaInc3

def insertar_salto_de_linea(texto, limite):
    if len(texto) <= limite:
        return texto  # No es necesario un salto de línea, el texto es lo suficientemente corto

    palabras = texto.split()  # Dividir el texto en palabras
    conteo_caracteres = 0
    indice_ultima_palabra = 0

    for i, palabra in enumerate(palabras):
        conteo_caracteres += len(palabra) + 1  # +1 para contar el espacio en blanco
        if conteo_caracteres > limite:
            palabras[indice_ultima_palabra] += '\n'  # Agregar el salto de línea a la última palabra
            conteo_caracteres = len(palabra)  # Reiniciar el conteo con la longitud de la palabra actual
        else:
            indice_ultima_palabra = i

    return ' '.join(palabras)

def sumar_puntos():
    global puntaje, totalAcertado
    puntaje+=100
    totalAcertado +=1

def nueva_pregunta():
    pregunta_seleccionada = seleccionar_pregunta()
    if pregunta_seleccionada:
        rojo = "#f54254"
        azul = "#4287f5"
        verde = "#42f57b"
        amarillo = "#f5e342"
        button_color = [rojo, azul, verde, amarillo]
        random.shuffle(button_color)
        #fila, columna, padx(primervalor), padx(segundovalor)
        button_grid = [(9,1,0,50),(9,2,50,0),(12,1,0,50),(12,2,50,0)]
        random.shuffle(button_grid)
        # Actualizamos el contenido de la ventana actual
        pregunta = insertar_salto_de_linea(pregunta_seleccionada[0], 40)
        respuestaCor = insertar_salto_de_linea(pregunta_seleccionada[1], 22)
        respuestaInc1 = insertar_salto_de_linea(pregunta_seleccionada[2], 22)
        respuestaInc2 = insertar_salto_de_linea(pregunta_seleccionada[3], 22)
        respuestaInc3 = insertar_salto_de_linea(pregunta_seleccionada[4], 22)
        preguntaLabel.config(text=pregunta)
        opcion1.config(text=respuestaCor, background=button_color[0])
        opcion2.config(text=respuestaInc1, background=button_color[1])
        opcion3.config(text=respuestaInc2, background=button_color[2])
        opcion4.config(text=respuestaInc3, background=button_color[3])
        opcion1.grid(row=button_grid[0][0], column=button_grid[0][1], sticky="nsew", padx=(button_grid[0][2],button_grid[0][3]))
        opcion2.grid(row=button_grid[1][0], column=button_grid[1][1], sticky="nsew", padx=(button_grid[1][2],button_grid[1][3]))
        opcion3.grid(row=button_grid[2][0], column=button_grid[2][1], sticky="nsew", padx=(button_grid[2][2],button_grid[2][3]))
        opcion4.grid(row=button_grid[3][0], column=button_grid[3][1], sticky="nsew", padx=(button_grid[3][2],button_grid[3][3]))
        puntaje_label.config(text=f"Puntaje: {puntaje}")
    
    else:
        fin_juego()

def eliminar_widgets(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def empezar_juego():
    global nombre, telefono, instagram
    nombre = name_entry.get()
    instagram = ig_entry.get()
    telefono = tel_entry.get()
    if nombre:
        if len(nombre)>2:
            #Verifico si alguno de los caracteres de nombre es un número
            nombre_valido = not any(c.isdigit() for c in nombre)
        else:
            messagebox.showwarning("Error", "El nombre debe tener más de 2 caracteres.")
            return
    else:
        messagebox.showwarning("Error", "Debe ingresar un nombre")
        return

    if nombre_valido:
        create_window()
    else:
        messagebox.showwarning("Error", "El nombre no puede contener números")
        return

def mostrar_respuesta(window, op):
    for widget in window.winfo_children():
        widget.hide()
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, "red")

    respuesta_label = tk.Label(window, font=(font, 40))
    respuesta_label.grid.grid(row=7,column=0,columnspan=4)
 
    if op == 1:

        respuesta_label.config(text="Respuesta correcta!", bg="green")

        # Esperar dos segundos
        time.sleep(2)

        # Ocultar el widget Label
        respuesta_label.destroy()

    elif op == 2:
        respuesta_label.config(text="Respuesta incorrecta!", bg="red")

        # Esperar dos segundos
        time.sleep(2)

        # Ocultar el widget Label
        respuesta_label.destroy()
    
    for widget in window.winfo_children():
        widget.show()

    nueva_pregunta()




def fin_juego():
    global tiempo_logrado
    bgcolor = "#4a4949"
    tiempo_logrado = time_label.cget('text')
    reiniciar_tiempo(time_label)
    eliminar_widgets(window)
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor)
    fin_label = tk.Label(window, text=f"Felicidades {nombre.capitalize()}! Finalizaste el juego.", font=(font,60))
    fin_label.grid(row=3,column=0,columnspan=4)

    preguntasT_label = tk.Label(window, font=(font,40), text=f"Contestaste correctamente {totalAcertado} de {totalPreguntas} preguntas")
    preguntasT_label.grid(row=5,column=0,columnspan=4)

    punt_label = tk.Label(window, text=f"Tu puntaje fue: {puntaje}", font=(font,40))
    punt_label.grid(row=6,column=0,columnspan=4)

    tiempoT_label = tk.Label(window, text=f"Tu tiempo fue de: {tiempo_logrado}", font=(font,40))
    tiempoT_label.grid(row=7,column=0,columnspan=4)

    regresar_button = tk.Button(window, text="Regresar", cursor="hand2", bg="green", font=(font,20), relief="flat", command=lambda:[main()])
    regresar_button.grid(row=10,column=0,columnspan=4, ipadx=10, ipady=10)

    guardar_jugador()


def create_window():
    global font, time_label, preguntaLabel, opcion1, opcion2, opcion3, opcion4, user_label, puntaje_label

    bgcolor = "#4a4949"

    eliminar_widgets(window)
    
    window.config(bg=bgcolor)
    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor)

    user_frame = tk.Frame(window, bg="orange")
    user_frame.grid(row=1,column=0,sticky="nsew", rowspan=4, padx=(30,80), pady=25)
    user_frame.columnconfigure(0, weight=1)  # Expande la columna 0
    user_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    user_frame.rowconfigure(1, weight=1)  # Expande la fila 1

    user_label = tk.Label(user_frame, font=(font, 20), text=f"Jugador: {nombre}", bg="orange")
    user_label.grid(row=0, column=0, sticky="w", padx=(10,0))

    puntaje_label = tk.Label(user_frame, font=(font, 20), bg="orange")
    puntaje_label.grid(row=1, column=0, sticky="w", padx=(10,0))

    time_frame = tk.Frame(window, bg="#4a4949")
    time_frame.grid(row=1,column=3,sticky="nsew", rowspan=4)
    time_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    time_frame.columnconfigure(0, weight=1)  # Expande la columna 0

    time_label = tk.Label(time_frame, text="00:00", font=(font, 60), bg="orange")
    time_label.grid(column=0, row=0)

    actualizar_cronometro(window, time_label)

    pregunta_frame = tk.Frame(window, background="white")
    pregunta_frame.grid(row=1,column=1, columnspan=2,rowspan=4, sticky="nsew")
    pregunta_frame.grid_rowconfigure(0, weight=1)  # Expande la fila 0
    pregunta_frame.rowconfigure(0, weight=1)  # Expande la fila 0
    pregunta_frame.columnconfigure(0, weight=1)  # Expande la columna 0
    preguntaLabel = tk.Label(pregunta_frame, background="white", font=(font, 30))
    preguntaLabel.grid(row=0,column=0, sticky="nsew")
    opcion1 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[sumar_puntos(), mostrar_respuesta(window,1)])
    opcion2 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[mostrar_respuesta(window,2)])
    opcion3 = tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[ mostrar_respuesta(window,2)])
    opcion4= tk.Button(window, width=20, bg="lightgray", cursor="hand2", relief="flat", font=(font, 20), command=lambda:[ mostrar_respuesta(window,2)])
        
    exitP_button = tk.Button(window, width=20, text="SALIR",bg="#eb6781",cursor="hand2",font=(font, 16), relief="flat", command=lambda:[reiniciar_tiempo(time_label), main()])
    exitP_button.grid(row=15,column=0, rowspan=2)

    nueva_pregunta()


def main():
    global window, listaPreguntas, totalPreguntas, screen_width, font, totalAcertado, puntaje, tiempo_transcurrido, name_entry, ig_entry, tel_entry

    eliminar_widgets(window)
    screen_width = window.winfo_screenwidth()

    bgcolor = "#BCFFCC"
    frcolor = "#ADDAFF"

    for row in range(18):
        for column in range(4):
            crear_celda(window, row, column, (screen_width-180)/4, bgcolor)
    
    for i in range(18):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)


    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("TLabel", font=(font, 30)) 
    estilo.configure("TEntry", font=(font, 20)) 
    estilo.configure("Custom.TLabel", font=(font,20))
    estilo.configure("Title.TLabel", font=(font,45))

    window.columnconfigure(0, weight=1)  # Expande la primera columna
    window.columnconfigure(1, weight=1)  # Expande la segunda columna
    window.columnconfigure(2, weight=1)  # Expande la tercera columna
    window.columnconfigure(3, weight=1)  # Expande la cuarta columna

    window.config(bg=bgcolor)
    # Iniciar el bucle principal de tkinter

    clock_label = tk.Label(window, font=(font, 32), bg=bgcolor)
    clock_label.grid(row=17,column=3, sticky="e")

    actualizar_reloj(window, clock_label)  # Inicia la actualización

    # Obtén la ruta del directorio actual donde se encuentra tu archivo .py
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

    # Combina el directorio actual con el nombre de la imagen
    ruta_imagen = os.path.join(directorio_actual, "logo-isaui.jpg")

    # Abre una imagen
    image = Image.open(ruta_imagen)

    # Convierte la imagen a un formato compatible con tkinter
    icon = ImageTk.PhotoImage(image)

    logo = tk.Label(window, image=icon, background=bgcolor)
    logo.grid(row=0,column=0,sticky="w", rowspan=2, pady=(10,0), padx=(10,0))

    title = ttk.Label(text="TRIVIAUI ", background=bgcolor, style="Title.TLabel")
    title.grid(row=0,column=0, columnspan=2, rowspan=3, padx=(100,0), sticky="s", pady=(0,10))

    description = ttk.Label(text="EL JUEGO DE PREGUNTAS Y RESPUESTAS DE LOS 40 AÑOS DEL ISAUI.",style="Custom.TLabel", background=bgcolor)
    description.grid(row=17,column=0, columnspan=4, sticky="w", padx=(10,0))

    form = tk.Frame(window, bg="lightblue", width=450)
    form.grid(row=3,column=0,columnspan=2, rowspan=13, sticky="ns", padx=(100,0))

    name_label = ttk.Label(text="NOMBRE *", background="lightblue", font=(font, 20))
    name_label.grid(row=4, column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    name_entry = ttk.Entry(width=25, font=(font, 16))
    name_entry.grid(row=5,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    ig_label = ttk.Label(text="INSTAGRAM", background="lightblue", font=(font, 20))
    ig_label.grid(row=6, column=0, columnspan=2, rowspan=2, padx=(100,0))

    ig_entry = ttk.Entry(width=25, font=(font, 16))
    ig_entry.grid(row=7,column=0, columnspan=2, rowspan=2, padx=(100,0))

    tel_label = ttk.Label(text="TELEFONO", background="lightblue", font=(font, 20))
    tel_label.grid(row=8, column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    tel_entry = ttk.Entry(width=25, font=(font, 16))
    tel_entry.grid(row=9,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    newGame_button = tk.Button(window, width=20, text="NUEVO JUEGO", bg="#5bd0f0",cursor="hand2",font=(font, 16), relief="flat", command=lambda:[empezar_juego()])
    newGame_button.grid(row=12,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="n")

    exit_button = tk.Button(window, width=20, text="SALIR",bg="#eb6781",cursor="hand2",font=(font, 16), relief="flat", command=lambda:window.destroy())
    exit_button.grid(row=13,column=0, columnspan=2, rowspan=2, padx=(100,0), sticky="s")

    punt_label = ttk.Label(window, text="PUNTAJES", background=bgcolor)
    punt_label.grid(row=1, column=2, columnspan=2, rowspan=2)

    data_button = tk.Button(window, width=10, text="DATOS", bg="#be77ed",cursor="hand2",font=(font, 16), relief="flat")
    data_button.grid(row=9,column=2, columnspan=2, rowspan=2)

    tree_style = ttk.Style()

    tree_style.configure("Custom.Treeview.Heading", font=(font, 16), background="orange", margin=(5, 5))  # Cambia la fuente de los headings
    tree_style.configure("Custom.Treeview", font=(font, 16), background="", fieldbackground="#dbe096", rowheight=30, foreground="black")  # Cambia la fuente de los datos de la grilla
    tree_style.map("Custom.Treeview", background=[("selected", "brown")])

    punt_tree = ttk.Treeview(window, columns=("Nombre", "Tiempo", "Puntaje"), style="Custom.Treeview")
    punt_tree.grid(row=3, column=2, columnspan=2, rowspan=6, sticky="nsew")

    punt_tree.column("#0", width=0, stretch=tk.NO)
    punt_tree.heading("#1", text="Nombre")
    punt_tree.heading("#2", text="Tiempo")
    punt_tree.heading("#3", text="Puntaje")

    punt_tree.column("#1", anchor="center")
    punt_tree.column("#2", anchor="center")
    punt_tree.column("#3", anchor="center")

    punt_tree.bind("<Button-1>", lambda event: punt_tree.selection_remove(punt_tree.selection()) if punt_tree.selection() else None)
      
    cargar_jugadores(punt_tree)

    totalAcertado = 0
    puntaje = 0
    tiempo_transcurrido = 0

    listaPreguntas = cargar_preguntas()

    totalPreguntas = len(listaPreguntas)

    window.mainloop()

if __name__ == "__main__":
    conexion = mysql.connector.connect(host="localhost", user="root", password="", database="trivia")
    font = "Gill Sans MT"
    listaPreguntas = []
    window = tk.Tk()
    window.title("Trivia")
    window.attributes('-fullscreen', True)
    window.resizable(0, 0)
    main()




"""
create database trivia;

use trivia;

create table Jugador(
ID_JUGADOR int auto_increment primary key,
NOMBRE VARCHAR(255) NOT NULL,
INSTAGRAM varchar(255),
TELEFONO varchar(255),
PUNTAJE INT NOT NULL,
TIEMPO DOUBLE NOT NULL
);

create table Pregunta(
ID_PREGUNTA INT auto_increment primary key,
PREGUNTA VARCHAR (255) NOT NULL,
RESPUESTA_CORRECTA VARCHAR (255) NOT NULL,
RESPUESTA_INCORRECTA1 VARCHAR(255) NOT NULL,
RESPUESTA_INCORRECTA2 VARCHAR(255) NOT NULL,
RESPUESTA_INCORRECTA3 VARCHAR(255) NOT NULL
);

INSERT INTO pregunta(NOMBRE, RESPUESTA_CORRECTA, RESPUESTA_INCORRECTA1, RESPUESTA_INCORRECTA2, RESPUESTA_INCORRECTA3) VALUES 
("¿En qué año se fundó el instituto?", "1983", "1987", "1993", "1980"), 
("¿Cuál fue el nombre del establecimiento educativo cuando se fundó?", "Complejo Facultativo de Enseñanza Superior San Francisco de Asís", "Instituto Educativo Superior Cura Brochero", "Instituto Superior Arturo Umberto Illia", "Escuela Mayor Facultativa Raúl Alfonsin"), 
("¿Cómo se llamaban los fundadores?", "Raúl", "Eduardo", "Claudio", "Graciela"), 
("¿En qué año se convierte en colegio nacional?", "1985", "1989", "1995", "2001"), 
("¿Cuántos directores tuvo el Instituto hasta la fecha?", "4", "7", "9", "12"), 
("¿Cuántas carreras se dictan actualmente en el ISAUI?", "6", "4", "9", "11"), 
("¿Cuál fue el primer número de teléfono del Instituto?", "41164", "52314", "34245", "79845"), 
("¿Qué es el workshop?", "Una técnica de venta", "Un lugar donde comprar cosas", "Una carrera", "Un estilo de vida"), 
("¿Qué carrera fue la pionera con los viajes en las materias de prácticas?", "Técnico y Guía Superior en Turismo", "Tecnicatura en Desarrollo de Software", "Diseño de Espacios", "Trekking"), 
("¿Cómo era el edificio educativo en sus comienzos?", "Una casa con 3 ambientes", "Una cafetería con 2 ambientes", "Una casa con tan solo 1 ambiente", "Una panadería de 5 ambientes"), 
("¿Qué tipo de instituto es el ISAUI?", "Instituto Público", "Instituto Privado", "Instituto Semi-privado", "Instituto Semi-público"), 
("¿A partir de qué año la cooperadora empezó a construir las aulas?", "1986", "1981", "1992", "2001"), 
("¿De dónde provenía el dinero?", "Del bono contribución de los padres", "Del bono contribución de los profesores", "Del gobierno nacional", "Del gobierno provincial"), 
("¿Quién fue el presidente de la cooperadora en el inicio de la institución?", "Sr. Gatica", "Sra. Graciela", "Sr. Augusto", "Carlos"), 
("¿Quién es la presidenta de la cooperadora actualmente?", "Daniela Maschio", "Gabriela Roldan", "Agustina Aperlo", "Elizabeth Afazani"), 
("¿Cómo se logró la nacionalización?", "Mediante la gestión del diputado Anselmo Pelaez", "Mediante la ayuda del gobernador Schiaretti", "Mediante el acuerdo con la UEPC", "Mediante la reunión de las escuelas de Carlos Paz");
"""
