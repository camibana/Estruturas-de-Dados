def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1,n):
            if vetor [j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo],vetor[i]

def acharSegundoMenor(vetor):
    selecao_ordenacao(vetor)
    return print(vetor[1])

vetor = [5,7,4,3,9,1]
selecao_ordenacao(vetor)
print(vetor)
acharSegundoMenor(vetor)
