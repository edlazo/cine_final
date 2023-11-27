import json

# Cargar o inicializar las salas desde un archivo JSON
try:
    with open("salas_cine.json", "r") as file:
        peliculas = json.load(file)
except FileNotFoundError:
    # Películas en cartelera con sus salas y asientos disponibles
    peliculas = {
        "El Padrino": {
            "sala": "Sala 1",
            "asientos": [0] * 30
        },
        "Titanic": {
            "sala": "Sala 2",
            "asientos": [0] * 30
        },
        "El Señor de los Anillos": {
            "sala": "Sala 3",
            "asientos": [0] * 30
        },
        "Harry Potter": {
            "sala": "Sala 4",
            "asientos": [0] * 30
        },
        "Star Wars": {
            "sala": "Sala 5",
            "asientos": [0] * 30
        }
    }

# Función para mostrar los asientos en forma de matriz usando símbolos ASCII
def mostrar_asientos(asientos):
    print("Estado de los asientos:")
    print("-----------------------")
    for i in range(0, len(asientos), 5):
        print(*asientos[i:i + 5], sep='  ')
    print("-----------------------")

# Función para reservar un asiento
def reservar_asiento(pelicula):
    sala = peliculas[pelicula]["sala"]
    asientos = peliculas[pelicula]["asientos"]

    while True:
        mostrar_asientos(asientos)
        num_asiento = int(input(f"Elige un asiento en la {sala} para '{pelicula}' (1-30): "))
        if 1 <= num_asiento <= 30:
            if asientos[num_asiento - 1] == 0:
                confirmacion = input(f"El asiento {num_asiento} está disponible. ¿Deseas reservarlo? (Sí/No): ").lower()
                if confirmacion == 'sí' or confirmacion == 'si':
                    asientos[num_asiento - 1] = 1
                    print(f"¡Has reservado el asiento {num_asiento} para '{pelicula}' en la {sala}!")
                    seguir_reservando = input("¿Quieres reservar otro asiento? (Sí/No): ").lower()
                    if seguir_reservando != 'sí' and seguir_reservando != 'si':
                        # Guardar cambios en el archivo JSON
                        with open("salas_cine.json", "w") as file:
                            json.dump(peliculas, file)
                        break
                else:
                    print("No se ha realizado ninguna reserva.")
                    opcional = input("¿Quieres seleccionar otro asiento? (Sí/No): ").lower()
                    if opcional != 'sí' and opcional != 'si':
                        break
            else:
                print(f"El asiento {num_asiento} en la {sala} ya está ocupado.")
                opcional = input("¿Quieres seleccionar otro asiento? (Sí/No): ").lower()
                if opcional != 'sí' and opcional != 'si':
                    break
        else:
            print("Número de asiento inválido.")
            opcional = input("¿Quieres seleccionar otro asiento? (Sí/No): ").lower()
            if opcional != 'sí' and opcional != 'si':
                break

# Uso del programa
while True:
    print("\nPelículas en cartelera:")
    for idx, pelicula in enumerate(peliculas, start=1):
        print(f"{idx}. {pelicula}")

    opcion = int(input("\nElige una película (1-5) o ingresa 0 para salir: "))
    if opcion == 0:
        print("¡Hasta luego!")
        break
    elif 1 <= opcion <= 5:
        pelicula_seleccionada = list(peliculas.keys())[opcion - 1]
        reservar_asiento(pelicula_seleccionada)
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
