import tkinter as tk

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

def mostrar_instrucciones():
    instrucciones = tk.Toplevel(ventana)
    instrucciones.title("Instrucciones")
    instrucciones.geometry("700x500")
    instrucciones.resizable(False, False)
    instrucciones.configure(bg="#101820")

    titulo_instrucciones = tk.Label(
        instrucciones,
        text="INSTRUCCIONES",
        font=("Arial", 24, "bold"),
        bg="#101820",
        fg="white"
    )
    titulo_instrucciones.pack(pady=40)

    texto = tk.Label(
    instrucciones,
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
    bg="#101820",
    fg="white",
    justify="left"
    )
    texto.pack(pady=10)

    boton_volver = tk.Button(
    instrucciones,
    text="VOLVER",
    font=("Arial", 12, "bold"),
    width=15,
    command=instrucciones.destroy
    )
    boton_volver.pack(pady=30)

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

boton_jugar = tk.Button(ventana,
    text="JUGAR",
    font=("Arial", 14, "bold"),
    width=20
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
    width=20
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