class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password = self.__generar_password(valor)


usuario = Usuario('pruebqa', 'unodostres', 'prueba@prueba.cl')

print(usuario.password)
# set password
usuario.password = 'nuevo password'
print(usuario.password)

# print(usuario.__password)
# print(usuario.email)
