# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

num = int(input("Digite um número inteiro:"))


if num < 0:
    print("O número deve ser positivo.")
else:
    fatorial = 1  # Inicializa o fatorial como 1
    
    for i in range(1, num + 1):
        fatorial *= i
    
    print(f"O fatorial de {num} é {fatorial}")
