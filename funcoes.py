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