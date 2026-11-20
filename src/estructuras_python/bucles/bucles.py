import random
'''
lista =["manzana", "pera", "platano", "limon", "fresa"]

for fruta in lista:
    print(fruta)
'''

'''
for letra in "Pepito":
    print(letra)
'''
'''
prices = [100, 250, 75, 500, 150]
discounted_prices = []
discount_rate = 0.20

for price in prices:
    discounted = price * (1 - discount_rate)
    discounted_prices.append(discounted)
    print (f"Precio original: $ {price} + Con descuento: $ {discounted} ")

print(f"Precios con descuento: {discounted_prices}")
'''
#Cuenta regresiva
'''
for number in range(10,0,-1):
    print(f"Número: {number}")
'''
'''
number = 7
print(f"Tabla del {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
'''
#For con enumerate
'''
tasks = ["Comprar leche", "Llamar al medico", "Hacer ejercicio"]
for index, task in enumerate(tasks, start=1) :
    print (f"{index}. {task}")
'''
#For anidado
'''
for i in range(1,6):
    print(f"Tabla del {i}:")
    for j in range(1,4):
        result=i*j
        print(f"{i} x {j}= {result}")
'''

#List comprehension
#Forma tradicional
'''
squares = []

for number in range(1, 6):
    squares.append (number ** 2)
print(squares)
'''

#Forma ListComprehension
'''
squares = [number ** 2 for number in range (1, 6) ]
print(squares)
'''

#Triangulo
'''
for i in range (1,6):
    for j in range (i):
        number= random.randint(0,9)
        if number%2 ==0:
            number="p"
        print(f"{number} \t", end="")
    print("\n")
'''
# while
'''
counter =1
while counter<=5:
    print(counter)
    counter+=1
'''