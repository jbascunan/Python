class Lapiz:  # pantilla
    # atributos
    color = 'amarillo'
    contiene_borrador = False
    usa_grafo = True

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
lapiz_generico = Lapiz()

lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
