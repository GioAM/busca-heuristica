from queue import PriorityQueue
from models import *
from random import *


def sortear_revendas(mapa):
    revendas = []
    numero_de_revendas = 0

    while numero_de_revendas < 3:
        x = int(random() * 10)
        y = int(random() * 10)
        if not mapa.mapa[x][y].valido():
            continue
        revenda = Revenda(x, y)
        revendas.append(revenda)
        numero_de_revendas += 1

    return revendas


def sortear_pessoas(mapa):
    pessoas = PriorityQueue()
    numero_de_pessoas = 0

    while numero_de_pessoas < 3:
        x = int(random() * 10)
        y = int(random() * 10)
        casa_x = int(random() * 10)
        casa_y = int(random() * 10)
        if not mapa.mapa[x][y].valido():
            continue
        if not mapa.mapa[casa_x][casa_y].valido():
            continue
        pessoa = Pessoa(x, y, casa_x, casa_y)
        pessoas.put((random()*100, pessoa))
        numero_de_pessoas += 1

    numero_de_pessoas = 0

    while numero_de_pessoas < 3:
        x = int(random() * 10)
        y = int(random() * 10)
        casa_x = int(random() * 10)
        casa_y = int(random() * 10)
        if not mapa.mapa[x][y].valido():
            continue
        if not mapa.mapa[casa_x][casa_y].valido():
            continue
        pessoa = Pessoa(x, y, casa_x, casa_y, False)
        pessoas.put((int(random() * 100), pessoa))
        numero_de_pessoas += 1
    return pessoas


def buscar_alcool_gel(mapa, agente, revendas):
    revenda = choice(revendas)
    print("O Agente está no (%s,%s) e está indo buscar alcool gel na localização (%s,%s)"%(agente.x, agente.y, revenda.x, revenda.y))
    origem = mapa.mapa[agente.x][agente.y]
    destino = mapa.mapa[revenda.x][revenda.y]
    busca_heuristica(mapa, origem, destino)
    agente.x = revenda.x
    agente.y = revenda.y
    print("O Agente está na localização(%d,%d) pegando alcool gel" % (agente.x, agente.y))
    input("-------------------------- Pressione Enter para a próxima ação ----------------------------------")


def encontrar_pessoa(mapa, agente, pessoa):
    print("O Agente está no (%d,%d) e está indo até na pessoa que está na localização (%d,%d)" % (agente.x, agente.y, pessoa.x, pessoa.y))
    origem = mapa.mapa[agente.x][agente.y]
    destino = mapa.mapa[pessoa.x][pessoa.y]
    busca_heuristica(mapa, origem, destino)
    agente.x = pessoa.x
    agente.y = pessoa.y
    agente.sucesso = pessoa.ajuda
    print("O Agente está na localização(%d,%d) com uma pessoa" % (agente.x, agente.y))
    input("-------------------------- Pressione Enter para a próxima ação ----------------------------------")


def levar_para_casa(mapa, agente, pessoa):
    print("O Agente está no (%d,%d) e levando a pessoa para casa na localização (%d,%d)" % (agente.x, agente.y, pessoa.casa_x, pessoa.casa_y))
    origem = mapa[agente.x][agente.y]
    destino = mapa[pessoa.casa_x][pessoa.casa_y]
    busca_heuristica(mapa, origem, destino)
    agente.x = pessoa.casa_x
    agente.y = pessoa.casa_y
    print("O Agente levou uma pessoa para casa e está na localização(%d,%d)" % (agente.x, agente.y))
    input("-------------------------- Pressione Enter para a próxima ação ----------------------------------")


def busca_heuristica(mapa, origem, destino):
    print("Buscando")
    print("")
    fronteira = PriorityQueue()
    fronteira.put([0, origem])

    mapa[origem.x][origem.y].F = 0 + heuristica(origem, destino)
    mapa[origem.x][origem.y].G = 0
    while not fronteira.empty():
        atual = fronteira.get()[1]
        if atual.x == destino.x and atual.y == destino.y:
            print("Você chegou no seu destino (%s,%s)"%(atual.x, atual.y))
            while not fronteira.empty():
                fronteira.get()
            break

        for vizinho in vizinhos(atual, mapa):
            custo_atual = vizinho.peso + atual.G

            if custo_atual < mapa[vizinho.x][vizinho.y].G:
                mapa[vizinho.x][vizinho.y].G = custo_atual
                mapa[vizinho.x][vizinho.y].F = custo_atual + heuristica(vizinho, destino)
                fronteira.put((mapa[vizinho.x][vizinho.y].F, mapa[vizinho.x][vizinho.y]))
    print("")
    print("Final da Busca")


def vizinhos(atual, mapa):
    vizinhos = []
    DIRECOES=[
        Coordenada(0, -1),
        Coordenada(0, 1),
        Coordenada(1, 0),
        Coordenada(-1, 0)
    ]

    for direcao in DIRECOES:
        vizinho = Coordenada(atual.x + direcao.x, atual.y + direcao.y)

        if vizinho.valido() and mapa[vizinho.x][vizinho.y].valido():
            vizinhos.append(mapa[vizinho.x][vizinho.y])
    return vizinhos


def heuristica(atual, destino):
    return abs(atual.x - destino.x) + abs(atual.y - destino.y)