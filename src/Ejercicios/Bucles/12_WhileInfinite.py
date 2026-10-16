total = 0

while True:
    numero = input("Introduce un número o escribe 'salir' para terminar: ")

    if numero.lower() == "salir":
        break

    total += float(numero)

print("El total de la suma es:", total)