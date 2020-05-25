from functions import *
from matriz import *
TAMANHO = 10
mapa = Mapa(matriz())
agente = Agente(0, 0)
pessoas_ajudadas = 0
pessoas = sortear_pessoas(mapa)
revendas = sortear_revendas(mapa)

while pessoas_ajudadas < 3:
    buscar_alcool_gel(mapa, agente, revendas)
    pessoa = pessoas.get()[1]
    encontrar_pessoa(mapa, agente, pessoa)
    agente.sucesso = True
    if agente.sucesso:
        levar_para_casa(mapa, agente, pessoa)
        pessoas_ajudadas += 1
    else:
        print("Pessoa não quer ser levada para casa")

    print("----------------------------------------------------")