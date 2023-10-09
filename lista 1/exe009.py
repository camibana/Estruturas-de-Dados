# Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'.

listaNomes = ["Ana", "Paula", "Aldo", "Carla", "Diego", "Fernando", "Abel"]

listaNomesOrdem = sorted(listaNomes) # organizando a lista por ordem alfabética

print(listaNomesOrdem)

listaNomesA = []

for nome in listaNomes:
    if nome[0] == "A":
        listaNomesA.append(nome) # adicionando itens a lista que antes era vazia.

print(listaNomesA)