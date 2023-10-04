import minhabiblioteca as mb    

vetor = [5,7,4,2,4,7,3]

print(vetor)
mb.selecao_ordenacao(vetor)
print(vetor)

n = len(vetor)

def acharMediana(vetor):
    mb.selecao_ordenacao(vetor)

    if len(vetor) % 2 ==0:
        meio1 = vetor[n // 2 - 1]
        meio2 = vetor[n // 2]
        return print((meio1 + meio2) / 2)
    else:
        return print(vetor[n // 2])


acharMediana(vetor)
