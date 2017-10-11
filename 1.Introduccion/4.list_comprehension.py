"""
lista = []  # false
for valor in range(1, 10):
    lista.append(valor)
"""

lista = [valor for valor in range(1, 10)]

# devuelve solamente numero pares
lista = [valor for valor in range(1, 10) if valor % 2 == 0]

tupla = tuple([valor for valor in range(1, 10) if valor %
               2 == 0])  # convierte a tupla

diccionario = {indice: valor for indice, valor in enumerate(
    lista) if valor % 2 == 0}  # convierte a diccionario

print(lista)
print(tupla)
print(diccionario)
