# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self):
        deposito = float(input("Insira o valor do depósito em R$: "))
        self.saldo += deposito

        return self.saldo
    
    def sacar(self):
        saque = float(input("Insira o valor do saque em R$: "))
        self.saldo -= saque

        return self.saldo



novoSaldo = ContaBancaria(1000, "Josefa Justina da Cruz")
print(f"O seu saldo inicial é R$: {novoSaldo.saldo}")
novoSaldo.depositar()
print(f"Após depósito, o seu novo saldo é de R$: {novoSaldo.saldo}")
novoSaldo.sacar()
print(f"Após realizar um saque, o seu novo saldo é de R$: {novoSaldo.saldo}")