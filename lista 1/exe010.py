# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. 
# O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.


import random

opcoes = ["Pedra", "Papel", "Tesoura"]

print("Escolha uma opção: 1. Pedra, 2. Papel, 3. Tesoura")

escolha = int(input("Digite o número da sua escolha (1/2/3): "))

if escolha < 1 or escolha > 3:  # Verifica se a escolha do usuário é válida
    print("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
else:
    escolha = opcoes[escolha - 1]  # Converte a escolha do usuário em texto

    escolhaComputador = random.choice(opcoes)
    print(f"O computador escolheu: {escolhaComputador}")

    if escolha == escolhaComputador:
        print("Empate!")
    elif (
        (escolha == "Pedra" and escolhaComputador == "Tesoura")
        or (escolha == "Papel" and escolhaComputador == "Pedra")
        or (escolha == "Tesoura" and escolhaComputador == "Papel")
    ):
        print("Parabéns, Você ganhou!:D ")
    else:
        print("Você perdeu e o computador ganhou!")
