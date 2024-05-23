hoteles_del_Profe_Armando = [
    {"nombre": "Hotel Montejo", "ciudad": "Merida", "estrellas": 3, "cuartos": 35},
    {"nombre": "Hotel Ibis Merida", "ciudad": "Merida", "estrellas": 3, "cuartos": 60},
    {"nombre": "Hotel Fiesta Americana", "ciudad": "Merida", "estrellas": 5, "cuartos": 75},
    {"nombre": "Hotel Emporio Cancun", "ciudad": "Quintana Roo", "estrellas": 4, "cuartos": 120},
    {"nombre": "Hotel Paradisus Cancun", "ciudad": "Quintana Roo", "estrellas": 4, "cuartos": 80},
    {"nombre": "Hotel Holbox", "ciudad": "Quintana Roo", "estrellas": 4, "cuartos": 75},
    {"nombre": "Hotel Marriott", "ciudad": "Tuxtla Gutiérrez", "estrellas": 4, "cuartos": 80},
    {"nombre": "Hotel Xilita", "ciudad": "San Luis Potosi", "estrellas": 4, "cuartos": 75},
    {"nombre": "Hotel Mio", "ciudad": "Jalisco", "estrellas": 4, "cuartos": 120},
    {"nombre": "The Explorean Kohunlich", "ciudad": "Campeche", "estrellas": 4, "cuartos": 80}
]

def burbuja(hoteles, ciudad, nombre):
    n = len(hoteles)
    for i in range(n):
        for j in range(0, n-i-1):
            if hoteles[j][ciudad] > hoteles[j+1][ciudad]:
                hoteles[j], hoteles[j+1] = hoteles[j+1], hoteles[j]

            elif hoteles[j][ciudad] == hoteles[j+1][ciudad] and hoteles[j][nombre] > hoteles[j+1][nombre]:
                hoteles[j], hoteles[j+1] = hoteles[j+1], hoteles[j]

burbuja(hoteles_del_Profe_Armando, "ciudad", "nombre")

print("Estos son los hoteles de Ingeniero Armando Valadez ordenados por ciudad y luego por nombre:\n")
for hotel in hoteles_del_Profe_Armando:
    print(f"Nombre: {hotel['nombre']}, Ciudad: {hotel['ciudad']}, Estrellas: {hotel['estrellas']}, Cuartos: {hotel['cuartos']}")
