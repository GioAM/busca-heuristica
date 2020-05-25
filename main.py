from functions import *
from matriz import matriz
from models import Mapa

print(" .  Terreno que pode ser usado")
print(" #  Terreno que pode não ser usado (Edifício)")
print(" R  Revenda de Alcool Gel")
print(" P  Pessoa na rua")
print(" A  Agente")
#print(" |  Agente Passou")

mapa = Mapa(matriz())
agente = Agente(0, 0, mapa)
pessoas_ajudadas = 0
pessoas = sortear_pessoas(mapa)
revendas = sortear_revendas(mapa)
numero_de_pessoas = 0

mapa.mostrar_mapa()
while pessoas_ajudadas < 3:
    numero_de_pessoas += 1
    print("-------------------------- Pessoa %s ----------------------------------"%(numero_de_pessoas))
    buscar_alcool_gel(mapa, agente, revendas)
    mapa.reiniciar_mapa(agente, revendas, pessoas)
    pessoa = pessoas.get()[1]
    encontrar_pessoa(mapa, agente, pessoa)
    mapa.reiniciar_mapa(agente, revendas, pessoas)
    if agente.sucesso:
        levar_para_casa(mapa, agente, pessoa)
        mapa.reiniciar_mapa(agente, revendas, pessoas)
        pessoas_ajudadas += 1
    else:
        print("Pessoa não quer ser levada para casa")