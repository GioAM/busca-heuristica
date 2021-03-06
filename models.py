import math
from matriz import TAMANHO

class Mapa():
    def __init__(self, matriz, exibir_cores=False):
        self.exibir_cores = exibir_cores
        self.mapa = []
        for i in range(0, TAMANHO):
            self.mapa.append([])
            coordenada = Coordenada(0, 0)
            for j in range(0, TAMANHO):
                if matriz[i][j] == "G":
                    coordenada = Coordenada(i, j, '.', 10)
                elif matriz[i][j] == "A":
                    coordenada = Coordenada(i, j, '.', 1)
                elif matriz[i][j] == "P":
                    coordenada = Coordenada(i, j, '.', 3)
                elif matriz[i][j] == "T":
                    coordenada = Coordenada(i, j, '.', 6)
                elif matriz[i][j] == "E":
                    coordenada = Coordenada(i, j, '#', -1)
                self.mapa[i].append(coordenada)

    def reiniciar_mapa(self, agente, revendas, pessoas):
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                self.mapa[i][j].F = math.inf
                self.mapa[i][j].G = math.inf
                if self.mapa[i][j].tipo == "#":
                    self.mapa[i][j].tipo = "#"
                else:
                    self.mapa[i][j].tipo = "."
        for revenda in revendas:
            self.mapa[revenda.x][revenda.y].tipo = "R"
        for pessoa in pessoas.queue:
            self.mapa[pessoa[1].x][pessoa[1].y].tipo = "P"
            self.mapa[pessoa[1].casa_x][pessoa[1].casa_y].tipo = "C"
        self.mapa[agente.x][agente.y].tipo = "A"


    def mostrar_mapa(self):
        if self.exibir_cores:
            cores = {
            ".": '\33[1:30:40m',
            "#": '\33[1:31:41m',
            "P": '\33[1:33:43m',
            "A": '\33[1:34:44m',
            "R": '\33[1:35:45m',
            "C": '\33[1:36:46m',
            "|": '\33[1:32:42m',
            }
        else:
            cores = {
                ".": '',
                "#": '',
                "P": '',
                "A": '',
                "R": '',
                "C": '',
                "|": '',
            }
        print("Mapa - Visão Terrenos")
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                print(cores[self.mapa[i][j].tipo] + self.mapa[i][j].tipo , end=" ")
                print('\33[0:0m', end="")
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
    def __init__(self, x, y, tipo=".", peso=0, veio_de_y=0):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.peso = peso
        self.F = math.inf
        self.G = math.inf
        self.veio_de_x = 0
        self.veio_de_y = 0

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
        if self.tipo == "#":
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

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y <= other.y


class Agente():
    def __init__(self, x, y, mapa, sucesso=False):
        self.x = x
        self.y = y
        self.sucesso = sucesso
        mapa.mapa[self.x][self.y].tipo = "A"

class Revenda():
    def __init__(self, x, y):
        self.x = x
        self.y = y