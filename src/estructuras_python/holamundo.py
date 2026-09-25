# print("Hola mundo")

#a=3
#print(type(a))
#a="Pepe"
#print(type(a))

lista1= [1,2,3]

lista2= [1,2,3]

lista3= lista1

print(lista1 == lista2)

print(lista1 is lista2)

print(lista1 is lista3)

lista1[1]=4
lista3[2]=6

print("Lista 1: ", lista1)
print("Lista 2: ", lista2)
print("Lista 3: ", lista3)

saludo= "Hola mundo"

print("Hola" in saludo)