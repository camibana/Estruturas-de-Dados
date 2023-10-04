def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1,n):
            if vetor [j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo],vetor[i]

def encontrar_max_min(vetor):
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento

    minimo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return maximo, minimo