# ciclo while
contador = 0

while contador <= 5:
    print(contador)
    contador += 1

    if contador == 3:
        break
else:
    print("el while ha terminado")

# ciclo for
print("--------------------------------")
lista = {1, 2, 3, 4, 5}

for valor in lista:
    print(valor)

"""rango"""
print("--------------------------------")
nuevo_rango = range(0, 8)
for valor in nuevo_rango:
    print(valor)

print("--------------------------------")
for indice, valor in enumerate(nuevo_rango):
    print(valor, "tiene el indice", indice)


print("--------------------------------")
diccionario = {
    'a': 1,
    'b': 2,
    'c': 3
}

for llave, valor in diccionario.items():
    print("la llave", llave, "tiene el valor de", valor)
