import math
from main import TAMANHO


class Mapa():
    def __init__(self, matriz):
        x, y = TAMANHO
        self.mapa = []
        for i in range(x):
            self.mapa.append([])
            coordenada = Coordenada(0, 0)
            for j in range(y):
                if matriz[i][j] == "G":
                    coordenada = Coordenada(i, j, 'G', 10)
                elif matriz[i][j] == "A":
                    coordenada = Coordenada(i, j, 'A', 1)
                elif matriz[i][j] == "P":
                    coordenada = Coordenada(i, j, 'P', 3)
                elif matriz[i][j] == "T":
                    coordenada = Coordenada(i, j, 'T', 6)
                elif matriz[i][j] == "E":
                    coordenada = Coordenada(i, j, 'E', -1)
                self.mapa[i].append(coordenada)

    def reiniciar_mapa(self):
        x, y = TAMANHO
        for i in range(x):
            for j in range(y):
                self.mapa[i][j].F = math.inf
                self.mapa[i][j].G = math.inf

    def mostrar_mapa(self):
        x, y = TAMANHO
        for i in range(x):
            for j in range(y):
                print(self.mapa[i][j], end=" ")
            print('')
        print("")

    def mostrar_parede(self):
        x, y = TAMANHO
        for i in range(x):
            for j in range(y):
                if self.mapa[i][j].peso > 0:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print('')
        print("")

    def mostrar_mapa_G(self):
        x, y = TAMANHO
        for i in range(x):
            for j in range(y):
                print(self.mapa[i][j].G, end=" ")
            print('')
        print("")

    def mostrar_mapa_F(self):
        x, y = TAMANHO
        for i in range(x):
            for j in range(y):
                print(self.mapa[i][j].F, end=" ")
            print('')
        print("")


class Coordenada():
    def __init__(self, x, y, tipo="*", peso=0):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.peso = peso
        self.F = math.inf
        self.G = math.inf

    def __str__(self):
        return self.tipo

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y <= other.y

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