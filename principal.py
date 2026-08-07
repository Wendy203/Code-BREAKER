import tkinter as tk

# -----------------------------
#            Menu
# -----------------------------

ventana = tk.Tk()
ventana.title("Code BREAKER")
ventana.geometry("800x500")
ventana.resizable(False, False)
ventana.configure(bg="#101820")

# -----------------------------
#           Juego
# -----------------------------

titulo = tk.Label(ventana,
    text="CODE BREAKER",
    font=("Arial", 32, "bold"),
    bg="#101820",
    fg="white"
)
titulo.pack(pady=(70, 40))

# -----------------------------
#         Botones
# -----------------------------

boton_jugar = tk.Button(ventana,
    text="JUGAR",
    font=("Arial", 14, "bold"),
    width=20
)
boton_jugar.pack(pady=8)

boton_instrucciones = tk.Button(ventana,
    text="INSTRUCCIONES",
    font=("Arial", 14, "bold"),
    width=20
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

# -----------------------------
#          Ejecutar
# -----------------------------

ventana.mainloop()