class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def oi(self):
        return f'Oi meu nome é {self.nome}, e tenho {self.idade} anos'

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def exibir_salario(self):
        return f'O meu salário é de {self.salario} reais'

f1 = Funcionario('pedro', 28, 3000)
f1.oi()
f1.exibir_salario()

print(f'{f1.oi()} {f1.exibir_salario()}')

