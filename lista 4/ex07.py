def selecao_ordenacao(vetor):
    n = len(vetor) 

    for i in range(n):
        indice_minino = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minino]:
                indice_minino = j
            vetor[i], vetor[indice_minino] = vetor[indice_minino], vetor[i]
        
def terceiroMaior(vetor):
    selecao_ordenacao(vetor)
    if len(vetor) <= 2:
        print(" Neste vetor há menos que três elementos.")
        return None #vazio
    else:
        return print(vetor[2])

vetor = [3,5,6,4,8,9,2]
selecao_ordenacao(vetor)
print(vetor)
terceiroMaior(vetor)