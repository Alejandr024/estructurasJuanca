class Perro:
    def sonido(self):
        print("Guauuuu!")

class Gato:
        def sonido(self):
            print("Miauuu!")

class Vaca:
        def sonido(self):
            print("Muuu!")

def oir_sonido(animales):
    for animal in animales:
        animal.sonido()

granja= [Perro(), Gato(), Vaca()]

oir_sonido(granja)