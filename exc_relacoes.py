class Fabricante:
    def __init__(self, nome):
        self.nome = nome




class Carro:
    def __init__(self, nome):
        self.nome_carro = nome

    def inserir_motor(self, nome_motor):
        self.nome_motor.append(Motor(nome_motor))




class Motor:
    def __init__(self, nome):
        self.nome = nome


    def exibir_motor(self, nome_motor):
        print(nome_motor)

motor = Motor('V8')
motor.nome_motor()