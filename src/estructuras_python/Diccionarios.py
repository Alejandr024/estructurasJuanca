inventario ={"manzanas":50, "peras":30, "naranjas":100}
frutas=[]
for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad}")
    frutas.append(fruta)
print(frutas)