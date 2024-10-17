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
        for navio in tipodenavio:
            for localnavio in navio:
                tabuleiro[localnavio[0]][localnavio[1]] = 1
    return tabuleiro