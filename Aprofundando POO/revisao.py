# "Molde" Da pessoa
class Pessoa:
    def __init__(self, name):
# Atributos: Características da pessoa
        self.name = name

# Métodos: Coisas que a pessoa pode fazer
    def saudar(self):
        return f'Olá, meu nome é {self.name}'

# Instancia dessa pessoa, ou seja, um objeto
p1 = Pessoa('Hyago')
p2 = Pessoa('Joana')

print(p2.saudar())