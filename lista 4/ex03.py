# primeira opção

def acharMaximoMinimo(vetor):
    maximo = vetor[0]
    for i in vetor:
        if i > maximo:
            maximo = i

    minimo = vetor[0]
    for i in vetor:
        if i < minimo:
            minimo = i

    return maximo, minimo

vetor = [4,8,9,7,2,3]
acharMaximoMinimo(vetor)
resp = acharMaximoMinimo(vetor)
print(resp[0], resp[1])


# segunda maneira

def selecao_ordenada(vetor):
    n = len(vetor)

    for i in range(n):
        indice_mini = i
        for j in range(i+1,n):
            if vetor[j] < vetor[indice_mini]:
                indice_mini = j
        vetor[i],vetor[indice_mini] = vetor[indice_mini],vetor[i]

def elementoMaximo(vetor):
    print(vetor[0])
def elementoMinimo(vetor):
    print(vetor[-1])

vetor = [4,8,9,7,2,3]
selecao_ordenada(vetor)
print(vetor)
elementoMaximo(vetor)
elementoMinimo(vetor)