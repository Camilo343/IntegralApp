import tkinter as tk
from tkinter import messagebox
import os

def abrir_calculadora_indefinidas():
    os.system("python integralesIndefinidas.py")

def abrir_calculadora_definidas():
    os.system("python integralesDefinidas.py")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Integrales")

# Crear etiquetas
etiqueta = tk.Label(ventana, text="Selecciona el tipo de integral:")
etiqueta.pack(pady=10)

# Botones para seleccionar el tipo de integral
boton_indefinidas = tk.Button(ventana, text="Integrales Indefinidas", command=abrir_calculadora_indefinidas)
boton_indefinidas.pack(pady=10)

boton_definidas = tk.Button(ventana, text="Integrales Definidas", command=abrir_calculadora_definidas)
boton_definidas.pack(pady=10)

# Función para mostrar información de ayuda
def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Este programa permite calcular integrales indefinidas y definidas. Selecciona el tipo de integral y haz clic en el botón correspondiente.")

# Botón de ayuda
boton_ayuda = tk.Button(ventana, text="Ayuda", command=mostrar_ayuda)
boton_ayuda.pack(pady=10)

ventana.mainloop()
inciar la aplicación
>>>>>>> 18f57398aa95eeb97ec8724bf53f208de6a1ed7e
ventana.mainloop()
