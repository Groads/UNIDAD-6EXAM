import csv
from datetime import datetime
import pandas as pd

# Datos para cada archivo
data_a1 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Juan', 123, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['María', 456, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['Pedro', 789, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
]

data_a2 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Laura', 321, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['Carlos', 654, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['Sofía', 987, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
]

data_a3 = [
    ['Nombre', 'Número', 'Fecha'],
    ['Ana', 111, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['Diego', 222, datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    ['Elena', 333, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
]

# Función para crear archivo CSV
def crear_csv(nombre_archivo, datos):
    with open(nombre_archivo + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datos)

# Crear archivos CSV
crear_csv('A1', data_a1)
crear_csv('A2', data_a2)
crear_csv('A3', data_a3)

# Leer los archivos CSV
a1 = pd.read_csv("A1.csv")
a2 = pd.read_csv("A2.csv")
a3 = pd.read_csv("A3.csv")

# Concatenar los DataFrames
recitales = pd.concat([a1, a2, a3])

# Ordenar por el primer campo (Nombre)
recitales.sort_values(by='Nombre', inplace=True)

# Guardar el DataFrame resultante en un nuevo archivo CSV
recitales.to_csv("RECITALES.csv", index=False)

print("Archivo RECITALES.csv creado exitosamente.")