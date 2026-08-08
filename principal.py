import tkinter as tk
import random

################################
#            Temas             #
################################

TEMAS = {
    "dark": {
        "fondo": "#101820",
        "texto": "white",
        "boton": "#1F2933",
        "texto_boton": "white"
    },

    "matrix": {
        "fondo": "#000000",
        "texto": "#00FF41",
        "boton": "#003B00",
        "texto_boton": "#00FF41"
    },

    "light": {
        "fondo": "#F2F2F2",
        "texto": "#202020",
        "boton": "#D9D9D9",
        "texto_boton": "#202020"
    }
}
tema_actual = "dark"

# -----------------------------#
#       Efecto Matrix          #
# -----------------------------#

matrices = {}
ventanas_abiertas = []

CARACTERES_MATRIX = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def iniciar_matrix_en(ventana_destino):
    # Si ya tiene Matrix, no hacemos otro
    if ventana_destino in matrices:
        return

    canvas = tk.Canvas(
        ventana_destino,
        bg="#000000",
        highlightthickness=0
    )

    canvas.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    # Colocar el Canvas detrás de los demás widgets
    ventana_destino.tk.call("lower", canvas._w)

    columnas = []

    for x in range(0, 800, 20):
        columnas.append({
            "x": x,
            "y": random.randint(-500, 0),
            "velocidad": random.randint(3, 8)
        })

    matrices[ventana_destino] = {
        "canvas": canvas,
        "columnas": columnas,
        "animacion": None
    }

    animar_matrix(ventana_destino)


def animar_matrix(ventana_destino):

    if ventana_destino not in matrices:
        return

    if not ventana_destino.winfo_exists():
        matrices.pop(ventana_destino, None)
        return

    datos = matrices[ventana_destino]
    canvas = datos["canvas"]
    columnas = datos["columnas"]

    canvas.delete("all")

    ancho = canvas.winfo_width()
    alto = canvas.winfo_height()

    if ancho <= 1:
        ancho = 800

    if alto <= 1:
        alto = 500

    for columna in columnas:

        x = columna["x"]
        y = columna["y"]

        # Si la ventana es más pequeña, no dibujamos
        # columnas que estén fuera de ella
        if x > ancho:
            continue

        for i in range(8):

            caracter = random.choice(CARACTERES_MATRIX)

            canvas.create_text(
                x,
                y - (i * 18),
                text=caracter,
                fill="#00FF41",
                font=("Courier New", 12, "bold")
            )

        columna["y"] += columna["velocidad"]

        if columna["y"] > alto + 100:
            columna["y"] = random.randint(-300, 0)

    datos["animacion"] = ventana_destino.after(
        50,
        lambda: animar_matrix(ventana_destino)
    )


def detener_matrix_en(ventana_destino):

    if ventana_destino not in matrices:
        return

    datos = matrices[ventana_destino]

    if datos["animacion"] is not None:
        try:
            ventana_destino.after_cancel(datos["animacion"])
        except:
            pass

    datos["canvas"].destroy()

    del matrices[ventana_destino]


def actualizar_matrix():

    if tema_actual == "matrix":
        iniciar_matrix_en(ventana)

        for ventana_destino in ventanas_abiertas:
            if ventana_destino.winfo_exists():
                iniciar_matrix_en(ventana_destino)

    else:
        detener_matrix_en(ventana)

        for ventana_destino in ventanas_abiertas:
            if ventana_destino.winfo_exists():
                detener_matrix_en(ventana_destino)

################################
#            Menu              #
################################

ventana = tk.Tk()
ventana.title("Code BREAKER")
ventana.geometry("800x500")
ventana.resizable(False, False)
ventana.configure(bg="#101820")

##############################
#        Instrucciones       #
##############################

ventana_instrucciones = None
titulo_instrucciones = None
texto_instrucciones = None
boton_volver_instrucciones = None

ventana_temas = None
ventana_juego = None
ventana_records = None
entrada_juego = None
resultado = None
etiqueta_intentos = None
codigo_secreto = ""
intentos = 0
titulo_temas = None
nombre_jugador = ""
boton_dark = None
boton_matrix = None
boton_light = None
boton_volver_temas = None

def mostrar_instrucciones():
    global ventana_instrucciones
    global titulo_instrucciones
    global texto_instrucciones
    global boton_volver_instrucciones

    tema = TEMAS[tema_actual]

    # Si la ventana ya existe, solamente la mostramos
    if ventana_instrucciones is not None and ventana_instrucciones.winfo_exists():
        ventana_instrucciones.lift()
        actualizar_matrix()
        return

    ventana_instrucciones = tk.Toplevel(ventana)
    ventanas_abiertas.append(ventana_instrucciones)
    ventana_instrucciones.title("Instrucciones")
    ventana_instrucciones.geometry("700x500")
    ventana_instrucciones.resizable(False, False)

    ventana_instrucciones.configure(bg=tema["fondo"])

    titulo_instrucciones = tk.Label(
        ventana_instrucciones,
        text="INSTRUCCIONES",
        font=("Arial", 24, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )
    titulo_instrucciones.pack(pady=40)

    texto_instrucciones = tk.Label(
        ventana_instrucciones,
text="¿CÓMO JUGAR?\n\n"
     "• Introduce una combinación de números.\n"
     "• Haz clic en REVISAR.\n"
     "• Si la combinación es incorrecta intenta de nuevo.\n\n"
     
     "PISTAS\n\n"
     "• El código secreto está formado por números sin repetir.\n"
     "• Un * por número correcto en la posición correcta.\n"
     "• Un - por número correcto en posición incorrecta.\n"
     "• Sin símbolo → el número no pertenece al código.\n\n"
     
     "¡Intenta resolverlo con la menor cantidad de intentos!",
    font=("Arial", 12),
    bg=tema["fondo"],
    fg=tema["texto"],
    justify="left",
    bd=0,
    highlightthickness=0,
    relief="flat"
    )
    texto_instrucciones.pack(pady=10)

    boton_volver_instrucciones = tk.Button(ventana_instrucciones,
        text="VOLVER",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=ventana_instrucciones.destroy
    )
    boton_volver_instrucciones.pack(pady=30)
    if tema_actual == "matrix":
        iniciar_matrix_en(ventana_instrucciones)

def cambiar_tema(nombre_tema):
    global tema_actual

    tema_actual = nombre_tema

    tema = TEMAS[tema_actual]

    ventana.configure(bg=tema["fondo"])

    titulo.configure(
        bg=tema["fondo"],
        fg=tema["texto"]
    )

    botones = [
        boton_jugar,
        boton_instrucciones,
        boton_records,
        boton_tema,
        boton_salir
    ]

    for boton in botones:
        boton.configure(
            bg=tema["boton"],
            fg=tema["texto_boton"],
            activebackground=tema["boton"],
            activeforeground=tema["texto_boton"]
        )

    # Actualizar ventana de instrucciones
    if ventana_instrucciones is not None and ventana_instrucciones.winfo_exists():

        ventana_instrucciones.configure(
            bg=tema["fondo"]
        )

        titulo_instrucciones.configure(
            bg=tema["fondo"],
            fg=tema["texto"]
        )

        texto_instrucciones.configure(
            bg=tema["fondo"],
            fg=tema["texto"]
        )

        boton_volver_instrucciones.configure(
            bg=tema["boton"],
            fg=tema["texto_boton"],
            activebackground=tema["boton"],
            activeforeground=tema["texto_boton"]
        )
    # Actualizar ventana de temas
    if ventana_temas is not None and ventana_temas.winfo_exists():
        ventana_temas.configure(
        bg=tema["fondo"]
    )
        
        # Actualizar ventana de selección de juego
    if ventana_juego is not None and ventana_juego.winfo_exists():

        ventana_juego.configure(
            bg=tema["fondo"]
        )

        for widget in ventana_juego.winfo_children():

            if isinstance(widget, tk.Label):
                widget.configure(
                    bg=tema["fondo"],
                    fg=tema["texto"]
                )

            elif isinstance(widget, tk.Button):
                widget.configure(
                    bg=tema["boton"],
                    fg=tema["texto_boton"],
                    activebackground=tema["boton"],
                    activeforeground=tema["texto_boton"]
                )

            elif isinstance(widget, tk.Spinbox):
                widget.configure(
                    bg=tema["boton"],
                    fg=tema["texto_boton"]
                )

    titulo_temas.configure(
        bg=tema["fondo"],
        fg=tema["texto"]
    )

    botones_temas = [
        boton_dark,
        boton_matrix,
        boton_light,
        boton_volver_temas
    ]

    for boton in botones_temas:
        boton.configure(
            bg=tema["boton"],
            fg=tema["texto_boton"],
            activebackground=tema["boton"],
            activeforeground=tema["texto_boton"]
    )
    
    actualizar_matrix()

def mostrar_temas():
    global ventana_temas
    global titulo_temas
    global boton_dark
    global boton_matrix
    global boton_light
    global boton_volver_temas

    tema = TEMAS[tema_actual]

    # Si la ventana ya existe, solamente la mostramos
    if ventana_temas is not None and ventana_temas.winfo_exists():
        ventana_temas.lift()
        return

    ventana_temas = tk.Toplevel(ventana)
    ventanas_abiertas.append(ventana_temas)
    ventana_temas.title("Tema")
    ventana_temas.geometry("400x350")
    ventana_temas.resizable(False, False)

    ventana_temas.configure(
        bg=tema["fondo"]
    )

    titulo_temas = tk.Label(ventana_temas,
        text="TEMA",
        font=("Arial", 26, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )
    titulo_temas.pack(pady=35)

    boton_dark = tk.Button(ventana_temas,
        text="DARK",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=lambda: cambiar_tema("dark")
    )
    boton_dark.pack(pady=5)

    boton_matrix = tk.Button(ventana_temas,
        text="MATRIX",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=lambda: cambiar_tema("matrix")
    )
    boton_matrix.pack(pady=5)

    boton_light = tk.Button(ventana_temas,
        text="LIGHT",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=lambda: cambiar_tema("light")
    )
    boton_light.pack(pady=5)

    boton_volver_temas = tk.Button(ventana_temas,
        text="VOLVER",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=ventana_temas.destroy
    )
    boton_volver_temas.pack(pady=15)

def iniciar_juego():
    global ventana_juego

    tema = TEMAS[tema_actual]

    ventana_juego = tk.Toplevel(ventana)
    ventanas_abiertas.append(ventana_juego)
    ventana_juego.title("Nueva partida")
    ventana_juego.geometry("500x400")
    ventana_juego.resizable(False, False)

    ventana_juego.configure(
        bg=tema["fondo"]
    )

    if tema_actual == "matrix":
        iniciar_matrix_en(ventana_juego)

    titulo_juego = tk.Label(
        ventana_juego,
        text="CODE BREAKER",
        font=("Arial", 26, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0
    )

    titulo_juego.pack(pady=35)

    texto_nombre = tk.Label(
    ventana_juego,
    text="Nombre del jugador:",
    font=("Arial", 12),
    bg=tema["fondo"],
    fg=tema["texto"]
)

    texto_nombre.pack(pady=10)

    nombre_jugador = tk.Entry(
        ventana_juego,
        font=("Arial", 14),
        justify="center",
        width=20
    )

    nombre_jugador.pack(pady=5)

    texto = tk.Label(
        ventana_juego,
        text="¿Cuántos números tendrá el código?",
        font=("Arial", 12),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0
    )

    texto.pack(pady=10)

    longitud = tk.Spinbox(
        ventana_juego,
        from_=3,
        to=10,
        font=("Arial", 16),
        width=5,
        justify="center"
    )

    longitud.pack(pady=15)

    boton_iniciar = tk.Button(
        ventana_juego,
        text="INICIAR",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=lambda: crear_partida(
            int(longitud.get()),
            nombre_jugador.get()
        )
    )

    boton_iniciar.pack(pady=20)

def partida_ganada():
    tema = TEMAS[tema_actual]

    ventana_ganada = tk.Toplevel(ventana_juego)
    ventana_ganada.title("¡Ganaste!")
    ventana_ganada.geometry("400x300")
    ventana_ganada.resizable(False, False)

    ventana_ganada.configure(
        bg=tema["fondo"]
    )
    
    titulo = tk.Label(
        ventana_ganada,
        text="¡FELICIDADES!",
        font=("Arial", 24, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"]
    )
    titulo.pack(pady=35)

    guardar_record(nombre_jugador, intentos)

    texto = tk.Label(
        ventana_ganada,
        text=f"¡Ganaste en {intentos} intentos!\n\n"
             f"Código: {codigo_secreto}",
        font=("Arial", 14),
        bg=tema["fondo"],
        fg=tema["texto"]
    )
    texto.pack(pady=10)

    boton_menu = tk.Button(
        ventana_ganada,
        text="VOLVER AL MENÚ",
        font=("Arial", 12, "bold"),
        width=18,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=lambda: [ventana_ganada.destroy(), ventana_juego.destroy()]
    )
    boton_menu.pack(pady=20)

def revisar_respuesta():
    global intentos

    respuesta = entrada_juego.get()

    # Comprobar que tenga la longitud correcta
    if len(respuesta) != len(codigo_secreto):
        resultado.configure(
            text=f"Debes introducir {len(codigo_secreto)} números."
        )
        return

    # Comprobar que solamente sean números
    if not respuesta.isdigit():
        resultado.configure(
            text="Solo puedes introducir números."
        )
        return

    # Comprobar que no haya números repetidos
    if len(set(respuesta)) != len(respuesta):
        resultado.configure(
            text="No puedes repetir números."
        )
        return

    intentos += 1

    pistas = ""

    for i in range(len(codigo_secreto)):

        if respuesta[i] == codigo_secreto[i]:
            pistas += "*"

        elif respuesta[i] in codigo_secreto:
            pistas += "-"

        else:
            pistas += " "

    # Reorganizar: primero * y después -
    asteriscos = pistas.count("*")
    guiones = pistas.count("-")

    pistas = " ".join(["*"] * asteriscos + ["-"] * guiones)

    resultado.configure(
        text=f"{respuesta}\n{pistas}",
        font=("Arial", 16)
    )

    if respuesta == codigo_secreto:
        partida_ganada()
def crear_partida(longitud, nombre):
    global codigo_secreto
    global intentos
    global ventana_juego
    global entrada_juego
    global etiqueta_intentos
    global resultado
    global nombre_jugador

    nombre_jugador = nombre

    codigo_secreto = "".join(
        random.sample("0123456789", longitud)
    )

    print("Código secreto:", codigo_secreto)

    intentos = 0

    # Cerramos la ventana de selección
    ventana_juego.destroy()

    # Creamos la ventana real del juego
    ventana_juego = tk.Toplevel(ventana)
    ventanas_abiertas.append(ventana_juego)
    ventana_juego.title("Code Breaker")
    ventana_juego.geometry("600x500")
    ventana_juego.resizable(False, False)

    tema = TEMAS[tema_actual]

    ventana_juego.configure(
        bg=tema["fondo"]
    )

    if tema_actual == "matrix":
        iniciar_matrix_en(ventana_juego)

    titulo_juego = tk.Label(
        ventana_juego,
        text="CODE BREAKER",
        font=("Arial", 28, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    titulo_juego.pack(pady=(35, 10))

    texto_longitud = tk.Label(
        ventana_juego,
        text=f"Código de {longitud} números",
        font=("Arial", 12),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    texto_longitud.pack(pady=5)

    entrada_juego = tk.Entry(
        ventana_juego,
        font=("Arial", 20),
        justify="center",
        width=15
    )

    entrada_juego.pack(pady=20)

    boton_revisar = tk.Button(
        ventana_juego,
        text="REVISAR",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=revisar_respuesta
    )

    boton_revisar.pack(pady=10)

    etiqueta_intentos = tk.Label(
        ventana_juego,
        text="Intentos: 0",
        font=("Arial", 12),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    etiqueta_intentos.pack(pady=15)

    etiqueta_pistas = tk.Label(
        ventana_juego,
        text="PISTAS",
        font=("Arial", 14, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"],
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    etiqueta_pistas.pack(pady=(10, 5))

    resultado = tk.Label(
        ventana_juego,
        text="",
        font=("Arial", 12),
        bg=tema["fondo"],
        fg=tema["texto"],
        justify="left",
        bd=0,
        highlightthickness=0,
        relief="flat"
    )

    resultado.pack(pady=10)
def mostrar_records():
    global ventana_records

    tema = TEMAS[tema_actual]

    ventana_records = tk.Toplevel(ventana)
    ventanas_abiertas.append(ventana_records)
    ventana_records.title("Récords")
    ventana_records.geometry("500x450")
    ventana_records.resizable(False, False)

    ventana_records.configure(
        bg=tema["fondo"]
    )

    if tema_actual == "matrix":
        iniciar_matrix_en(ventana_records)

    titulo = tk.Label(
        ventana_records,
        text="RÉCORDS",
        font=("Arial", 26, "bold"),
        bg=tema["fondo"],
        fg=tema["texto"]
    )
    titulo.pack(pady=30)

    try:
        with open("records.txt", "r", encoding="utf-8") as archivo:
            records = archivo.readlines()
    except FileNotFoundError:
        records = []

    if records:
        texto_records = ""

        for i, record in enumerate(records, start=1):
            nombre, intentos = record.strip().split(",")

            texto_records += f"{i}. {nombre} - {intentos} intentos\n"

    else:
        texto_records = "Todavía no hay récords."

    lista = tk.Label(
        ventana_records,
        text=texto_records,
        font=("Arial", 14),
        bg=tema["fondo"],
        fg=tema["texto"],
        justify="left"
    )
    lista.pack(pady=20)

    boton_volver = tk.Button(
        ventana_records,
        text="VOLVER",
        font=("Arial", 12, "bold"),
        width=15,
        bg=tema["boton"],
        fg=tema["texto_boton"],
        activebackground=tema["boton"],
        activeforeground=tema["texto_boton"],
        relief="flat",
        bd=0,
        highlightthickness=0,
        command=ventana_records.destroy
    )
    boton_volver.pack(pady=20)
# -----------------------------#
#           Juego              #
# -----------------------------#

titulo = tk.Label(ventana,
    text="CODE BREAKER",
    font=("Arial", 32, "bold"),
    bg="#101820",
    fg="white"
)
titulo.pack(pady=(70, 40))

# -----------------------------#
#           Botones            #
# -----------------------------#

boton_jugar = tk.Button(
    ventana,
    text="JUGAR",
    font=("Arial", 14, "bold"),
    width=20,
    command=iniciar_juego
)
boton_jugar.pack(pady=8)

boton_instrucciones = tk.Button(ventana,
    text="INSTRUCCIONES",
    font=("Arial", 14, "bold"),
    width=20,
    command=mostrar_instrucciones
)
boton_instrucciones.pack(pady=8)

boton_records = tk.Button(ventana,
    text="RÉCORDS",
    font=("Arial", 14, "bold"),
    width=20,
    command=mostrar_records
)
boton_records.pack(pady=8)

boton_tema = tk.Button(ventana,
    text="TEMA",
    font=("Arial", 14, "bold"),
    width=20,
    command=mostrar_temas
)
boton_tema.pack(pady=8)

boton_salir = tk.Button(ventana,
    text="SALIR",
    font=("Arial", 14, "bold"),
    width=20,
    command=ventana.destroy
)
boton_salir.pack(pady=8)

def guardar_record(nombre, intentos):
    with open("records.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{intentos}\n")
# -----------------------------#
#            Bucle             #
# -----------------------------#

ventana.mainloop()