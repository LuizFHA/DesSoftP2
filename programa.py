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
    linha = int(input('Digite a linha inicial '))
    coluna = int(input('Digite a coluna inicial '))
    orientacao = int(input('Digite a orientação. Digite 1 para vertical e 2 para horizontal '))
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
    linha = int(input('Digite a linha inicial '))
    coluna = int(input('Digite a coluna inicial '))
    orientacao = int(input('Digite a orientação. Digite 1 para vertical e 2 para horizontal '))
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
    linha = int(input('Digite a linha inicial '))
    coluna = int(input('Digite a coluna inicial  '))
    orientacao = int(input('Digite a orientação. Digite 1 para vertical e 2 para horizontal '))
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
    linha = int(input('Digite a linha inicial '))
    coluna = int(input('Digite a coluna inicial '))
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
    else:
        frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        quantidade -= 1

#print(frota)

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

taboponente = posiciona_frota(frota_oponente)

tabjogador = posiciona_frota(frota)

jogando = True

listajogadas = []

while jogando:
    print(monta_tabuleiros(tabjogador, taboponente))
    ataque = False
    while ataque == False:
        valido = False
        while valido == False:
            ataquel = int(input("Qual linha você quer atacar? "))
            if ataquel > 9 or ataquel < 0:
                print('Coluna inválida!')
            else:
                valido = True
        valido = False
        while valido == False:
            ataquec = int(input("Qual coluna você quer atacar? "))
            if ataquec > 9 or ataquec < 0:
                print('Coluna inválida!')
            else:
                valido = True
        if [ataquel, ataquec] not in listajogadas:
            listajogadas.append([ataquel, ataquec])
            ataque = True
        else:
            print('A posição linha',ataquel,'e coluna',ataquec,'já foi informada anteriormente!')
    taboponente = faz_jogada(taboponente,ataquel,ataquec)
    if afundados(frota_oponente, taboponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False