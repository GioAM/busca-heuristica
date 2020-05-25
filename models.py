import math
from matriz import TAMANHO


class Mapa():
    def __init__(self, matriz):
        self.mapa = []
        for i in range(TAMANHO):
            self.mapa.append([])
            coordenada = Coordenada(0, 0)
            for j in range(TAMANHO):
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
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                self.mapa[i][j].F = math.inf
                self.mapa[i][j].G = math.inf

    def mostrar_mapa(self):
        print("")
        print("Mapa - Visão Terrenos")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(self.mapa[i][j].tipo, end=" ")
            print('')
        print("")

    def mostrar_parede(self):
        print("")
        print("Mapa - Visão Paredes")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                if self.mapa[i][j].peso > 0:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print('')
        print("")

    def mostrar_mapa_G(self):
        print("")
        print("Mapa - Visão G")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(self.mapa[i][j].G, end=" ")
            print('')
        print("")

    def mostrar_mapa_F(self):
        print("")
        print("Mapa - Visão F")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
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

    def __repr__(self):
        return "(%s,%s)"%(self.x, self.y)

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y <= other.y

    def atribuir_valores(self, F, G):
        self.F = F
        self.G = G

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

    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)


class Agente():
    def __init__(self, x, y, sucesso=False):
        self.x = x
        self.y = y
        self.sucesso = sucesso


class Revenda():
    def __init__(self, x, y):
        self.x = x
        self.y = y