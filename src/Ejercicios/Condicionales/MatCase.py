controladorApi= int(input("Introduce el código de estado HTTP: "))

match controladorApi:
    case 200 | 201:
        if controladorApi==200:
            print(f"Respuesta {controladorApi}: OK")
        elif controladorApi==201:
            print(f"Respuesta {controladorApi}: Created")
    case controladorApi if 400<=controladorApi<=404:
        if controladorApi==400:
            print(f"Error {controladorApi}: Bad request")
        elif controladorApi==401:
            print(f"Error {controladorApi}: Unauthorized")
        elif controladorApi==403:
            print(f"Error {controladorApi}: Forbidden")
        elif controladorApi==404:
            print(f"Error {controladorApi}: Not Found")
    case 500 | 503:
        print("Error en el servidor.")
    case _:
        print("Código de estado no reconocido.")