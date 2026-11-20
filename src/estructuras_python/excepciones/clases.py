class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# Orden Correcto: Subclases específicas primero
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D - Capturado como Subclase Específica D")
    except C:
        print("C - Capturado como Subclase Intermedia C")
    except B:
        print("B - Capturado como Clase Base B")