def generador(*args):
    for valor in args:
        yield valor * 10, True  # retorna 2 valores en este ejemplo


for valor1, valor2 in generador(1, 2, 3, 4, 5):
    print(valor1, valor2)
