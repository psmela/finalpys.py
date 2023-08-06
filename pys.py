# Lista de películas y series
peliculas_y_series = [
    {
        "titulo": "Donde estan las rubias",
        "productora": "bw",
        "generos": ["Comwdia", "Acción"],
        "tipo": "Película",
        "fecha_estreno": "31/03/2008",
        "valoracion": 8.9,
    },
    {
        "titulo": "Stranger Things",
        "productora": "Netflix",
        "generos": ["Drama", "Fantasía", "Suspenso"],
        "tipo": "Serie",
        "fecha_estreno": "15/07/2016",
        "valoracion": 8.7,
    },
    {
        "titulo":"Rosario tijeras",
        "productora":"telemundo",
        "generos":"asesinatos,venganza",
        "tipo":"serie",
        "fecha_estreno":"21/09/1991",
        "valoracion":9.9,

    },

    {
        "titulo":"Señora acero",
        "productora":"nace",
        "generos":"romance,drama",
        "tipo":"serie",
        "fecha_estreno":"09/09/2018",
        "valoracion":9.8
    },

    {
        "titulo":"la gloria",
        "productora":"coreana",
        "generos":"drama.amor",
        "tipo":"serie",
        "fecha_estreno":"12/07/2020",
        "valoracion":10.0
    },
]

def listar_pys(pys_list):
    for pys in pys_list:
        print(f"Título: {pys['titulo']}, Productora: {pys['productora']}, Géneros: {', '.join(pys['generos'])}, Tipo: {pys['tipo']}, Fecha de estreno: {pys['fecha_estreno']}, Valoración de usuarios: {pys['valoracion']}")

def agregar_pelicula_o_serie(pys_list):
    nueva_pys = {}
    nueva_pys["titulo"] = input("Ingrese el título: ")
    nueva_pys["productora"] = input("Ingrese el nombre de la productora cinematográfica: ")
    nueva_pys["generos"] = input("Ingrese los géneros separados por comas: ").split(',')
    nueva_pys["tipo"] = input("Ingrese el tipo (Película o Serie): ")
    nueva_pys["fecha_estreno"] = input("Ingrese la fecha de estreno: ")
    nueva_pys["valoracion"] = float(input("Ingrese la valoración de usuarios: "))
    
    pys_list.append(nueva_pys)
    print(f"Se ha agregado '{nueva_pys['titulo']}' a la lista de PyS.")

def buscar_pys_por_titulo(pys_list, titulo_buscar):
    for pys in pys_list:
        if pys['titulo'].lower() == titulo_buscar.lower():
            return pys
    return None

def modificar_pys(pys_list):
    titulo_buscar = input("Ingrese el título de la película o serie a buscar: ")
    pys_encontrada = buscar_pys_por_titulo(pys_list, titulo_buscar)
    
    if pys_encontrada:
        print("Se encontró la PyS:")
        print(f"Título: {pys_encontrada['titulo']}, Productora: {pys_encontrada['productora']}, Géneros: {', '.join(pys_encontrada['generos'])}, Tipo: {pys_encontrada['tipo']}, Fecha de estreno: {pys_encontrada['fecha_estreno']}, Valoración de usuarios: {pys_encontrada['valoracion']}")
       

        pys_encontrada.update({
            "titulo": input("Nuevo título: "),
            "productora": input("Nueva productora: "),
            "generos": input("Nuevos géneros separados por comas: ").split(','),
            "tipo": input("Nuevo tipo (Película o Serie): "),
            "fecha_estreno": input("Nueva fecha de estreno: "),
            "valoracion": float(input("Nueva valoración de usuarios: ")),
        })
        print("Datos modificados con éxito.")
    else:
        print("No se encontró la película o serie.")



# Menú principal
while True:
    print("\n--- Administrador de Películas y Series ---")
    print("1. Listar todas las películas y series")
    print("2. Agregar nueva película o serie")
    print("3. Buscar película o serie por título")
    print("4. Modificar película o serie")
    
    print("10. Salir")
    opcion = int(input("Ingrese el número de la opción que desee: "))

    if opcion == 1:
        listar_pys(peliculas_y_series)
    elif opcion == 2:
        agregar_pelicula_o_serie(peliculas_y_series)
    elif opcion == 3:
        titulo_buscar = input("Ingrese el título de la película o serie a buscar: ")
        pys_encontrada = buscar_pys_por_titulo(peliculas_y_series, titulo_buscar)
        if pys_encontrada:
            print("Detalles de la PyS:")
            print(f"Título: {pys_encontrada['titulo']}")
            print(f"Productora: {pys_encontrada['productora']}")
            print(f"Género(s): {', '.join(pys_encontrada['generos'])}")
            print(f"Tipo: {pys_encontrada['tipo']}")
            print(f"Fecha de estreno: {pys_encontrada['fecha_estreno']}")
            print(f"Valoración de usuarios: {pys_encontrada['valoracion']}")
        else:
            print("No se encontró la película o serie.")
    elif opcion == 4:
        modificar_pys(peliculas_y_series)
   
    elif opcion == 10:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")