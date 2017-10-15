class TinyIntError(Exception):
    pass


def tyni_int(val):
    return val >= 0 and val <= 255


try:
    numero = 400
    if tyni_int(numero):
        print("el numero es correcto")
    else:
        raise TinyIntError(
            "este es un mensaje para los numeros que no son tyni_int")
except TinyIntError as error:
    print(error)
