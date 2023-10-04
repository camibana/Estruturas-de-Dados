def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1,n):
            if vetor [j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo],vetor[i]

vetor = [4,8,9,7,2,3]
selecao_ordenacao(vetor)
print(vetor)