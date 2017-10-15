#!/usr/bin/python3
"""
aqui colocamos todo lo que hace el modulo
"""
__autor__ = "jose bascuñan"


def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial


def multiplicaion(valor1, valor2=10):
    return valor1 * valor2


def multiples_valores():
    return "string", 1, True, 25.6
