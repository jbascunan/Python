try:
    print(2 / 0)
except Exception as ex:
    print("se ha producido un error:", ex)
finally:
    print("siempre se ejecuta")
