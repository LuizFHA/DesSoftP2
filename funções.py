def define_posicoes(linha, coluna, orientacao, tamanho):
    posição = []
    posição.append([linha, coluna])
    if tamanho > 1:
        if orientacao == "vertical":
            i = 2
            while i <= tamanho:
                posição.append([i, coluna])
                i += 1
        if orientacao == "horizontal":
            i = 2
            while i <= tamanho:
                posição.append([linha, i])
                i += 1
    return posição