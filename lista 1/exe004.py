# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.
num = int(input("Digite um número inteiro:"))
num2 = int(input("Digite um número inteiro:"))
num3 = int(input("Digite um número inteiro:"))
num4 = int(input("Digite um número inteiro:"))

listan = [num, num2,num3,num4]

listaemOrdem = sorted(listan)
print(listaemOrdem)
print(f" O menor valor: {listaemOrdem[0]}" , f"O maior valor: {listaemOrdem[-1]}")


# Outra maneira
#  Procurando o menor valor
menor = num
if num2<num and num2<num3 and num2<num4:
    menor = num2
if num3<num and num3<num2 and num3<num4:
    menor = num3
if num4<num and num4<num2 and num4<num3:
    menor = num4
print("O menor valor é: {}.".format(menor))

# # Procurando o maior valor
maior= num
if num2>num and num2>num3 and num2>num4:
    maior= num2
if num3>num and num3>num2 and num3>num4:
    maior=num3
if num4>num and num4>num2 and num4>num3:
    maior = num4
print("O maior valor é: {}.".format(maior))