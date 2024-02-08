class camera:

    def __init__(self, nome, filmando= False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f'{self.nome} já está filmando')
            return
        
        print(f'{self.nome} está filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando is True:
            print('Não é permitido fotografar enquanto filma')

        else:
            print(f'{self.nome} está fotografando')

    def parar_de_filmar(self):
        if self.filmando is False:
            print(f'{self.nome} não está filmando')

        print(f'{self.nome} parou de filmar')
        self.filmando = False




c1 = camera('Canon')
c2 = camera('Sony')
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_de_filmar()
c2.fotografar()
print(c2.__dict__)