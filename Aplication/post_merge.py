#fix the actividades programadas file
with open(r"Dataset\c_dataset_actividades_programadas_limpio.csv", "r+", encoding="UTF-8") as file:
    lines = file.readlines()
    lines[0] = "Código centro,Centro,Ubicac. técnica,Denominación Ubic.,Equipo,Denominación,No. Plan,Desc. Plan,Orden,Actividad,Clase de orden,Status sistema,Inicio program.,Responsable,Prioridad,Duración\n"
    file.seek(0)
    file.writelines(lines)
    file.truncate()