# Problema: Esquecer de difinir atributos básicos de uma classe, no exemplo abaixo, nao definimos o valor 'price' do produto 2 (p2), caso chamemos a função resumir do produto 2, o código retornará um erro, pois o price desse produto não existe. Ou seja, quando criamos uma instancia de uma classe, precisamos dar a ele os atributos mais básicos dessa classe, para isso usamos os contrutores
# class Product:
#     def resumir(self):
#         print(f'{self.name} custa R$ {self.price}')

# p1 = Product()
# p1.name = 'Arroz'
# p1.price = 25


# p2 = Product()
# p2.name = 'Feijao'

# p1.resumir()
# p2.resumir()


# Construtor:

class Product:
    def __init__(self, # sempre comece com o self, para referir-se ao objeto atual armazenado na memória
                 name,
                 price 
                 #demais atributos da classe
                 ):
        self.name = name
        self.price = price
    
    def resumir(self):
        print(f'{self.name} custa {self.price}')

# E então, no momento da criação daquela instancia da classe, logo de inicio já iremos colocar os atributos dessa instancia
p1 = Product('Arroz', 18)
p1.resumir()