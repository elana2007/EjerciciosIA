import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

class AppInmobiliaria:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Consultas pandas ia")
        self.ventana.geometry("1000x700")
        
        self.datos = self.cargar_datos()
        if self.datos is None:
            self.ventana.destroy()
            return
        
        self.pantalla_login()
        self.ventana.mainloop()
    
    def cargar_datos(self):
        try:
            df = pd.read_csv("Sacramentorealestatetransactions.csv")
            columnas_numericas = ['price', 'sq__ft', 'beds', 'baths']
            for col in columnas_numericas:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                if col != 'price':
                    df[col] = df[col].fillna(0)
            return df
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de datos")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos: {e}")
            return None
    
    def pantalla_login(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
        
        marco = ttk.Frame(self.ventana, padding=20)
        marco.pack(expand=True)
        
        ttk.Label(marco, text="Sistema de Consultas", font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(marco, text="Usuario:").pack(pady=5)
        self.usuario_entry = ttk.Entry(marco, width=25)
        self.usuario_entry.pack(pady=5)
        
        ttk.Label(marco, text="Contraseña:").pack(pady=5)
        self.password_entry = ttk.Entry(marco, show="*", width=25)
        self.password_entry.pack(pady=5)
        
        botones_frame = ttk.Frame(marco)
        botones_frame.pack(pady=15)
        
        ttk.Button(botones_frame, text="Entrar", command=self.verificar_login).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_frame, text="Salir", command=self.ventana.destroy).pack(side=tk.LEFT, padx=5)
        
        marco.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def verificar_login(self):
        usuario_correcto = "sami"
        password_correcto = "sami123"
        
        if (self.usuario_entry.get() == usuario_correcto and 
            self.password_entry.get() == password_correcto):
            self.pantalla_consultas()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.usuario_entry.focus_set()
    
    def pantalla_consultas(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
        
        marco_principal = ttk.Frame(self.ventana)
        marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        marco_controles = ttk.Frame(marco_principal)
        marco_controles.pack(fill=tk.X, pady=10)
        
        self.tipo_consulta = tk.StringVar()
        opciones = [
            "Promedio de precio por ciudad",
            "Propiedades más caras por tipo",
            "Cantidad de propiedades por ciudad",
            "Propiedades con +3 habitaciones",
            "Propiedades grandes (+2000 pies)",
            "Propiedades baratas (<$100k)",
            "Estadísticas de precios",
            "Tipos de propiedad",
            "Más baños que habitaciones",
            "Top 10 propiedades más caras"
        ]
        
        combo = ttk.Combobox(
            marco_controles,
            textvariable=self.tipo_consulta,
            values=opciones,
            state="readonly",
            width=30
        )
        combo.pack(side=tk.LEFT, padx=5)
        combo.current(0)
        
        ttk.Button(
            marco_controles,
            text="Ejecutar",
            command=self.hacer_consulta
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            marco_controles,
            text="Cerrar sesión",
            command=self.pantalla_login
        ).pack(side=tk.LEFT, padx=5)
        
        self.marco_resultados = ttk.Frame(marco_principal)
        self.marco_resultados.pack(fill=tk.BOTH, expand=True)
        
        self.hacer_consulta()
    
    def hacer_consulta(self):
        for widget in self.marco_resultados.winfo_children():
            widget.destroy()
        
        consulta = self.tipo_consulta.get()
        
        try:
            if consulta == "Promedio de precio por ciudad":
                resultado = self.datos.groupby('city')['price'].mean().round(2)
                resultado = resultado.sort_values(ascending=False)
                texto = "Precio promedio por ciudad:\n\n" + resultado.to_string()
            
            elif consulta == "Propiedades más caras por tipo":
                resultado = self.datos.groupby('type')['price'].max()
                resultado = resultado.sort_values(ascending=False)
                texto = "Precio máximo por tipo de propiedad:\n\n" + resultado.to_string()
            
            elif consulta == "Cantidad de propiedades por ciudad":
                resultado = self.datos['city'].value_counts()
                texto = "Cantidad de propiedades por ciudad:\n\n" + resultado.to_string()
            
            elif consulta == "Propiedades con +3 habitaciones":
                resultado = self.datos[self.datos['beds'] > 3]
                texto = f"Propiedades con más de 3 habitaciones ({len(resultado)} encontradas):\n\n" + resultado[['street', 'city', 'beds', 'price']].to_string(index=False)
            
            elif consulta == "Propiedades grandes (+2000 pies)":
                resultado = self.datos[self.datos['sq__ft'] > 2000]
                texto = f"Propiedades grandes (+2000 pies cuadrados) ({len(resultado)} encontradas):\n\n" + resultado[['street', 'city', 'sq__ft', 'price']].to_string(index=False)
            
            elif consulta == "Propiedades baratas (<$100k)":
                resultado = self.datos[self.datos['price'] < 100000]
                texto = f"Propiedades baratas (<$100,000) ({len(resultado)} encontradas):\n\n" + resultado[['street', 'city', 'price']].to_string(index=False)
            
            elif consulta == "Estadísticas de precios":
                resultado = self.datos['price'].describe().round(2)
                texto = "Estadísticas de precios:\n\n" + resultado.to_string()
            
            elif consulta == "Tipos de propiedad":
                resultado = self.datos['type'].value_counts()
                texto = "Distribución de tipos de propiedad:\n\n" + resultado.to_string()
            
            elif consulta == "Más baños que habitaciones":
                resultado = self.datos[self.datos['baths'] > self.datos['beds']]
                texto = f"Propiedades con más baños que habitaciones ({len(resultado)} encontradas):\n\n" + resultado[['street', 'city', 'beds', 'baths', 'price']].to_string(index=False)
            
            elif consulta == "Top 10 propiedades más caras":
                resultado = self.datos.nlargest(10, 'price')
                texto = "Top 10 propiedades más caras:\n\n" + resultado[['street', 'city', 'price']].to_string(index=False)
            
            else:
                texto = "Seleccione una consulta válida"
            
            area_texto = tk.Text(self.marco_resultados, wrap=tk.WORD)
            area_texto.pack(fill=tk.BOTH, expand=True)
            
            scrollbar = ttk.Scrollbar(area_texto)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            scrollbar.config(command=area_texto.yview)
            area_texto.config(yscrollcommand=scrollbar.set)
            
            area_texto.insert(tk.END, texto)
            area_texto.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

if __name__ == "__main__":
    app = AppInmobiliaria()