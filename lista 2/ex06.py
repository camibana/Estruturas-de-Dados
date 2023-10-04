# Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.valorTotal = 0

    def calcular_total(self):
        self.valorTotal = self.preco * self.quantidade

        return self.valorTotal
    
p1 = Produto("Borracha", 1.40, 8)
p1.calcular_total()
print(f"O estoque do produto {p1.nome} possui {p1.quantidade} unidades, totalizando o valor de R$: {p1.valorTotal:.2f}.")