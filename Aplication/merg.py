import os
import pandas as pd
import re
from pathlib import Path

def eliminar_filas_con_patrones(df):
    # Patrones a buscar en cada fila
    patron_vlookup = re.compile(r'=VLOOK')
    patron_corchete = re.compile(r'=\[')

    # Lista para almacenar índices de filas a eliminar
    filas_a_eliminar = []

    # Iterar sobre cada fila del DataFrame
    for indice, fila in df.iterrows():
        try:
            # Convertir cada valor de la fila a cadena y luego unirlos
            fila_str = ''.join(fila.astype(str))
            # Verificar si la fila contiene alguno de los patrones
            if patron_vlookup.search(fila_str) or patron_corchete.search(fila_str):
                filas_a_eliminar.append(indice)
        except Exception as e:
            print(f"Error al procesar la fila {indice}: {e}")

    # Eliminar las filas identificadas de la lista
    df_filtrado = df.drop(filas_a_eliminar)

    # Restablecer los índices después de eliminar las filas
    df_filtrado.reset_index(drop=True, inplace=True)
    #df_filtrado = df_filtrado(headers=1)
    return df_filtrado


def merg(carpeta, name="default"):
    def obtener_nombre_csv(ruta):
        nombre_archivo = ruta.split('/')[-1]  # Obtener el nombre del archivo a partir de la ruta
        return nombre_archivo + ".csv"

    df_combinado = pd.DataFrame()
    # Iterar sobre todos los archivos en la carpeta
    for filename in os.listdir(carpeta):
        if filename.endswith('.csv'):
            archivo_path = os.path.join(carpeta, filename)
            try:
                # Leer el archivo CSV y especificar los encabezados
                df = pd.read_csv(archivo_path, na_values=['NaN', 'NA'], dtype=str)

                # Concatenar el DataFrame actual al DataFrame combinad
                df_combinado = pd.concat([df_combinado, df], ignore_index=True)
            except:
                pass
    try:
        name = obtener_nombre_csv(carpeta)
        # Guardar el DataFrame combinado en un archivo CSV
        umbral_nulos = len(df.columns) * 0.8  # Define el umbral como el 90% de las columnas
        df_limpiado = df_combinado.dropna(thresh=umbral_nulos)
        df_limpiado = eliminar_filas_con_patrones(df_limpiado)
        if inspecciones in name:
            df_limpiado = df_limpiado.iloc[:, :16]
        else: 
            df_limpiado = df_limpiado.iloc[:,:15]
        df_limpiado.to_csv(f'Dataset/{name}', index=False)

    except:
        pass

Path(r"Dataset").mkdir(parents=True, exist_ok=True) # Create the dataset directory

directorio_No_programados_inspecciones = r"c_dataset_inspecciones_no_programadas_limpio"
directorio_No_programados_actividades = r"c_dataset_actividades_no_programadas_limpio"
directorio_programados_inspecciones = r"c_dataset_inspecciones_programadas_limpio"
directorio_programados_actividades = r"c_dataset_actividades_programadas_limpio"

directorios = [
    directorio_No_programados_inspecciones,
    directorio_No_programados_actividades,
    directorio_programados_inspecciones,
    directorio_programados_actividades
]

for directorio in directorios:
            merg(directorio)
            
