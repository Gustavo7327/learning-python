class Casa:
    #definindo construtor
    def __init__(self, num_quartos, cor, tamanho_m2):
        self.num_quartos = num_quartos
        self.cor = cor
        self.tamanhom2 = tamanho_m2
    
    # mostrando informações da casa
    def mostrar_info(self):
        print(f"A casa tem {self.num_quartos}")
        print(f"A casa foi pintada de {self.cor}")
        print(f"A casa tem {self.tamanhom2} metros quadrados")