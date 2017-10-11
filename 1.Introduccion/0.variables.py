cadena1 = "curso sitio codigo"
cadena2 = "apellido"

result = cadena1.find("sitio")
result2 = cadena1.count("s")

result3 = cadena1.split(" ")

print(result)
print(result3)

# string como arreglo
print(cadena1[3])

# subsring
print(cadena1[0:5])  # return curso

# listas
miLista = ["uno", 2]
miLista.append("dos")  # agrega dato al arreglo
print(miLista)
miLista.insert(1, "tres")  # inserta dato en la posicion
print(miLista)
# miLista.remove(0)  # elimina dato al arreglo en la posicion
# print(miLista)
posicion = miLista.pop()  # elimina ultimo registro

miListaEnteros = [5, 2, 1, 4]
miListaEnteros2 = [6, 8]
miListaEnteros.sort()  # ordena en forma ascendente
print(miListaEnteros)
miListaEnteros.sort(reverse=True)  # ordena en forma descendente
print(miListaEnteros)
miListaEnteros.extend(miListaEnteros2)  # unir listas
print(miListaEnteros)
