class Lapiz:  # pantilla
    tipo = 'lapicera'

    # constructor
    def __init__(self, color, contiene_borrador, usa_grafo):
        # atributos
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafo = usa_grafo

    # Metodos
    def dibujar(self):
        print("el lapiz esta dibujando")

    def borrar(self):
        if self.es_valido_para_borrar():
            print("borrando")
        else:
            print("no se puede borrar")

    def es_valido_para_borrar(self):
        return self.contiene_borrador


# objeto de lapiz
lapiz_generico = Lapiz('amarillo', True, True)

lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
print(lapiz_generico.tipo)
