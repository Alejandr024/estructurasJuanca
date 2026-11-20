import logging

# 1. Configuración del módulo logging
# Configuramos el archivo de auditoría donde se guardarán los registros de error.
logging.basicConfig(
    filename='auditoria_errores.log',
    filemode='a', # 'a' para anexar nuevos registros al archivo existente
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)


def realizar_division(dividendo, divisor):
    # Función que realiza una división e integra registro de errores profesional.
    print(f"Procesando operación: {dividendo} / {divisor}...")
    try:
        resultado = dividendo / divisor
        print(f"✅ Operación exitosa: Resultado = {resultado}\n")
        return resultado
    except Exception:
        # logging.exception registra el mensaje personalizado Y añade automáticamente
        # la traza completa de la excepción (traceback) con la línea exacta del fallo.
        logging.exception("Error crítico durante el cálculo de división en el sistema.")

        # Respuesta controlada para no colapsar la aplicación
        print("⚠️ Ocurrió un error interno. El fallo fue registrado en la auditoría y el programa continúa.\n")


# --- Simulación del flujo de ejecución de la aplicación ---
print("=== INICIO DE LA APLICACIÓN EN PRODUCCIÓN ===\n")

# Operación 1: Ejecución normal
realizar_division(100, 5)

# Operación 2: Provocamos un fallo (ZeroDivisionError)
realizar_division(50, 0)
# Operación 3: La aplicación NO colapsó y sigue atendiendo peticiones
realizar_division(80, 4)

print("=== FIN DE LA APLICACIÓN (Ejecución completada con éxito sin colapsar) ===")
