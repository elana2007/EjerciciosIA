import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from pandastable import Table

class Aplicacion:
    def __init__(self):
        # configuracion de la ventana pincipal
        self.root = tk.Tk()
        self.root.title("Sistema de Consultas Inmobiliarias")
        self.root.geometry("1100x750")
        
        # config del estilo
        self.setup_styles()
        
        #  cargamos los datos
        self.df = self.cargar_datos()
        if self.df is None:
            self.root.destroy()
            return
            
        # login 
        self.setup_login()
        
        self.root.mainloop()
    
    def setup_styles(self):
        """Configura los estilos visuales de la aplicación"""
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('Title.TLabel', font=('Arial', 12, 'bold'))
    
    def cargar_datos(self):
        """Carga y prepara los datos del archivo CSV"""
        try:
            df = pd.read_csv("Sacramentorealestatetransactions.csv")
            
            # se limpian y convierten los datos
            numeric_cols = ['price', 'sq__ft', 'beds', 'baths']
            for col in numeric_cols:
                # se convierten a numerico y se  manejan valores faltantes o inválidos
                df[col] = pd.to_numeric(df[col], errors='coerce')
                # rellenar na con 0 para columnas vacias menos el precio
                if col != 'price':
                    df[col] = df[col].fillna(0)
            
            return df
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo 'Sacramentorealestatetransactions.csv' no encontrado.")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
            return None
    
    def setup_login(self):
        """Configura la interfaz de login"""
        self.clear_window()
        
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        login_frame = ttk.Frame(main_frame)
        login_frame.pack(pady=50)
        
        ttk.Label(
            login_frame, 
            text="Sistema de Consultas Inmobiliarias", 
            style='Title.TLabel'
        ).grid(row=0, columnspan=2, pady=10)
        
        ttk.Label(login_frame, text="Usuario:").grid(row=1, column=0, pady=5, sticky=tk.E)
        self.usuario = ttk.Entry(login_frame, width=25)
        self.usuario.grid(row=1, column=1, pady=5, sticky=tk.W)
        
        ttk.Label(login_frame, text="Contraseña:").grid(row=2, column=0, pady=5, sticky=tk.E)
        self.password = ttk.Entry(login_frame, show="*", width=25)
        self.password.grid(row=2, column=1, pady=5, sticky=tk.W)
        
        btn_frame = ttk.Frame(login_frame)
        btn_frame.grid(row=3, columnspan=2, pady=15)
        
        ttk.Button(
            btn_frame, 
            text="Iniciar Sesión", 
            command=self.validar_login
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            btn_frame, 
            text="Salir", 
            command=self.root.destroy
        ).pack(side=tk.LEFT, padx=5)
        
        # centrar frame login
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def validar_login(self):
        """Validar credenciales de login"""
        # contraseña y usuario
        usuario_correcto = "sami"
        password_correcto = "sami123"
        
        usuario = self.usuario.get()
        password = self.password.get()
        
        if usuario == usuario_correcto and password == password_correcto:
            self.setup_consultas()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            self.usuario.focus_set()
    
    def setup_consultas(self):
        """Configura la interfaz de consultas"""
        self.clear_window()
        
        # frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # frame de controles
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(control_frame, text="Tipo de Consulta:").pack(side=tk.LEFT, padx=5)
        
        self.consulta_var = tk.StringVar()
        consultas = [
            "Promedio de precio por ciudad",
            "Máximo precio por tipo de propiedad",
            "Cantidad de propiedades por ciudad",
            "Propiedades con más de 3 habitaciones",
            "Propiedades con más de 2000 pies cuadrados",
            "Propiedades con precio < $100,000",
            "Estadísticas descriptivas de precios",
            "Distribución de tipos de propiedad",
            "Propiedades con más baños que habitaciones",
            "Top 10 propiedades más caras"
        ]
        
        self.combo = ttk.Combobox(
            control_frame,
            textvariable=self.consulta_var,
            values=consultas,
            state="readonly",
            width=40,
            font=('Arial', 10)
        )
        self.combo.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        self.combo.current(0)
        
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(
            btn_frame,
            text="Ejecutar Consulta",
            command=self.ejecutar_consulta
        ).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(
            btn_frame,
            text="Cerrar Sesión",
            command=self.setup_login
        ).pack(side=tk.LEFT, padx=2)
        
        # frame de resultados
        self.result_frame = ttk.Frame(main_frame)
        self.result_frame.pack(fill=tk.BOTH, expand=True)
        
        # ejecutar consulta 1 automaticamente als abrir el programa
        self.ejecutar_consulta()
    
    def ejecutar_consulta(self):
        """Ejecuta la consulta seleccionada"""
        if not hasattr(self, 'result_frame'):
            return
            
        # limpiar resultados anteriores
        for widget in self.result_frame.winfo_children():
            widget.destroy()
            
        consulta = self.consulta_var.get()
        
        try:
            if consulta == "Promedio de precio por ciudad":
                res = self.df.groupby('city')['price'].mean().sort_values(ascending=False).reset_index()
                res.columns = ['Ciudad', 'Precio Promedio']
                res['Precio Promedio'] = res['Precio Promedio'].round(2).apply(lambda x: f"${x:,.2f}")
            
            elif consulta == "Máximo precio por tipo de propiedad":
                res = self.df.groupby('type')['price'].max().sort_values(ascending=False).reset_index()
                res.columns = ['Tipo de Propiedad', 'Precio Máximo']
                res['Precio Máximo'] = res['Precio Máximo'].apply(lambda x: f"${x:,.2f}")
            
            elif consulta == "Cantidad de propiedades por ciudad":
                res = self.df['city'].value_counts().sort_values(ascending=False).reset_index()
                res.columns = ['Ciudad', 'Cantidad de Propiedades']
            
            elif consulta == "Propiedades con más de 3 habitaciones":
                res = self.df[self.df['beds'] > 3].copy()
                res = res.sort_values('price', ascending=False)
            
            elif consulta == "Propiedades con más de 2000 pies cuadrados":
                res = self.df[self.df['sq__ft'] > 2000].copy()
                res = res.sort_values('price', ascending=False)
            
            elif consulta == "Propiedades con precio < $100,000":
                res = self.df[self.df['price'] < 100000].copy()
                res = res.sort_values('price', ascending=True)
            
            elif consulta == "Estadísticas descriptivas de precios":
                stats = self.df['price'].describe().to_frame().round(2)
                stats.index = ['Cantidad', 'Media', 'Desv. Estándar', 'Mínimo', '25%', '50%', '75%', 'Máximo']
                stats.columns = ['Precio']
                stats['Precio'] = stats['Precio'].apply(lambda x: f"${x:,.2f}")
                res = stats
            
            elif consulta == "Distribución de tipos de propiedad":
                res = self.df['type'].value_counts().reset_index()
                res.columns = ['Tipo de Propiedad', 'Cantidad']
                res['Porcentaje'] = (res['Cantidad'] / res['Cantidad'].sum() * 100).round(2).astype(str) + '%'
            
            elif consulta == "Propiedades con más baños que habitaciones":
                res = self.df[self.df['baths'] > self.df['beds']].copy()
                res = res.sort_values('price', ascending=False)
            
            elif consulta == "Top 10 propiedades más caras":
                res = self.df.nlargest(10, 'price').sort_values('price', ascending=False)
            
            else:
                res = pd.DataFrame({'Mensaje': ['Seleccione una consulta válida']})
            
            self.mostrar_resultado(res)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar la consulta:\n{str(e)}")
            #mostrar el error en la interfaz
            error_frame = tk.Frame(self.result_frame)
            error_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(
                error_frame,
                text=f"Error al ejecutar la consulta:\n{str(e)}",
                fg='red',
                font=('Arial', 10)
            ).pack(pady=20)
    
    def mostrar_resultado(self, resultado):
        """Muestra los resultados en la tabla"""
        frame = tk.Frame(self.result_frame)
        frame.pack(fill=tk.BOTH, expand=True)
        
        if isinstance(resultado, pd.DataFrame):
            # configurara pandastable
            pt = Table(
                frame,
                dataframe=resultado,
                showtoolbar=True,
                showstatusbar=True,
                width=1050,
                height=600,
                cellbackgr='#ffffff',
                grid_color='#e0e0e0',
                textcolor='#000000'
            )
            pt.show()
            
            # ajuste del ancho de columnas automaticamente
            pt.autoResizeColumns()
        else:
            tk.Label(
                frame,
                text=str(resultado),
                font=('Arial', 12),
                wraplength=1000
            ).pack(pady=20)
    
    def clear_window(self):
        """Limpia todos los widgets de la ventana"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    try:
        app = Aplicacion()
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"La aplicación falló:\n{str(e)}")