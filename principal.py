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
        "boton": "#001A00",
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
titulo_temas = None

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
        return

    ventana_instrucciones = tk.Toplevel(ventana)
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
    ventana_juego.title("Nueva partida")
    ventana_juego.geometry("400x300")
    ventana_juego.resizable(False, False)

    ventana_juego.configure(
        bg=tema["fondo"]
    )

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
        command=lambda: crear_partida(int(longitud.get()))
    )

    boton_iniciar.pack(pady=20)

def crear_partida(longitud):
    global codigo_secreto
    global intentos
    global ventana_juego

    codigo_secreto = "".join(
        random.sample("0123456789", longitud)
    )

    intentos = 0

    # Aquí después construiremos la pantalla del juego
    print("Código secreto:", codigo_secreto)

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
    width=20
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

# -----------------------------#
#            Bucle             #
# -----------------------------#

ventana.mainloop()