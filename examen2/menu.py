import os
import subprocess

def unir_archivos(archivos):
    contenido_total = ""
    for archivo in archivos:
        with open(archivo, 'r') as f:
            contenido_total += f.read() + "\n"
    return contenido_total

def mostrar_menu(archivos):
    print("Seleccione el archivo que desea abrir:")
    for i, archivo in enumerate(archivos, 1):
        print(f"{i}. {archivo}")
    print("0. Salir")

def ejecutar_archivo(archivo):
    try:
        subprocess.run(["python", archivo], check=True)
    except subprocess.CalledProcessError:
        print("Error al ejecutar el archivo.")

def main():
    print("¡Bienvenido al programa de ejecución de archivos!")
    archivos = ["Mezclas.py", "examen6.py", "hoteles.py", "orquestas.py", "Examen.py"]
    while True:
        mostrar_menu(archivos)
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa.")
                break
            elif opcion >= 1 and opcion <= len(archivos):
                archivo_seleccionado = archivos[opcion - 1]
                print(f"Ejecutando archivo {archivo_seleccionado}...")
                ejecutar_archivo(archivo_seleccionado)
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

