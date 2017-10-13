class Animal:  # clase abuelo
    @property
    def terrestre(self):
        return "animal"


class Felino(Animal):  # clase padre hereda de Animal
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("cazando")


class Gato(Felino):  # hereda de Felino
    def gato_cazador(self):
        self.cazar()


class Jaguar(Felino):  # hereda de Felino
    @classmethod
    def prueba(cls):
        print("prueba")

    @staticmethod
    def prueba2():
        print("prueba static")


gato = Gato()
jaguar = Jaguar()

print(gato.gato_cazador())
print(jaguar.garras_retractiles)

print(jaguar.terrestre)  # obtiene propiedad de clase herencia abuelo

Jaguar.prueba()
Jaguar.prueba2()
