import pandas as pd
import os
import re
from pathlib import Path

# Ruta de la carpeta con archivos originales
input_folder_path = r'dataset_inspecciones_programadas'
# Ruta de la carpeta donde se guardarán los archivos limpios
output_folder_path = r'c_dataset_inspecciones_programadas_limpio'

# Crear la carpeta de salida si no existe
Path(output_folder_path).mkdir(parents=True, exist_ok=True)

# Función para limpiar un archivo CSV
def clean_csv(file_path, output_folder_path):
    # Cargar el archivo con la suposición de que la tercera fila contiene los encabezados correctos
    df = pd.read_csv(file_path, header=3, dtype=str)
    # Eliminar filas completamente vacías
    df_cleaned = df.dropna(how='all')
    # Eliminar columnas completamente vacías
    df_cleaned = df_cleaned.dropna(axis=1, how='all')
    # Guardar el archivo limpio
    output_file_path = os.path.join(output_folder_path, os.path.basename(file_path))
    df_cleaned.to_csv(output_file_path, index=False)

# Expresión regular para verificar si el nombre del archivo comienza con 4 dígitos
pattern = re.compile(r'^\d{3,}')

# Recorrer todos los archivos CSV en la carpeta de entrada
for file_name in os.listdir(input_folder_path):
    # Verificar si el archivo cumple con el patrón de nombre y es un archivo CSV
    if pattern.match(file_name) and file_name.endswith('.csv'):
        file_path = os.path.join(input_folder_path, file_name)
        clean_csv(file_path, output_folder_path)
        print(f"Archivo procesado: {file_name}")
    else:
        print(f"Archivo omitido: {file_name}")

print("Todos los archivos válidos han sido procesados y guardados en la carpeta de salida.")
