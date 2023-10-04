def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1,n):
            if vetor [j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo],vetor[i]

def conta_par_imp(vetor):
    n = len(vetor)
    cpar = 0
    cimp = 0
    for i in range(n):
        if i % 2 == 0:
            cpar +=1
        else:
            cimp +=1
    
    return cpar , cimp

vetor = [5,7,4,3,6]
selecao_ordenacao(vetor)
conta_par_imp(vetor)
print(vetor)
print(conta_par_imp(vetor))