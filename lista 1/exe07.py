# Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.
try:
 
    valorMaximo = int(input("Digite um valor máximo para a sequência de Fibonacci: "))
    if valorMaximo < 0:
        print("Por favor, digite um valor positivo.")
    else:
        a, b = 0, 1
        print("Essa é a sequência de Fibonacci até", valorMaximo, ":")
        while a <= valorMaximo:
            print(a, end=" ")
            a, b = b, a + b
except ValueError:
    print("Por favor, digite um valor válido.")