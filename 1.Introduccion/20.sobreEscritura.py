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


class Mascota:
    nombre = ''

    def mostrar_nombre(self):
        print(self.nombre)


class Gato(Felino, Mascota):  # hereda de Felino y Mascota
    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self):  # sobreescritura de metodos
        Mascota.mostrar_nombre(self)
        print("self.nombre")


gato = Gato()
gato.nombre = "Tom"

gato.mostrar_nombre()  # herencia mascota
gato.cazar()  # herencia felino
