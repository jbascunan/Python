class Circulo:
    # variable de clase
    pi = 3.1416
    # metodo

    def __init__(self, radio):
        self.radio = radio
        self.perimetro = 4

    def suma(self):
        return "suma"


circulo1 = Circulo(1)
circulo2 = Circulo(2)

# obtiene valor de variable de clase sin instanciar
print(Circulo.pi)
# obtiene valor de variable de objeto(INSTANCIA)
print(circulo1.perimetro)
