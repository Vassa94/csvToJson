import pandas as pd
import json
import tkinter as tk

from tkinter import Label, filedialog
import codecs
import os

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

# Botón para cargar el archivo CSV
cargar_boton = tk.Button(root, text='Cargar archivo CSV', command=cargar_archivo)
cargar_boton.pack()

# Cuadro de texto para mostrar el resultado JSON
resultado = tk.Text(root, height=20, width=50)
resultado.config(state=tk.DISABLED, padx=10, pady=10)  # Agregar relleno al cuadro de texto
resultado.pack(fill=tk.BOTH, expand=True)  # Hacer que el cuadro de texto se ajuste al tamaño de la pantalla



# establecer el título de la ventana
root.title("CSV to JSON Converter")

# establecer el ícono de la ventana
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'icon.ico'))

firma = Label(root, text="© Ignacio Vassallo, 2023")
firma.pack(side="bottom")
firma.config(font=("Arial", 10))


# Iniciar el loop principal de la GUI
root.mainloop()
