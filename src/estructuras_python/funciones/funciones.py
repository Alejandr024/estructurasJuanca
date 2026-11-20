# Sumnar
'''
def sumar(p1,p2):
    return (p1+p2)

print(sumar(3,4))
'''

#funcion con tuplas
"""Calcula suma, promedio y maximo de una lista"""
'''
def calcular_estadisticas (numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    maximo = max (numeros)
    return total, promedio, maximo # Devuelve una tupla

# Desempaquetado de valores
suma, prom, max_val = calcular_estadisticas([10, 20, 30, 40, 50])
print(f"Suma: {suma}, Promedio: {prom}, Maximo: {max_val}")
'''
# Salida: Suma: 150, Promedio: 30.0, Máximo: 50

#funciones anidadas
'''
def calcular_precio_con_descuento(precio, porcentaje_descuento):
    """Calcula precio final con descuento e IVA"""
    
    def aplicar_descuento(p, descuento):
        """Función auxiliar interna"""
        return p * (1 - descuento / 100)
    
    def aplicar_iva(p):
        """Funcion auxiliar interna"""
        return p * 1.21

    precio_con_descuento = aplicar_descuento(precio, porcentaje_descuento)
    precio_final = aplicar_iva(precio_con_descuento)
    return precio_final

print(calcular_precio_con_descuento(100, 10)) # 108.9
'''
#decoradores
'''
def anunciar_ejecucion(func):
# Envoltura que añade comportamiento antes y después

    def envoltura():
        print(" --- Iniciando funcion --- ")
        func()
        print(" --- Funcion terminada --- ")
    return envoltura
# Aplicamos el decorador usando @
@anunciar_ejecucion
def tarea_importante():
    print("Procesando datos en la base de datos ... ")
# Prueba
tarea_importante()
'''

# map lambda
'''
numeros=[1,2,3,4,5]
cuadrados= list(map(lambda x: x**2, numeros))

print("Cuadrados: ", cuadrados)
'''

#kwargs
'''
def crear_perfil_user(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

crear_perfil_user(nombre="Luis",edad=35, ciudad="Madrid", pais="España")
'''

#alternativa
''''
def crear_perfil_user(nombre, apellido, **kwargs):
    perfil= {"nombre": nombre, "apellido": apellido}
    perfil.update(**kwargs)
    return perfil

user= crear_perfil_user("Luis", "Vega", ciudad="Madrid", pais="España")

print(user)
'''