name= str(input("Introduce tu nombre: ")).strip().lower()
codigoPostal= input("Introduce tu código postal: ").strip()

if not name:
    print("Error en el registro: campo vacío.")
elif not codigoPostal.isdigit():
    print("Error en el registro: codigo postal no numérico.")
else:
    print(f"Registro válido. Usuario: {name} | CP: {codigoPostal}")