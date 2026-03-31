class Product:
    def __init__(self, name, price):
        self._name = name # Isto é uma convenção, para que quando queremos PROTEGER um atributo, colocamos um underline antes do nome dessa variável
        self.price = price
    
# Getter: Usado para acessar o valor de um atributo por uma função
    def get_name(self):
        return self._name
    
# Setter: Usado para adicionar ou modificar o valor de uma tributo atraves de uma função
    def set_name(self, new_name):
        self._name = new_name

p1 = Product('Arroz', 18)

# É possivel acessar atributo das classes e altera-los, como no exemplo abaixo, no entanto, nem sempre queremos trocar valores dos nossos atributos, por isso, usamos o ENCAPSULAMENTO
# Atributo Público: É um atributo que é acessível públicamente, tanto pra acessar, quanto pra modificar informações
# Atributo Protegido: Não podemos acessar ele sem um auxiliar, nem modificar seu valor
# Atributo Privado: Ele está dentro do objeto, mas não é possivel acessar externamente. É um atributo utilizado internamente, como dados bancarios por exemplo
p1.name = 'Macarrão'
# print(p1.name)

# Usando getter
print(p1.get_name())

# Usando setter
p1.set_name('Desgraça')
print(p1.get_name())

p1._name = 'Lixo'
print(p1._name)