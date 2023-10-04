# Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método chamado “calcular_area” que retorna a área do retângulo.

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        area = self.base * self.altura

        return area
r1 = Retangulo(8,5)
print("A área do retângulo é: ", r1.calcularArea())   
