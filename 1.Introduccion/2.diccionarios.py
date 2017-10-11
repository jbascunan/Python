# las llaves puede ser string o enteros
diccionario = {
    'a': 1,
    'b': 2,
    'c': 3
}

# diccionario de llave enteros
diccionario1 = {
    1: "nada",
    2: "nada2"
}
print(diccionario1)

# agregar clave/valor
diccionario['d'] = 4
# modifica valor
diccionario['e'] = 5  # si la llave existe se actualiza sino la crea

print(diccionario)

# obtener valor por la clave
valor = diccionario['a']
print(valor)

# obtener valor por defecto cuando no existe llave
valor2 = diccionario.get('z', False)
print(valor2)

# eliminar llave/valor segun llave
del diccionario['e']
print(diccionario)

# obtener objeto iterable
llaves = diccionario.keys()  # obtiene llaves
print(llaves)
llaves1 = list(diccionario.keys())  # obtiene objeto como lista
print(llaves1)

valores = diccionario.values()  # obtiene valores
print(valores)
valores2 = list(valores)  # obtiene objeto como lista
print(valores2)

# unir diccionarios
diccionario.update(diccionario1)
print(diccionario)
