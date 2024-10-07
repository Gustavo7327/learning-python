class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando alto.")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")

def plano_voo(obj):
    obj.voar()

# Demonstração de polimorfismo
plano_voo(Pardal())
plano_voo(Avestruz())