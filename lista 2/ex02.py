# Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def mostrarDetalhes(self):

        detalhes = """É um livro fantástico autobiográfico sobre o feriado de ano novo que mudou a vida do autor. \n
        Após um trágico acidente, Marcelo acorda tretrapégico e terá que lidar com todas as mudanças que essa situação implica \n
        para um jovem universitário que sempre curtiu a vida intensamente. Nessa jornada, ele vai amadurecer e aprender\n
        que está vivo e lúcido é o gás que qualquer um precisa para reescrever sua tragetória."""

        return print(detalhes)
    
    def mostrarTitulo(self):
        return self.titulo
        
    def mostrarAutor(self):
        return self.autor
    
l1 = Livro("Feliz ano velho", "Marcelo Rubens Paiva")
print("Título: ", l1.mostrarTitulo())
print("Autor: ", l1.mostrarAutor())
print("-" * 30) # adicionando um separador entre o início dos detalhes 
l1.mostrarDetalhes()