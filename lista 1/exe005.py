# Faça um programa que leia uma lista de números e retorne a média dos números pares.

num = int(input("Digite um número inteiro:"))
num2 = int(input("Digite um número inteiro:"))
num3 = int(input("Digite um número inteiro:"))
num4 = int(input("Digite um número inteiro:"))
num5 = int(input("Digite um número inteiro:"))

listan = [num, num2,num3,num4,num5]
print(listan)

listapar = []

for i in (listan):
    if i % 2 == 0:
        listapar.append(i)

print (listapar)

mediapares = sum(listapar) / len(listapar) #usei o sum para somar os itnes da lista e usei o len para saber o tamanho da lista
print(mediapares)
    

