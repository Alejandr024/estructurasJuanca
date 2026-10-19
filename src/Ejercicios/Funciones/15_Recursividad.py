#calcular el factorial de un numero


def factorial(n):
    #Case base
    if n <=1:
        return 1
    #recursividad
    return n*factorial(n-1)

print("Factorial de 5 = ", factorial(5))