import os
import pandas as pd
import re
from pathlib import Path
def eliminar_filas_con_patrones(df):
    # Patterns to clean
    patron_vlookup = re.compile(r'=VLOOK')
    patron_corchete = re.compile(r'=\[')

    # The list where will set the index of the row to delete
    filas_a_eliminar = []

    # iter each file on the directory
    for indice, fila in df.iterrows():
        try:
            # Transform each value on the row and do the join for analice the pattern
            fila_str = ''.join(fila.astype(str))
            # Verificar si la fila contiene alguno de los patrones
            if patron_vlookup.search(fila_str) or patron_corchete.search(fila_str):
                filas_a_eliminar.append(indice)
        except Exception as e:
            print(f"Error al procesar la fila {indice}: {e}")

    # drop the files that have the pattern
    df_filtrado = df.drop(filas_a_eliminar)

    # reset the index before save the data
    df_filtrado.reset_index(drop=True, inplace=True)
    return df_filtrado


def merg(carpeta, name="default"):
    def obtener_nombre_csv(ruta):
        nombre_archivo = ruta.split('/')[-1]  # get the name of the file from his directory
        return nombre_archivo + ".csv"

    df_combinado = pd.DataFrame()#create the dataframe where we will set the same data

    # iter all file from the directory
    for filename in os.listdir(carpeta):
        if filename.endswith('.csv'):
            archivo_path = os.path.join(carpeta, filename)
            try:
                # read the csv 
                df = pd.read_csv(archivo_path, na_values=['NaN', 'NA'], dtype=str)

                # Concat (merg) the dataframe
                df_combinado = pd.concat([df_combinado, df], ignore_index=True)
            except:
                pass
    try:
        name = obtener_nombre_csv(carpeta)
        # Save the concat dataframe and define his name
        umbral_nulos = len(df.columns) * 0.8  # Define the thresh at 80% per row
        df_limpiado = df_combinado.dropna(thresh=umbral_nulos)#dropnulls
        df_limpiado = eliminar_filas_con_patrones(df_limpiado)#drop the rows with pattern
        df_limpiado = df_limpiado.iloc[:, :17]#avoid to set the combined headers
        df_limpiado.to_csv(f'Dataset/{name}', index=False)#save the  csv

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
            
