# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado “calcular_area” que retorna a área do círculo.
import math as mt

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        area = mt.pi * (self.raio**2)

        return area
    
c1 = Circulo(3)
area = c1.calcular_area()
print(f'A área é:{area:.2f}')