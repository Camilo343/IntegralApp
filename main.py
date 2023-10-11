import tkinter as tk
<<<<<<< HEAD
from tkinter import ttk
from sympy import symbols, integrate, simplify, latex, pretty


# Resto del código...

# Función para calcular la integral
def calcular_integral():
    f = entrada_funcion.get()  # Obtiene la función ingresada por el usuario
    x = symbols('x')  # Define el símbolo para la variable de integración
    try:
        res = integrate(f, x)  # Calcula la integral
        pretty_res = pretty(res, use_unicode=True)  # Formatea el resultado de manera atractiva
        resultado.config(text=f'{pretty_res}')  # Muestra la respuesta en la interfaz
    except:
        resultado.config(text='Error en la función')  # Manejo de errores si la función no es válida
=======
from tkinter import ttk, simpledialog
from sympy import symbols, diff, integrate, pretty

def configurar_ventana():
    ventana.title("Calculadora de Matemáticas")
    ventana.geometry('300x400')

def configurar_botones():
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

def calcular():
    f = entrada_funcion.get()  # Obtiene la función ingresada por el usuario
    x = symbols('x')  # Define el símbolo para la variable de integración
   
    if operacion_var.get() == 'Integral':
        try:
            res = integrate(f, x)
        except:
            resultado.config(text='Error en la función')
            return
    elif operacion_var.get() == 'Derivada':
        try:
            res = diff(f, x)
        except:
            resultado.config(text='Error en la función')
            return
    elif operacion_var.get() == 'Derivada definida':
        a = simpledialog.askfloat("Limite inferior", "Ingrese el límite inferior:")
        b = simpledialog.askfloat("Limite superior", "Ingrese el límite superior:")
        if a is None or b is None:
            return
        try:
            res = diff(f, x).subs(x, b) - diff(f, x).subs(x, a)
        except:
            resultado.config(text='Error en la función')
            return
   
    pretty_res = pretty(res, use_unicode=True)
    resultado.config(text=f'{pretty_res}')
>>>>>>> 18f57398aa95eeb97ec8724bf53f208de6a1ed7e

# Función para agregar un caracter al campo de entrada
def agregar_caracter(caracter):
    entrada_funcion.insert(tk.END, caracter)  # Inserta el caracter en el campo de entrada

# Función para borrar un caracter del campo de entrada
def borrar_caracter():
    entrada_funcion.delete(len(entrada_funcion.get()) - 1, tk.END)  # Borra el último caracter del campo de entrada

def limpiar_entrada():
    entrada_funcion.delete(0, tk.END)

# Crear una ventana
ventana = tk.Tk()
configurar_ventana()

# Crear un estilo personalizado
style = ttk.Style()
style.configure('TButton', padding=5, font=("Helvetica", 12))
style.configure('TFrame', background='#F0F0F0')
style.configure('TLabel', font=("Helvetica", 12))

# Cuadro de entrada y resultado
marco_principal = ttk.Frame(ventana)
marco_principal.pack(padx=10, pady=10)

<<<<<<< HEAD
# Símbolo de integral
simbolo_integral = ttk.Label(marco_principal, text="∫", font=("Times", 24))
simbolo_integral.grid(row=1, column=0, sticky=tk.E, padx=(0, 5))

=======
# Configurar Widgets
>>>>>>> 18f57398aa95eeb97ec8724bf53f208de6a1ed7e
etiqueta_funcion = ttk.Label(marco_principal, text="Ingrese la función f(x):")
etiqueta_funcion.grid(row=0, column=0, columnspan=5)

entrada_funcion = ttk.Entry(marco_principal, width=25)
entrada_funcion.grid(row=1, column=0, columnspan=5, pady=(0, 10))

# Elección de operación (Integral, Derivada, Derivada definida)
operacion_var = ttk.Combobox(marco_principal, values=['Integral', 'Derivada', 'Derivada definida'], state="readonly")
operacion_var.set('Integral')  # Valor por defecto
operacion_var.grid(row=2, column=0, columnspan=5, pady=(0, 10))

resultado = ttk.Label(marco_principal, text="", wraplength=250)
resultado.grid(row=6, column=0, columnspan=5, pady=(10, 0))

configurar_botones()

# Botón para calcular
boton_calcular = ttk.Button(marco_principal, text="Calcular", command=calcular)
boton_calcular.grid(row=7, column=0, columnspan=3, pady=5)

# Botón para limpiar
boton_limpiar = ttk.Button(marco_principal, text="Limpiar", command=limpiar_entrada)
boton_limpiar.grid(row=7, column=3, columnspan=2, pady=5)

<<<<<<< HEAD
# Iniciar la aplicación
=======
# In

inciar la aplicación
>>>>>>> 18f57398aa95eeb97ec8724bf53f208de6a1ed7e
ventana.mainloop()
