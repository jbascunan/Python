class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()


usuario = Usuario('pruebqa', 'unodostres', 'prueba@prueba.cl')

usuario.__password = 'nada'

print(usuario.username)
print(usuario.__password)
print(usuario.email)
