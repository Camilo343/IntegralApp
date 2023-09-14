import tkinter as tk
from sympy import *

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

# Cuadro de entrada y resultado
marco_principal = tk.Frame(ventana)
marco_principal.pack(padx=10, pady=10)

etiqueta_funcion = tk.Label(marco_principal, text="Ingrese la función f(x):")
etiqueta_funcion.grid(row=0, column=0, columnspan=5)

entrada_funcion = tk.Entry(marco_principal)
entrada_funcion.grid(row=1, column=0, columnspan=5)

resultado = tk.Label(marco_principal, text="")
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
        boton = tk.Button(marco_principal, text=boton_text, width=5, height=2,
                          command=borrar_caracter)
    else:
        boton = tk.Button(marco_principal, text=boton_text, width=5, height=2,
                          command=lambda bt=boton_text: agregar_caracter(bt))
    boton.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botón para calcular
boton_calcular = tk.Button(marco_principal, text="Calcular Integral", command=calcular_integral)
boton_calcular.grid(row=row, column=col, padx=5, pady=5, columnspan=4)

# Estilo básico para los botones
for widget in marco_principal.winfo_children():
    if isinstance(widget, tk.Button):
        widget.configure(font=("Helvetica", 12), bg="#E0E0E0")

# Iniciar la aplicación
ventana.mainloop()
