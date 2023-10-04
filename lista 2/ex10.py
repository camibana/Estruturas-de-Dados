# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”. Implemente um método chamado “aumentar_salario” que recebe um valor percentual de aumento e atualiza o salário do funcionário.

class Funcionario:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self):
        aumento = self.salario * 0.03  #percentual de aumento = 3% 
        self.salario += aumento

        return self.salario
    
f1 = Funcionario("Paulo Henrique Rodrigues", 5000, "Representante Comercial")
print(f"Nome do(a) Funcionário(a): {f1.nome}")
print(f"Cargo: {f1.cargo}")
print(f"Salário inicial R$ {f1.salario}")
f1.aumentar_salario()
print(f"Salário final R$ {f1.salario}")
    

