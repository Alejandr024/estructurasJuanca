'''
Enunciado: Pide una palabra al usuario y cuenta cuántas vocales (a, e, i, o, u) contiene iterando
letra por letra.
'''
palabra = input("Introduce una palabra: ")

vocales = "aeiou"
contador = 0

for letra in palabra.lower():
    if letra in vocales:
        contador += 1
        print(f"La letra '{letra}' es una vocal.")

print(f"La palabra '{palabra}' contiene {contador} vocales.")
