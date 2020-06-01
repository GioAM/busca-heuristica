from functions import *
from matriz import matriz
from models import Mapa

mapa = Mapa(matriz(), True)
if mapa.exibir_cores:
    print('\33[1:40:40m' + "Terreno que pode ser usado" + '\33[0:0m')
    print('\33[1:30:41m' + "Terreno que pode não ser usado (Edifício)" + '\33[0:0m')
    print('\33[1:30:45m' + "Revenda de Alcool Gel" + '\33[0:0m')
    print('\33[1:30:43m' + "Pessoa na rua" + '\33[0:0m')
    print('\33[1:30:44m' + "Agente" + '\33[0:0m')
    print('\33[1:30:46m' + "Casa de uma pessoa" + '\33[0:0m')
    print('\33[1:30:42m' + "Agente Passou" + '\33[0:0m')
else:
    print(" .  Terreno que pode ser usado")
    print(" #  Terreno que pode não ser usado (Edifício)")
    print(" R  Revenda de Alcool Gel")
    print(" P  Pessoa na rua")
    print(" A  Agente")
    print(" C  Casa de uma pessoa")
    print(" |  Agente Passou")

pessoas_ajudadas = 0
pessoas = sortear_pessoas(mapa)
revendas = sortear_revendas(mapa)
numero_de_pessoas = 0
agente = Agente(24, 20, mapa)
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
        mapa.mapa[pessoa.x][pessoa.y].tipo = "P"
        mapa.mapa[pessoa.casa_x][pessoa.casa_y].tipo = "C"
        levar_para_casa(mapa, agente, pessoa)
        mapa.reiniciar_mapa(agente, revendas, pessoas)
        pessoas_ajudadas += 1
    else:
        print('\33[1:30:41m'+"Pessoa não quer ser levada para casa" + '\33[0:0m')