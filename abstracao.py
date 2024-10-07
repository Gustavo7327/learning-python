from abc import ABC, abstractmethod

# classe abstrata
class Veiculo(ABC):
    def __init__(self, cor, numero_rodas):
        self.cor = cor
        self.numero_rodas = numero_rodas

    @abstractmethod
    def mover(self):
        pass

# classe que herda de veiculo
class Carro(Veiculo):
    def __init__(self, cor, numero_rodas, numero_portas):
        super().__init__(cor, numero_rodas)
        self.numero_portas = numero_portas

    def mover(self):
        print("O carro está se movendo.")

#classe que herda de veiculo
class Moto(Veiculo):
    def __init__(self, cor, numero_rodas):
        super().__init__(cor, numero_rodas)

    def mover(self):
        print("A moto está se movendo.")

# Criando objetos
meu_carro = Carro("prata", 4, 4)
minha_moto = Moto("preta", 2)

# Usando os métodos
meu_carro.mover()
minha_moto.mover()