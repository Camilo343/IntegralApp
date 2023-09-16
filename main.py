import tkinter as tk
from tkinter import ttk  # Importa ttk
from sympy import *
#pollito asado
#cualquier cosa 
def calcular_integral():
    f = entrada_funcion.get()
    x = symbols('x')
    try:
        res = integrate(f, x)
        resultado.config(text=f'La respuesta es {res}')
    except:
        resultado.config(text='Error en la función')

def agregar_caracter(caracter):
    entrada_funcion.insert(tk.END, caracter)

def borrar_caracter():
    entrada_funcion.delete(len(entrada_funcion.get()) - 1, tk.END)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora de Integrales")

# Crear un estilo personalizado
style = ttk.Style()
style.configure('TButton', padding=5, font=("Helvetica", 12))
style.configure('TFrame', background='#F0F0F0')
style.configure('TLabel', font=("Helvetica", 12))

# Cuadro de entrada y resultado
marco_principal = ttk.Frame(ventana)
marco_principal.pack(padx=10, pady=10)

etiqueta_funcion = ttk.Label(marco_principal, text="Ingrese la función f(x):")
etiqueta_funcion.grid(row=0, column=0, columnspan=5)

entrada_funcion = ttk.Entry(marco_principal)
entrada_funcion.grid(row=1, column=0, columnspan=5)

resultado = ttk.Label(marco_principal, text="")
resultado.grid(row=2, column=0, columnspan=5)

# Botones numéricos y de operación
botones = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '^', '/', 'Borrar',
    'x'
]

row, col = 3, 0
for boton_text in botones:
    if boton_text == 'Borrar':
        boton = ttk.Button(marco_principal, text=boton_text, width=5, command=borrar_caracter)
    else:
        boton = ttk.Button(marco_principal, text=boton_text, width=5, command=lambda bt=boton_text: agregar_caracter(bt))
    boton.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botón para calcular
boton_calcular = ttk.Button(marco_principal, text="Calcular Integral", command=calcular_integral)
boton_calcular.grid(row=row, column=col, padx=5, pady=5, columnspan=4)

# Estilo personalizado para los botones
for widget in marco_principal.winfo_children():
    if isinstance(widget, ttk.Button):
        widget.configure(style='TButton')

# Iniciar la aplicación
ventana.mainloop()