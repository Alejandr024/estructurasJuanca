from personaje import Personaje

class Elfo(Personaje):

    tipo_elfo=""

    def __init__(self, nombre, nivel, altura, tipo_elfo):
        super().__init__(nombre, nivel, altura)
        self.tipo_elfo= tipo_elfo

    def __str__(self):
        return f"Nombre Elfo: {self.nombre}; Nivel: {self.nivel} Altura: {self.altura}; TipoElfo: {self.tipo_elfo}"