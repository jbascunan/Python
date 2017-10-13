class Circulo:
    # variable de clase
    pi = 3.1416

    # METODO ESTATICO
    @staticmethod
    def pi2():
        return 3.14

    # CONSTRUCTOR
    def __init__(self, radio):
        self.radio = radio
        self.perimetro = 4

    # METODO DE INSTACIA
    def suma(self):
        return "suma"


circulo1 = Circulo(1)
circulo2 = Circulo(2)

# obtiene valor de variable de clase
print(Circulo.pi)
# obtiene valor de metodo de clase
print(Circulo.pi2())
# obtiene valor de variable de objeto (instancia)
print(circulo1.perimetro)
print(circulo1.pi)

print(Circulo.suma())
