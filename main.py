from functions import *
from matriz import matriz
from models import Mapa

mapa = Mapa(matriz())
mapa.mostrar_parede()
mapa.mostrar_mapa()
agente = Agente(21, 25)
pessoas_ajudadas = 0
pessoas = sortear_pessoas(mapa)
revendas = sortear_revendas(mapa)
numero_de_pessoas = 0

while pessoas_ajudadas < 3:
    numero_de_pessoas += 1
    print("-------------------------- Pessoa %s ----------------------------------"%(numero_de_pessoas))
    buscar_alcool_gel(mapa, agente, revendas)
    pessoa = pessoas.get()[1]
    encontrar_pessoa(mapa, agente, pessoa)
    if agente.sucesso:
        levar_para_casa(mapa, agente, pessoa)
        pessoas_ajudadas += 1
    else:
        print("Pessoa não quer ser levada para casa")