'''
Enunciado: Tienes una lista de tareas pendientes: ["Comprar leche", "Llamar al médico",
"Estudiar Python"]. Imprimelas numeradas empezando desde el 1 para mostrarlas como una
lista ordenada
'''
tareas = ["Comprar leche", "Llamar al médico", "Estudiar Python"]

for indice, tarea in enumerate(tareas, start=1):
    print(f"{indice}. {tarea}")
