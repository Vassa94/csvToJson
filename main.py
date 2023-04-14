import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog
import codecs

# Función para cargar el archivo CSV
def cargar_archivo():
    # Abrir el cuadro de diálogo de selección de archivo
    ruta_archivo = filedialog.askopenfilename()

    # Cargar el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(ruta_archivo)

    # Convertir el DataFrame en un objeto JSON con formato limpio
    objeto_json = json.dumps(json.loads(df.to_json(orient='records', force_ascii=False)), indent=4)
    objeto_json = codecs.encode(objeto_json, 'utf-8').decode('unicode_escape')

    # Mostrar el objeto JSON en la GUI
    resultado.config(state=tk.NORMAL)
    resultado.delete('1.0', tk.END)
    resultado.insert(tk.END, objeto_json)
    resultado.config(state=tk.DISABLED)

# Crear la interfaz gráfica de usuario
root = tk.Tk()
root.title('Convertir CSV a JSON')

# Botón para cargar el archivo CSV
cargar_boton = tk.Button(root, text='Cargar archivo CSV', command=cargar_archivo)
cargar_boton.pack()

# Cuadro de texto para mostrar el resultado JSON
resultado = tk.Text(root, height=20, width=50)
resultado.config(state=tk.DISABLED, padx=10, pady=10)  # Agregar relleno al cuadro de texto
resultado.pack(fill=tk.BOTH, expand=True)  # Hacer que el cuadro de texto se ajuste al tamaño de la pantalla

# Iniciar el loop principal de la GUI
root.mainloop()
