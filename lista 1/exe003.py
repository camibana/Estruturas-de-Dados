# . Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
# esse número.

num = int(input("Digite um número inteiro:"))

for n in range(0,num, 2):
    if n % 2 == 0:
        print(f"{n}", end="*")
