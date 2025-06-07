import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

ventana = tk.Tk()
ventana.title("FUNCIONES LINEALES")
ventana.geometry("400x300")

def graficar():
    try:
        m = float(entrada_m.get())  
        b = float(entrada_b.get())  
        
        x = np.linspace(0, 10, 400) #0 a 10 la graf
        y = m * x + b  
        
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f"f(x) = {m}x + {b}", color="red") #DIBUJA graf
        plt.axhline(0, color="black", linewidth=0.9)  # ejes x
        plt.axvline(0, color="black", linewidth=0.9)  # y
        plt.title("Gráfica Insana")
        plt.xlabel("eje x")# nom ejes
        plt.ylabel("eje y")# nom ejes
        plt.legend()
        plt.grid(True)#cuadricula
        plt.show()
        
    except ValueError:
        messagebox.showerror("error", "Ingresa numeros validos")

tk.Label(ventana, text="Ingresa la pendiente (m): ").pack(pady=15)
entrada_m = tk.Entry(ventana) # tk entry crea un cuadro text 
entrada_m.pack(pady=5)

tk.Label(ventana, text="Ingresa elk termino independiente (b): ").pack(pady=15)
entrada_b = tk.Entry(ventana)
entrada_b.pack(pady=5)

boton_graficar = tk.Button(ventana, text="graficar", command=graficar)
boton_graficar.pack(pady=30)

ventana.mainloop()