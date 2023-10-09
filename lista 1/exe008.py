# Faça um programa que determine se um número é primo ou não.

num_str = input("Digite um número inteiro: ")

if num_str.isdigit():  # Verifica se o número é um número inteiro positivo

    num = int(num_str)

    if num < 2:
        print(num, "não é um número primo.")
    else:
        # Inicializa uma variável para contar os divisores
        divisors = 0

        # Loop para verificar se o número é primo
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors += 1
                break

        if divisors == 0:          # Se divisors for 0, o número é primo; caso contrário, não é
            print(num, "Esse é um número primo.")
        else:
            print(num, "Esse não é um número primo.")
else:
    print("O número digitado não é válido, digite um número inteiro válido.")