class carro:
    
    def __init__(self, nome):
        self.nome = nome

    
    def acelerar(self):
        print (f'{self.nome} está acelerando')
       
        
    

corsa = carro(nome = 'corsa')
print(corsa.nome)
corsa.acelerar()


        