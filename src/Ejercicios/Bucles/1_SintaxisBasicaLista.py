'''
Enunciado: Dada una lista de precios de un carrito de la compra [15.50, 20.0, 35.75, 10.0],
calcula el total iterando sobre la lista (sin usar la función sum()).

'''
precios = [15.50, 20.0, 35.75, 10.0]

total = 0

for precio in precios:
    total += precio

print(f"El total de la compra es: {total:.2f}€")
