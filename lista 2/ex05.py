# Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        mensagem = f"""  Olá, {self.nome} , você é uma pessoa especial para todos em sua vida. Você tem \n
                    {self.idade} e já realizou muitos sonhos, desejamos que você continue feliz!"""
        
        return print(mensagem)
    
p1 = Pessoa("Carla Fernanda", 32)
p1.falar()

