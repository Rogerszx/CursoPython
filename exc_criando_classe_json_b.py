class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibir_nome(self):
        print(f'{self.nome}')

    def exibir_sobrenome(self):
        print(f'{self.sobrenome}')


p1 = Pessoa('Roger', 'Gonçalves')
p1.exibir_nome()
p1.exibir_sobrenome()
