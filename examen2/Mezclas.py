import csv
import os
import heapq

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)
    return merge(left_half, right_half, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def mezcla_equilibrada(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = mezcla_equilibrada(arr[:mid], key)
        right_half = mezcla_equilibrada(arr[mid:], key)
        return merge(left_half, right_half, key)


empleados = []
with open('EMPLEADOS.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
  
    encabezados = reader.fieldnames
    print("Encabezados:", encabezados)
    for row in reader:
       
        if '\ufeffNombre' in row:
            row['Nombre'] = row.pop('\ufeffNombre')
        empleados.append(row)


print("Datos leídos (primeros 5 registros):", empleados[:5])


empleados_ordenados_directa = merge_sort(empleados, "Nombre")


with open('EMPLEADOS_ORDENADOS_DIRECTA.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = empleados[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for emp in empleados_ordenados_directa:
        writer.writerow(emp)


empleados_ordenados_equilibrada = mezcla_equilibrada(empleados, "Nombre")


with open('EMPLEADOS_ORDENADOS_EQUILIBRADA.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = empleados[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for emp in empleados_ordenados_equilibrada:
        writer.writerow(emp)
