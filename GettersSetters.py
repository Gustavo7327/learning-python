class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade  # Atributo protegido

    # Getter para idade
    def get_idade(self):
        return self._idade

    # Setter para idade, com validação
    def set_idade(self, idade):
        if idade >= 0:
            self._idade = idade
        else:
            raise ValueError("A idade não pode ser negativa")
        

p = Pessoa("João", 30)

# Usando o getter para acessar a idade
print(p.get_idade())  # Saída: 30

# Usando o setter para modificar a idade
p.set_idade(35)  # Altera a idade para 35
print(p.get_idade())  # Saída: 35

# Tentando definir uma idade inválida
p.set_idade(-5)  # Lança um erro: "A idade não pode ser negativa"



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self._idade = idade
        else:
            raise ValueError("A idade não pode ser negativa")
        
p = Pessoa("João", 30)

# Usando a propriedade para acessar e modificar diretamente
print(p.idade)  # Saída: 30
p.idade = 35    # Altera a idade para 35
print(p.idade)  # Saída: 35

# Tentando definir uma idade inválida
p.idade = -5  # Lança um erro: "A idade não pode ser negativa"