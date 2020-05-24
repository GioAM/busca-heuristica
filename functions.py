from queue import PriorityQueue
from models import *
from random import *


def popular_mapa(mapa, x, y):
    mapa_a_popular = []
    for i in range(x):
        mapa_a_popular.append([])
        for j in range(y):
            if mapa[i][j] == "G":
                coordenada = Coordenada('G', i, j, 10)
            elif mapa[i][j] == "A":
                coordenada = Coordenada('A', i, j, 1)
            elif mapa[i][j] == "P":
                coordenada = Coordenada('P', i, j, 3)
            elif mapa[i][j] == "T":
                coordenada = Coordenada('T', i, j, 6)
            elif mapa[i][j] == "E":
                coordenada = Coordenada('E', i, j, 0)
            mapa_a_popular[i].append(coordenada)

    return mapa_a_popular


def mostrar_mapa(mapa, x, y):
    for i in range(x):
        for j in range(y):
            print(mapa[i][j], end=" ")
        print('')
    print("")


def sortear_revendas(mapa):
    revendas = []
    numero_de_revendas = 0

    while numero_de_revendas < 3:
        x = int(random() * 42)
        y = int(random() * 42)
        if not mapa[x][y].valido():
            continue
        revenda = Revenda(x, y)
        revendas.append(revenda)
        numero_de_revendas += 1

    return revendas


def sortear_pessoas(mapa):
    pessoas = PriorityQueue()
    numero_de_pessoas = 0

    while numero_de_pessoas < 3:
        x = int(random() * 42)
        y = int(random() * 42)
        casa_x = int(random() * 42)
        casa_y = int(random() * 42)
        if not mapa[x][y].valido():
            continue
        if not mapa[casa_x][casa_y].valido():
            continue
        pessoa = Pessoa(x, y, casa_x, casa_y)
        pessoas.put([int(random() * 100), pessoa])
        numero_de_pessoas += 1

    numero_de_pessoas = 0

    while numero_de_pessoas < 3:
        x = int(random() * 42)
        y = int(random() * 42)
        casa_x = int(random() * 42)
        casa_y = int(random() * 42)
        if not mapa[x][y].valido():
            continue
        if not mapa[casa_x][casa_y].valido():
            continue
        pessoa = Pessoa(x, y, casa_x, casa_y, False)
        pessoas.put([int(random() * 100), pessoa])
        numero_de_pessoas += 1
    return pessoas


def buscar_alcool_gel(mapa, agente, revendas):
    revenda = choice(revendas)
    print("O Agente está no (%s,%s) e está indo buscar alcool gel na localização (%s,%s)"%(agente.x, agente.y, revenda.x, revenda.y))
    busca_heuristica(mapa, agente.x, agente.y, revenda.x, revenda.y)
    agente.x = revenda.x
    agente.y = revenda.y
    print("O Agente está na localização(%d,%d) pegando alcool gel" % (agente.x, agente.y))


def encontrar_pessoa(mapa, agente, pessoa):
    print("O Agente está no (%d,%d) e está indo até na pessoa que está na localização (%d,%d)" % (agente.x, agente.y, pessoa.x, pessoa.y))
    busca_heuristica(mapa, agente.x, agente.y, pessoa.x, pessoa.y)
    agente.x = pessoa.x
    agente.y = pessoa.y
    agente.sucesso = pessoa.ajuda
    print("O Agente está na localização(%d,%d) com uma pessoa" % (agente.x, agente.y))


def levar_para_casa(mapa, agente, pessoa):
    print("O Agente está no (%d,%d) e levando a pessoa para casa na localização (%d,%d)" % (agente.x, agente.y, pessoa.casa_x, pessoa.casa_y))
    busca_heuristica(mapa, agente.x, agente.y, pessoa.casa_x, pessoa.casa_y)
    agente.x = pessoa.casa_x
    agente.y = pessoa.casa_y
    print("O Agente levou uma pessoa para casa e está na localização(%d,%d)" % (agente.x, agente.y))


def busca_heuristica(mapa, origem_x, origem_y, destino_x, destino_y):
    print("")