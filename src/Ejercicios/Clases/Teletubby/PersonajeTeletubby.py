class PersonajeTeletubby:
    # Atributo de clase
    saludo_oficial = "¡Tubby abrazo!"

    def __init__(self, nombre: str, color: str, antena: str, objeto_favorito: str):
        # Atributos públicos
        self.nombre = nombre
        self.color = color
        self.antena = antena
        self.objeto_favorito = objeto_favorito

        # Atributos privados
        self.__nivel_hambre = 50
        self.__nivel_felicidad = 100

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, soy de color {self.color} y mi antena tiene forma de {self.antena}.")

    def jugar(self):
        print(f"{self.nombre} está jugando alegremente con su {self.objeto_favorito}.")
        self.__nivel_hambre += 20
        self.__nivel_felicidad += 10

    def comer_tubby_papilla(self):
        print(f"{self.nombre} está comiendo una deliciosa Tubby-papilla. ¡Yum yum!")
        self.__nivel_hambre = 0
        self.__nivel_felicidad += 20

    def ver_estado(self) -> str:
        return f"Estado de {self.nombre} -> Felicidad: {self.__nivel_felicidad} | Hambre: {self.__nivel_hambre}"
    '''
        def __repr__(self):
            return f"Teletubby\n Nombre: {self.nombre}\n Color: {self.color}\n Antena: {self.antena}\n Objeto Favorito: {self.objeto_favorito}\n"
    '''

    '''
    '''
    def __str__(self):
        return f"Teletubby '{self.nombre}' color {self.color}, antena {self.antena} | Felicidad: {self.__nivel_felicidad} | Hambre: {self.__nivel_hambre}"

if __name__ == "__main__":
    # 1. Instanciación de dos objetos de la clase
    tinky_winky = PersonajeTeletubby("Tinky Winky", "morado", "triángulo", "bolso rojo")
    po = PersonajeTeletubby("Po", "rojo", "círculo", "patinete")

    print("Representación de cada Teletubby.")
    print(tinky_winky)
    print(po)
    # 2. Saludo de los personajes y presentación del saludo oficial de clase
    print(f"Saludo Oficial: {PersonajeTeletubby.saludo_oficial}\n")
    tinky_winky.saludar()
    po.saludar()
    print("-" * 60)

    # 3. Invocar el método jugar() en ambos personajes
    tinky_winky.jugar()
    po.jugar()
    print("-" * 60)

    # 4. Mostrar el estado interno usando ver_estado()
    print(tinky_winky.ver_estado())
    print(po.ver_estado())
    print("-" * 60)

    # 5. Hacer que solo Po coma tubby papilla
    po.comer_tubby_papilla()
    print("-" * 60)

    # 6. Comprobación del estado final de ambos personajes
    print(tinky_winky.ver_estado())
    print(po.ver_estado())