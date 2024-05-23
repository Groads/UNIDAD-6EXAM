class alumnostec:
    def __init__(self, nombre, matricula, num_materias_apro, promedio):
        self.nombre = nombre
        self.matricula = matricula
        self.num_materias_aprobadas = num_materias_apro
        self.promedio = promedio

    def __str__(self):
        return f'Nombre: {self.nombre}, Matricula: {self.matricula}, Materias Aprobadas: {self.num_materias_aprobadas}, Promedio: {self.promedio}'

def metodo_de_seleccion_directa(alumnos):
    for i in range(len(alumnos)):
        min_idx = i
        for j in range(i+1, len(alumnos)):
            if alumnos[min_idx].nombre > alumnos[j].nombre:
                min_idx = j
        alumnos[i], alumnos[min_idx] = alumnos[min_idx], alumnos[i]

def metodo_quicksort_particion(alumnos, bajo, alto):
    i = (bajo-1)
    pivot = alumnos[alto].num_materias_aprobadas

    for j in range(bajo, alto):
        if alumnos[j].num_materias_aprobadas <= pivot:
            i = i+1
            alumnos[i], alumnos[j] = alumnos[j], alumnos[i]

    alumnos[i+1], alumnos[alto] = alumnos[alto], alumnos[i+1]
    return (i+1)

def quicksort_ordenamiento(alumnos, bajo, alto):
    if len(alumnos) == 1:
        return alumnos
    if bajo < alto:
        pi = metodo_quicksort_particion(alumnos, bajo, alto)
        quicksort_ordenamiento(alumnos, bajo, pi-1)
        quicksort_ordenamiento(alumnos, pi+1, alto)

def imprimir_alumnos(alumnos):
    for alumno in alumnos:
        print(alumno)

alumnos = [
    alumnostec('Marco', '6578', 7, 75),
    alumnostec('Jesus', '4846', 7, 80),
    alumnostec('Isaac', '7642', 7, 85),
    alumnostec('Armando', '2881', 7, 90),
    alumnostec('Fernando', '8247', 7, 95),
    alumnostec('Maria', '1224', 5, 67),
    alumnostec('Nicol', '5878', 4, 52),
    alumnostec('Sharon', '9775', 5, 58),
    alumnostec('Juan', '6684', 6, 75),
    alumnostec('Carlos', '3548', 6, 76),
    alumnostec('Angel', '5257', 7, 97),
    alumnostec('Samuel', '9245', 7, 92.5),
    alumnostec('Diego', '4215', 7, 97.5),
    alumnostec('Elias', '6078', 6, 88),
    alumnostec('Harvin', '1875', 5, 82.7),
    alumnostec('Lizzette', '6835', 7, 72.4),
    alumnostec('Manuel', '8754', 7, 100),
    alumnostec('Adriana', '7775', 4, 50),
    alumnostec('Alo', '7954', 5, 66),
    alumnostec('Angie', '5785', 4, 69.5)
]

metodo_de_seleccion_directa(alumnos)
print("Alumnos ordenados por nombre:")
imprimir_alumnos(alumnos)

alumnos_por_materias = alumnos.copy()
quicksort_ordenamiento(alumnos_por_materias, 0, len(alumnos_por_materias)-1)
print("\nAlumnos ordenados por número de materias aprobadas:")
imprimir_alumnos(alumnos_por_materias)
