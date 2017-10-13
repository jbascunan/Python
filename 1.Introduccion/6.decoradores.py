def decorador(func):  # A,B
    # agregue codigo
    def before_action():
        print("vamos a ejecutar la funcion")

    # agregue codigo
    def after_action():
        print("se ejecuto la funcion")

    def nueva_funcion(*args, **kwargs):
        before_action()
        resultado = func(*args, **kwargs)
        after_action()
        return resultado

    return nueva_funcion  # C


@decorador
def saluda():
    print("Hola")


@decorador
def suma(valor1, valor2):
    return (valor1 + valor2)


resultado = suma(10, 20)
print(resultado)
