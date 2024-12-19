class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Público
        self.modelo = modelo  # Público
        self.ano = ano  # Público

    def acelerar(self):
        print("O carro está acelerando.")

# Criando um objeto e acessando atributos e métodos públicos
meu_carro = Carro("Honda", "Civic", 2023)
print(meu_carro.marca)  # Imprime "Honda"
meu_carro.acelerar()


class Animal:
    def __init__(self, nome):
        self._nome = nome  # Protegido

    def comer(self):
        print(f"{self._nome} está comendo.")

class Cachorro(Animal):
    def latir(self):
        print("Au au!")

# Criando um objeto e acessando o atributo protegido dentro da classe filha
meu_cachorro = Cachorro("Rex")
meu_cachorro.latir()  # Chama o método da classe filha
print(meu_cachorro._nome)  # Acessa o atributo protegido da classe pai



class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self.__saldo = saldo  # Privado

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

# Criando um objeto e tentando acessar o atributo privado diretamente
minha_conta = ContaBancaria("João", 1000)
# print(minha_conta.__saldo)  # Isso geraria um erro, pois o atributo é privado


class Teste:
    def __init__(self):
        self._teste = 0
        self.__teste2 = 12

    def __get_teste2():
        return 12

teste = Teste() 

print(teste._Teste__teste2)

