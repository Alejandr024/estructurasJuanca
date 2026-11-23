class Personaje:

    nombre=""
    nivel=0
    altura=0.00
    
    def __init__(self, nombre, nivel, altura):
        self.nombre= nombre
        self.nivel= nivel
        self.altura= altura

    def subir_nivel(self):
        self.nivel+=1
        return f"Has subido de nivel. Nivel actual: {self.nivel}"

    def __str__(self):
        return f"Nombre: {self.nombre}; Nivel: {self.nivel}; Altura: {self.altura}"
