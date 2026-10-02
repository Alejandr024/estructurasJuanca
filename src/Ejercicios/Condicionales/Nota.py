nota=float(input("Introduce la nota del examen: "))

match nota:
    case nota if 0<= nota <5:
        print("Suspendido")
    case nota if 5<= nota <7:
        print("Aprobado")
    case nota if 7<= nota <8.5:
        print("Notable")
    case nota if 8.5<= nota <=10:
        print("Sobresaliente")
    case _:
        print("Nota no válida, introdúzcalo de nuevo.")
