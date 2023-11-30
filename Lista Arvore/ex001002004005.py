# RESPOSTAS A LISTA ARVORE BINÁRIA 
# 1.Diante da seguinte estrutura de árvore abaixo, responda as questões:
#a) 10
#b) 3
#c) H
#d) A,C,J,L,M,N
#e) H,B,F,E
#f) A,C,J,E
#g) F, H
#h) J,E,L,M,N

# 2.Diante da seguinte estrutura de árvore binária abaixo, responda as questões:
#a) Pré - ordem: D-B-A-C-F-E-G
#b) Pós - ordem: A-C-B-E-G-F-D
#c) Em - ordem: A-B-C-D-E-F-G

# 3. Numa tabela em pdf a parte.


# 4. 4.Imagine uma árvore binária representando uma árvore genealógica. Cada nó possui informações sobre um membro da família. Desenvolva um código em Python para criar e imprimir essa árvore.


class No:
    def __init__(self, nome, anoNascimento=None, esquerda=None, direita=None):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.esquerda = esquerda
        self.direita = direita

def print_tree(no, level=0, prefix="Raiz:"):
    if no is not None:
        print(" " * (level * 4) + f"{prefix} {no.nome} ({no.anoNascimento})")
        print_tree(no.esquerda, level + 1, "Esquerda:")
        print_tree(no.direita, level + 1, "Direita:")

# Exemplo de construção da árvore genealógica
# Instancioando o objeto criado pela classe e metodo contrutor - criando os nós da árvore-
avo = No("Avô", 1964)
avoo = No("Avó", 1966)
pai = No("Pai", 1988, avo, avoo)
mae = No("Mãe", 1990)
filho1 = No("Filho Primogênito", 2015, pai, mae)
filho2 = No("Segundo Filho", 2021, pai, mae)

# Imprimindo a árvore
print_tree(filho1)

# 5. Considere uma árvore binária que representa uma expressão matemática, onde cada nó é um operador ou um número. Veja a árvore abaixo e responda as questões abaixo:

#a) Em ordem, lendo Esquerda, Raiz e Direita.
