#funcion
def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


# llama funcion
numero = 5
resultado = factorial(numero)

print(resultado)

# funcion con valor por defecto


def multiplicaion(valor1, valor2=10):
    return valor1 * valor2


resultado1 = multiplicaion(1, 5)
print(resultado1)

# funcion retorna multiples valores


def multiples_valores():
    return "string", 1, True, 25.6


string, entero, bol, floa = multiples_valores()
print(string)
print(entero)
print(bol)
print(floa)

# variable asigna funcion
mi_variable = multiplicaion
print(mi_variable(5, 1))


def mostrar_resultado(funcion):
    print(funcion(6, 8))


mostrar_resultado(mi_variable)
