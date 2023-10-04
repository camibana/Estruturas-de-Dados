
def removeritensDuplicados(vetor):
    novoVetor = []
    for i in vetor:
        if i not in novoVetor:
            novoVetor.append(i)

    return novoVetor
        

vetor = [5,7,4,3,8,4,5]
print(vetor)
print(removeritensDuplicados(vetor))
