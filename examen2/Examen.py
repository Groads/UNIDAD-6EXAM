class Alumno:
    def __init__(self, nombre, promedio, num_materias_aprobadas):
        self.nombre = nombre
        self.promedio = promedio
        self.num_materias_aprobadas = num_materias_aprobadas

    def __str__(self):
        return f"Nombre: {self.nombre}, Promedio: {self.promedio}, Materias Aprobadas: {self.num_materias_aprobadas}"


class RegistroAlumnos:
    def __init__(self, alumnos):
        self.alumnos = alumnos

    def quicksort(self, lista, paso_a_paso=False):
        if len(lista) <= 1:
            return lista
        pivot = lista[len(lista) // 2]
        izquierda = [x for x in lista if x.nombre < pivot.nombre]
        centro = [x for x in lista if x.nombre == pivot.nombre]
        derecha = [x for x in lista if x.nombre > pivot.nombre]

        if paso_a_paso:
            print(f"Izquierda: {[alumno.nombre for alumno in izquierda]}")
            print(f"Centro: {[alumno.nombre for alumno in centro]}")
            print(f"Derecha: {[alumno.nombre for alumno in derecha]}")
            print()

        return self.quicksort(izquierda, paso_a_paso) + centro + self.quicksort(derecha, paso_a_paso)

    def imprimir_alumnos(self, ordenado=False):
        if ordenado:
            alumnos_a_imprimir = self.quicksort(self.alumnos.copy(), paso_a_paso=True)
        else:
            alumnos_a_imprimir = self.alumnos
        for alumno in alumnos_a_imprimir:
            print(alumno)

    def obtener_alumno_por_posicion(self, posicion, ordenado=False):
        if ordenado:
            lista = self.quicksort(self.alumnos)
        else:
            lista = self.alumnos
        if 0 <= posicion < len(lista):
            return lista[posicion]
        else:
            return None

    def buscar_alumno_por_nombre(self, nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None


def ingresar_alumnos():
    alumnos = []
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        if not nombre.isalpha():
            print("Error: El nombre solo debe contener caracteres alfabéticos.")
            continue
        while True:
            try:
                promedio = float(input(f"Ingrese el promedio de {nombre} (1-100): "))
                if promedio < 1 or promedio > 100:
                    raise ValueError("El promedio debe estar entre 1 y 100.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        num_materias_aprobadas = int(input(f"Ingrese el número de materias aprobadas de {nombre}: "))
        alumnos.append(Alumno(nombre, promedio, num_materias_aprobadas))
    return alumnos


def main():
    alumnos = ingresar_alumnos()
    registro = RegistroAlumnos(alumnos)

    print("\nLista de alumnos en orden desordenado (como se ingresaron):")
    registro.imprimir_alumnos(ordenado=False)

    ordenar_paso_a_paso = input("\n¿Desea ver el paso a paso del ordenamiento de la lista de alumnos? (s/n): ")
    if ordenar_paso_a_paso.lower() == 's':
        print("\nLista de alumnos en orden alfabético (paso a paso):")
        registro.imprimir_alumnos(ordenado=True)
    else:
        print("\nLista de alumnos en orden alfabético:")
        registro.imprimir_alumnos(ordenado=True)

    while True:
        nombre_buscar = input("\nIngrese el nombre del alumno a buscar: ")
        alumno = registro.buscar_alumno_por_nombre(nombre_buscar)
        if alumno:
            print(f"Alumno encontrado: {alumno}")
            break
        else:
            print(f"Alumno {nombre_buscar} no encontrado.")

    while True:
        posicion = int(input("\nIngrese la posición del alumno en la lista desordenada: "))
        alumno = registro.obtener_alumno_por_posicion(posicion, ordenado=False)
        if alumno:
            print(f"Alumno en la posición {posicion} (desordenado): {alumno}")
            break
        else:
            print(f"No hay alumno en la posición {posicion} en la lista desordenada.")

    while True:
        posicion = int(input("\nIngrese la posición del alumno en la lista ordenada: "))
        alumno = registro.obtener_alumno_por_posicion(posicion, ordenado=True)
        if alumno:
            print(f"Alumno en la posición {posicion} (ordenado): {alumno}")
            break
        else:
            print(f"No hay alumno en la posición {posicion} en la lista ordenada.")


if __name__ == "__main__":
    main()
