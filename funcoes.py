def define_posicoes(linha, coluna, orientacao, tamanho):
    posição = []
    posição.append([linha, coluna])
    if tamanho > 1:
        if orientacao == "vertical":
            i = 1
            while i < tamanho:
                posição.append([linha+i, coluna])
                i += 1
        if orientacao == "horizontal":
            i = 1
            while i < tamanho:
                posição.append([linha, coluna+i])
                i += 1
    return posição

def preenche_frota(infofrota, nomenavio, linha, coluna, orientacao, tamanho):
    if nomenavio not in infofrota:
        infofrota[nomenavio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    else:
        infofrota[nomenavio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    return infofrota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def posiciona_frota(infofrota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for tipodenavio in infofrota:
        for navio in infofrota[tipodenavio]:
            for localnavio in navio:
                tabuleiro[localnavio[0]][localnavio[1]] = 1
    return tabuleiro

#frota = {'porta-aviões': [[[4, 0], [5, 0], [6, 0], [7, 0]]], 'navio-tanque': [[[1, 8], [2, 8], [3, 8]], [[0, 1], [0, 2], [0, 3]]], 'contratorpedeiro': [[[5, 4], [5, 5]], [[6, 5], [6, 6]], [[0, 5], [1, 5]]], 'submarino': [[[2, 4]], [[2, 6]], [[2, 3]], [[9, 8]]]}

#print(posiciona_frota(frota))

def afundados(infofrota, tabuleiro):
    mortos = 0
    for tipodenavio in infofrota:
        for navio in infofrota[tipodenavio]:
            vivo = False
            for localnavio in navio:
                if tabuleiro[localnavio[0]][localnavio[1]] == 1:
                    vivo = True
            if not vivo:
                mortos += 1
    return mortos

def posicao_valida(infofrota, linha, coluna, orientacao, tamanho):
    disponivel = True
    desejada = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in desejada:
        for tipodenavio in infofrota:
            for navio in infofrota[tipodenavio]:
                if posicao in navio:
                    disponivel = False
        for casa in desejada:
            if casa[0] >= 10 or casa[1] >= 10:
                disponivel = False
    return disponivel

#frota = {'porta-aviões': [[[2, 1], [3, 1], [4, 1], [5, 1]]]}
#linha: 8, coluna: 8, orientacao: vertical, tamanho: 3
#print(posicao_valida(frota, 8, 8, 'vertical', 3))

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto