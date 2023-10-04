# Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método chamado “detalhes” que retorna uma string com as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano

    def detalhes(self):
        mensagem = f"Os delathes do carro são: Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}."

        return print(mensagem)
    
c1 = Carro("Toyota", "Yaris", 2022)
c1.detalhes()
    
