# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 


    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    

p1 = Pessoa.criar_com_50_anos('Helena')
print(p1.nome, p1.idade)