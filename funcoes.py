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
