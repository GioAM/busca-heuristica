from functions import *
from matriz import *

mapa = popular_mapa(matriz(), 42, 42)
mostrar_mapa(mapa, 42, 42)
agente = Agente('Agente', 21, 25)
pessoas_ajudadas = 0
pessoas = sortear_pessoas(mapa)
revendas = sortear_revendas(mapa)

while pessoas_ajudadas < 3:
    buscar_alcool_gel(mapa, agente, revendas)
    pessoa = pessoas.get()
    encontrar_pessoa(mapa, agente, pessoa[1])
    if agente.sucesso:
        levar_para_casa(mapa, agente, pessoa[1])
        pessoas_ajudadas += 1
    else:
        print("Pessoa não quer ser levada para casa")

    print("----------------------------------------------------")