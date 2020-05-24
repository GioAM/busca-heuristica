class Coordenada():
    def __init__(self, tipo, x, y, peso):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.peso = peso

    def __str__(self):
        return self.tipo

    def valido(self):
        if self.tipo == "E":
            return False
        return True


class Pessoa():
    def __init__(self, x, y, casa_x, casa_y, ajuda=True):
        self.x = x
        self.y = y
        self.casa_x = casa_x
        self.casa_y = casa_y
        self.ajuda = ajuda

class Agente():
    def __init__(self, x, y, sucesso=False):
        self.x = x
        self.y = y
        self.sucesso = sucesso

class Revenda():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.nome

