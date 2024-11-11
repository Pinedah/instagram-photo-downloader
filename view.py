import tkinter as tk
from tkinter import scrolledtext
import time


def agregar_texto():
    texto = "Nuevo dato agregado\n"  # Aquí puedes cambiar el texto que se agregará
    etiqueta_con_scroll.insert(tk.END, texto)  # Agrega el texto al final
    etiqueta_con_scroll.yview(tk.END)  # Desplaza hacia el final para ver el texto agregado

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("INSTAGRAM PHOTO-SCRAPPER")
ventana.geometry("500x300")  # Establece el tamaño de la ventana
ventana.configure(bg="black")  # Establece el fondo de la ventana a negro
ventana.resizable(False, False)

# Configurar icono de la ventana
icono = tk.PhotoImage(file="pank.png")  # Cambia la ruta a tu archivo .ico
ventana.iconphoto(False, icono)

program_label = tk.Label(ventana, text="INSTAGRAM PHOTO-SCRAPPER", font=("Arial", 14), fg="white", bg="black")
program_label.pack(padx=10, pady=10)

# Boton para inciar el scrapping
botonIniciar = tk.Button(ventana, text="Iniciar Scrap", command=agregar_texto, fg="white", bg="black", border=2)
botonIniciar.pack(padx= 10, pady=10)

# Crear el widget de texto con scroll
etiqueta_con_scroll = scrolledtext.ScrolledText(
    ventana, 
    width=50, 
    height=15, 
    wrap=tk.WORD, 
    font=("Arial", 10), 
    bg="#333333",      # Color de fondo de la etiqueta (gris oscuro)
    fg="#FFFFFF"       # Color del texto (blanco)
)
etiqueta_con_scroll.pack(pady=20)
etiqueta_con_scroll.configure(state="normal")  # Deshabilita la edición por el usuario

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
