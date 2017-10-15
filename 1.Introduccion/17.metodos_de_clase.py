class Animal:
    volador = True


class Cocodrilo(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    
    @classmethod
    def new(cls, nombre):
        return Cocodrilo(nombre)


cocodrilo = Cocodrilo.new("coco")
print(cocodrilo.nombre)

