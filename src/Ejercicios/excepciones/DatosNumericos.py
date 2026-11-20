total = 0
numeros_validos=0
class FicheroVacioError(Exception):
    pass
try:
    nombre_fichero = input("Nombre o ruta del fichero: ")
    with open(nombre_fichero, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            try:

                numero=int(linea.strip())
            except ValueError:
                print(f"Advertencia: dato no válido en la línea {numero_linea}")
                continue
            
            total+=numero
            numeros_validos+=1

        if numeros_validos==0:
            raise FicheroVacioError("No hay datos procesables")
        print(total)
except FileNotFoundError:
    print("Error: archivo no encontrado.")
except PermissionError as error:
    print(f"Error de permisos: {error}")
except OSError as error:
    print(f"Error de entrada/salida: {error}")
except FicheroVacioError as error:
    print(error)
except KeyboardInterrupt:
    print("\nEjecución cancelada. ¡Hasta luego!")
finally:
    print("Proceso de lectura finalizado")