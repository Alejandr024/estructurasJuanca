from personaje import Personaje

class Hombre(Personaje):

    edad=0
    
    def __init__(self, nombre, nivel, altura, edad):
        super().__init__(nombre, nivel, altura)
        self.edad= edad

    def __str__(self):
        return f"Nombre Hombre: {self.nombre}; Nivel: {self.nivel}; Altura: {self.altura}; Edad: {self.edad}"