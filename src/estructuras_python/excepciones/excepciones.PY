#Try, except, finally

while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        numero2 = int(input("Ingrese otro número entero positivo: "))
        resultado = numero + numero2
        print("El resultado de la suma es:", resultado)
        break
    except ValueError:
        print("Error: Por favor, ingrese solo numeros enteros positivos.")
    finally:
        print("Proceso completado.")