archivo=None
try:
    #Abrir y leer fichero
    archivo = open("datos.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    print(" Contenido del fichero leido con exito:")
    print(contenido)
except FileNotFoundError:
# Captura específica si el archivo no existe en el disco
    print("X Error: El archivo 'datos.txt' no fue encontrado!. ")
except OSError as error:
# Captura otros errores de lectura/escritura o permisos del sistema operativo
    print(f"X Error de entrada/salida: {error}")
except Exception as error:
# Captura cualquier otra excepción no prevista
    print(f"X Ocurrió un error inesperado: {error}")
finally:
# 2. Se ejecuta SIEMPRE para cerrar el fichero y liberar recursos
    if archivo is not None and not archivo.closed:
        archivo.close()
        print(" Accion de limpieza: El fichero se ha cerrado correctamente.")
    else:
        print(" Accion de limpieza: El flujo finalizo sin necesidad de cerrar ficheros abiertos.")