import tkinter as tk
from tkinter import ttk
from sympy import symbols, integrate, pretty


# Función para calcular la integral definida
def calcular_integral_definida():
    f = entrada_funcion.get()  # Obtiene la función ingresada por el usuario
    x = symbols('x')  # Define el símbolo para la variable de integración
    x0 = entrada_limite_inferior.get()  # Obtiene el límite inferior
    x1 = entrada_limite_superior.get()  # Obtiene el límite superior

    try:
        res = integrate(f, (x, x0, x1))  # Calcula la integral definida
        pretty_res = pretty(res, use_unicode=True)  # Formatea el resultado de manera atractiva
        resultado.config(text=f' {pretty_res}')
    except:
        resultado.config(text='Error en la función')

# Función para agregar un caracter al campo de entrada
def agregar_caracter(caracter):
    entrada_funcion.insert(tk.END, caracter)

# Función para borrar un caracter del campo de entrada
def borrar_caracter():
    entrada_funcion.delete(len(entrada_funcion.get()) - 1, tk.END)

# Función para borrar todo el contenido del campo de entrada
def borrar_todo():
    entrada_funcion.delete(0, tk.END)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora de Integrales Definidas")

# Crear un estilo personalizado
style = ttk.Style()
style.configure('TButton', padding=5, font=("Helvetica", 12))
style.configure('TFrame', background='#F0F0F0')
style.configure('TLabel', font=("Helvetica", 12))

# Cuadro de entrada y resultado
marco_principal = ttk.Frame(ventana)
marco_principal.pack(padx=10, pady=10)

# Símbolo de integral
simbolo_integral = ttk.Label(marco_principal, text="∫", font=("Times", 24))
simbolo_integral.grid(row=1, column=0, padx=(0, 1), rowspan=2, sticky=tk.W)

etiqueta_funcion = ttk.Label(marco_principal, text="Ingrese la función f(x):")
etiqueta_funcion.grid(row=0, column=2, columnspan=3)

entrada_funcion = ttk.Entry(marco_principal)
entrada_funcion.grid(row=1, column=2, columnspan=3)

# Cuadro de entrada para límite inferior
entrada_limite_inferior = ttk.Entry(marco_principal, width=3)
entrada_limite_inferior.grid(row=2, column=0, sticky=tk.E)

# Cuadro de entrada para límite superior
entrada_limite_superior = ttk.Entry(marco_principal, width=3)
entrada_limite_superior.grid(row=1, column=0, sticky=tk.E)

# Botones numéricos y de operación
botones = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '^', '/', 'sin(x)',
    'cos(x)', 'tan(x)',
    'x'
]

# Posiciones de los botones
boton_posiciones = [
    (3, 0), (3, 1), (3, 2), (3, 3),
    (4, 0), (4, 1), (4, 2), (4, 3),
    (5, 0), (5, 1), (5, 2), (5, 3),
    (6, 1), (6, 2), (6, 3), (6, 0),
    (7, 1), (7, 2),
    (7, 0)
]

for i, boton_text in enumerate(botones):
    boton = ttk.Button(marco_principal, text=boton_text, width=5, command=lambda bt=boton_text: agregar_caracter(bt))
    boton.grid(row=boton_posiciones[i][0], column=boton_posiciones[i][1], padx=5, pady=5)

# Botón para borrar
boton_borrar = ttk.Button(marco_principal, text="Borrar", width=5, command=borrar_caracter)
boton_borrar.grid(row=8, column=0, padx=5, pady=5)

# Botón para borrar todo
boton_borrar_todo = ttk.Button(marco_principal, text="C", width=5, command=borrar_todo)
boton_borrar_todo.grid(row=8, column=1, padx=5, pady=5)

# Botón para calcular
boton_calcular = ttk.Button(marco_principal, text="Calcular Integral", command=calcular_integral_definida)
boton_calcular.grid(row=8, column=2, columnspan=2, padx=5, pady=5)

# Ajustes de estilo para el resultado
resultado = ttk.Label(marco_principal, text="", justify=tk.CENTER)
resultado.grid(row=9, column=0, columnspan=5, pady=(10, 0))


# Iniciar la aplicación
ventana.mainloop()
