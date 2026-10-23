from Producto import Producto

producto1= Producto("Camiseta", 25.99)
producto2= Producto("Pantalón", 39.99)

print(producto1.calidad)

producto1.categoria= "Ropa"
print(producto1.categoria)
# Demostración del límite de alcance dinámico:
try:
    print(producto2.categoria)
except AttributeError as e:
    print(f"Error esperado: {e}")
# Salida: Error esperado: 'Producto' object has no attribute 'categoria
