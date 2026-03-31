# Classes
# - Atributos (nome, email, senha) (Seriam as características de uma classe)
# - Métodos (postar, excluir post, editar post) (Seriam as ações que uma classe pode fazer)

# Criando uma classe
class Product:
    def resume(self):
        print(f'''
Nome: {self.name}; 
Preço: {self.price}
-------------------------------
''')


# Instanciando uma classe
p1 = Product()

# Adicionando atributos em um objeto(instancia de uma classe)
p1.name = 'Camiseta do Blade and Bath'
p1.price = 20

p2 = Product()
p2.name = 'Moletom do Xasthur'
p2.price = 40


p1.resume()
p2.resume()