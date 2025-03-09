import tkinter as tk
from tkinter import ttk, messagebox

# Funciones para cada ejercicio

def calcular_aumento():
    """Calcula el aumento de sueldo basado en el sueldo ingresado."""
    try:
        sueldo = float(entry_sueldo.get())
        aumento = sueldo * 0.15 if sueldo < 4000 else sueldo * 0.08
        lbl_resultado.config(text=f"Aumento: {aumento:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def calcular_descuento():
    """Calcula el descuento para niños menores de 10 años en un parque de diversiones."""
    try:
        edad = int(entry_edad.get())
        total = 50 * 0.75 if edad < 10 else 50
        lbl_descuento.config(text=f"Total a pagar: {total:.2f} soles")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def calcular_descuento_octubre():
    """Aplica un descuento del 15% si el mes es octubre."""
    try:
        mes = entry_mes.get().strip().lower()
        importe = float(entry_importe.get())
        importe = importe * 0.85 if mes == "octubre" else importe
        lbl_importe.config(text=f"Total a cobrar: {importe:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos")

def comprobar_menor_10():
    """Verifica si el número ingresado es menor que 10."""
    try:
        num = int(entry_menor_10.get())
        if num < 10:
            lbl_menor_10.config(text=f"Número válido: {num}")
        else:
            messagebox.showerror("Error", "Ingrese un número menor que 10")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def comprobar_rango():
    """Verifica si el número ingresado está en el rango (0, 20)."""
    try:
        num = int(entry_rango.get())
        if 0 < num < 20:
            lbl_rango.config(text=f"Número válido: {num}")
        else:
            messagebox.showerror("Error", "Ingrese un número entre 1 y 19")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def contar_intentos():
    """Cuenta los intentos hasta que se ingrese un número válido en el rango (0, 20)."""
    intentos = 0
    while True:
        try:
            num = int(entry_contador.get())
            intentos += 1
            if 0 < num < 20:
                lbl_contador.config(text=f"Número válido: {num}, Intentos: {intentos}")
                break
            else:
                messagebox.showerror("Error", "Ingrese un número entre 1 y 19")
                entry_contador.delete(0, tk.END)  # olimpiar el campo para un nuevo intento
                return  # salir de la función para permitir un nuevo intento
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
            entry_contador.delete(0, tk.END)  # limpiar el campo para un nuevo intento
            return  # alir de la función para permitir un nuevo intento

def suma_n():
    """Calcula la suma de los primeros n números enteros positivos."""
    try:
        n = int(entry_n.get())
        suma = sum(range(1, n+1))
        lbl_suma_n.config(text=f"Suma de 1 a {n}: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def suma_hasta_cero():
    """Suma números ingresados hasta que se ingrese el número 0."""
    try:
        num1 = float(entry_suma_cero1.get())
        num2 = float(entry_suma_cero2.get())
        suma_hasta_cero.suma += num1 + num2

        if num1 == 0 or num2 == 0:
            messagebox.showinfo("Suma Finalizada", "Se ingresó un 0. Suma finalizada.")
            suma_hasta_cero.suma = 0  # reiniciar la suma
            entry_suma_cero1.config(state=tk.DISABLED)  # deshabilitar campos
            entry_suma_cero2.config(state=tk.DISABLED)
        else:
            lbl_suma_cero.config(text=f"Suma parcial: {suma_hasta_cero.suma}")
            entry_suma_cero1.delete(0, tk.END)  # limpiar campos
            entry_suma_cero2.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

suma_hasta_cero.suma = 0  # variable global para almacenar la suma

def reiniciar_suma_cero():
    """Reinicia la suma y habilita los campos para ingresar nuevos números."""
    suma_hasta_cero.suma = 0
    entry_suma_cero1.config(state=tk.NORMAL)
    entry_suma_cero2.config(state=tk.NORMAL)
    entry_suma_cero1.delete(0, tk.END)
    entry_suma_cero2.delete(0, tk.END)
    lbl_suma_cero.config(text="Resultado: ")

def suma_hasta_100():
    """Suma números ingresados hasta que la suma supere 100."""
    try:
        num1 = float(entry_suma_100_1.get())
        num2 = float(entry_suma_100_2.get())
        suma_hasta_100.suma += num1 + num2

        if suma_hasta_100.suma > 100:
            messagebox.showinfo("Suma Finalizada", "Suma superó 100. Suma finalizada.")
            suma_hasta_100.suma = 0  # reiniciar la suma
            entry_suma_100_1.config(state=tk.DISABLED)  # deshabilitar campos
            entry_suma_100_2.config(state=tk.DISABLED)
        else:
            lbl_suma_100.config(text=f"Suma parcial: {suma_hasta_100.suma}")
            entry_suma_100_1.delete(0, tk.END)  # limpiar campos
            entry_suma_100_2.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

suma_hasta_100.suma = 0  # variable global para almacenar la suma

def reiniciar_suma_100():
    """Reinicia la suma y habilita los campos para ingresar nuevos números."""
    suma_hasta_100.suma = 0
    entry_suma_100_1.config(state=tk.NORMAL)
    entry_suma_100_2.config(state=tk.NORMAL)
    entry_suma_100_1.delete(0, tk.END)
    entry_suma_100_2.delete(0, tk.END)
    lbl_suma_100.config(text="Resultado: ")

def calcular_pago_total():
    """Calcula el pago total de un trabajador, incluyendo horas normales, extras y bonificación por hijos."""
    try:
        nombre = entry_nombre.get()
        horas_normales = float(entry_horas_normales.get())
        horas_extras = float(entry_horas_extras.get())
        hijos = int(entry_hijos.get())
        
        pago_horas_normales = horas_normales * 10  # pago por hora normal
        pago_horas_extras = horas_extras * 15  # pago por hora extra
        bonificacion_hijos = hijos * 0.5  # bonificación por hijo
        
        pago_total = pago_horas_normales + pago_horas_extras + bonificacion_hijos
        
        lbl_pago_total.config(text=f"Nombre: {nombre}\nPago horas normales: {pago_horas_normales:.2f}\nPago horas extras: {pago_horas_extras:.2f}\nBonificación por hijos: {bonificacion_hijos:.2f}\nPago total: {pago_total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos")

#  ventana principal
root = tk.Tk()
root.title("Ejercicios")
notebook = ttk.Notebook(root)  # notebook para las pestañas
frames = [ttk.Frame(notebook) for _ in range(10)]  # 10 frames 
labels = [
    "Aumento Sueldo", "Descuento Juego", "Descuento Octubre", "Menor a 10", 
    "Rango 0-20", "Contador Intentos", "Suma N", "Suma Hasta 0", "Suma Hasta 100", "Pago Total"
]

# frame al notebbok
for i, frame in enumerate(frames):
    notebook.add(frame, text=labels[i])
notebook.pack(expand=True, fill="both")  # mostrar el notebook

# Función para agregar widgets comunes
def agregar_widgets(frame, texto, funcion, variable):
    entry = ttk.Entry(frame)
    entry.pack()
    ttk.Button(frame, text=texto, command=funcion).pack()
    label = ttk.Label(frame, text="Resultado: ")
    label.pack()
    return entry, label

# pestaña 1 Aumento Sueldo
entry_sueldo, lbl_resultado = agregar_widgets(frames[0], "Calcular Aumento", calcular_aumento, None)

# pestaña 2 Descuento Juego
entry_edad, lbl_descuento = agregar_widgets(frames[1], "Calcular Descuento", calcular_descuento, None)

# pestaña 3 Descuento Octubre
ttk.Label(frames[2], text="Mes (octubre para descuento):").pack()
entry_mes = ttk.Entry(frames[2])
entry_mes.pack()
ttk.Label(frames[2], text="Importe:").pack()
entry_importe = ttk.Entry(frames[2])
entry_importe.pack()
ttk.Button(frames[2], text="Calcular Descuento Octubre", command=calcular_descuento_octubre).pack()
lbl_importe = ttk.Label(frames[2], text="Resultado: ")
lbl_importe.pack()

# pestaña 4 Menor a 10
entry_menor_10, lbl_menor_10 = agregar_widgets(frames[3], "Verificar", comprobar_menor_10, None)

# pestaña 5 Rango 0-20
entry_rango, lbl_rango = agregar_widgets(frames[4], "Verificar", comprobar_rango, None)

# pestaña 6 Contador Intentos
entry_contador, lbl_contador = agregar_widgets(frames[5], "Verificar", contar_intentos, None)

# pestaña 7 Suma N
entry_n, lbl_suma_n = agregar_widgets(frames[6], "Calcular Suma", suma_n, None)

# pestaña 8 Suma Hasta 0
ttk.Label(frames[7], text="Ingrese dos números a sumar (0 para terminar):").pack()
entry_suma_cero1 = ttk.Entry(frames[7])
entry_suma_cero1.pack()
entry_suma_cero2 = ttk.Entry(frames[7])
entry_suma_cero2.pack()
ttk.Button(frames[7], text="Sumar", command=suma_hasta_cero).pack()
ttk.Button(frames[7], text="Reiniciar", command=reiniciar_suma_cero).pack()
lbl_suma_cero = ttk.Label(frames[7], text="Resultado: ")
lbl_suma_cero.pack()

# pestaña 9 Suma Hasta 100
ttk.Label(frames[8], text="Ingrese dos números a sumar (suma > 100 para terminar):").pack()
entry_suma_100_1 = ttk.Entry(frames[8])
entry_suma_100_1.pack()
entry_suma_100_2 = ttk.Entry(frames[8])
entry_suma_100_2.pack()
ttk.Button(frames[8], text="Sumar", command=suma_hasta_100).pack()
ttk.Button(frames[8], text="Reiniciar", command=reiniciar_suma_100).pack()
lbl_suma_100 = ttk.Label(frames[8], text="Resultado: ")
lbl_suma_100.pack()

# pestaña 10 Pago Total
ttk.Label(frames[9], text="Nombre del trabajador:").pack()
entry_nombre = ttk.Entry(frames[9])
entry_nombre.pack()
ttk.Label(frames[9], text="Horas normales trabajadas:").pack()
entry_horas_normales = ttk.Entry(frames[9])
entry_horas_normales.pack()
ttk.Label(frames[9], text="Horas extras trabajadas:").pack()
entry_horas_extras = ttk.Entry(frames[9])
entry_horas_extras.pack()
ttk.Label(frames[9], text="Número de hijos:").pack()
entry_hijos = ttk.Entry(frames[9])
entry_hijos.pack()
ttk.Button(frames[9], text="Calcular Pago Total", command=calcular_pago_total).pack()
lbl_pago_total = ttk.Label(frames[9], text="Resultado: ")
lbl_pago_total.pack()

# ejecutar la ventana principal
root.mainloop()