from funcoes import *
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     
nome = 'porta-aviões'
tamanho = 4
quantidade = 1
while quantidade > 0:
    print('Insira as informações referentes ao navio',nome,'que possui tamanho',tamanho)
    linha = int(input('Digite a linha '))
    coluna = int(input('Digite a coluna '))
    orientacao = int(input('Digite a orientacao '))
    if orientacao == 1:
        orientacao = "vertical"
    elif orientacao == 2:
        orientacao = "horizontal"
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
    else:
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        quantidade -= 1
    
nome = "navio-tanque"
tamanho = 3
quantidade = 2
while quantidade > 0:
    print('Insira as informações referentes ao navio',nome,'que possui tamanho',tamanho)
    linha = int(input('Digite a linha '))
    coluna = int(input('Digite a coluna '))
    orientacao = int(input('Digite a orientacao '))
    if orientacao == 1:
        orientacao = "vertical"
    elif orientacao == 2:
        orientacao = "horizontal"
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
    else:
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        quantidade -= 1

nome = "contratorpedeiro"
tamanho = 2
quantidade = 3
while quantidade > 0:
    print('Insira as informações referentes ao navio',nome,'que possui tamanho',tamanho)
    linha = int(input('Digite a linha '))
    coluna = int(input('Digite a coluna '))
    orientacao = int(input('Digite a orientacao '))
    if orientacao == 1:
        orientacao = "vertical"
    elif orientacao == 2:
        orientacao = "horizontal"
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
    else:
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        quantidade -= 1

nome = "submarino"
tamanho = 1
quantidade = 4
while quantidade > 0:
    print('Insira as informações referentes ao navio',nome,'que possui tamanho',tamanho)
    linha = int(input('Digite a linha '))
    coluna = int(input('Digite a coluna '))
    #orientacao = input('Digite a orientacao ')
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
    else:
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        quantidade -= 1