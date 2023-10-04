# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado “calcular_media” que retorna a média das notas do aluno.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0

notasA1 = [8.6, 9.8, 7.9]        
a1 = Aluno("João Paulo", notasA1)
mediaFinal = a1.calcular_media()
print(f"A média final do(a) aluno(a) {a1.nome} é {mediaFinal:.2f}")