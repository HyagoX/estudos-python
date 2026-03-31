# Projeto: Cadastro de clientes
# Regras:
# - Classe pessoa(nome e idade)
# - Classe cliente (E-mail e LTV - LifeTime Value)
# Cadastre 2 clientes diferentes em uma lista
# Exiba na lista de todos os clientes cadastrados
# Extra: Exiba a soma dos LTV de todos os clientes

class Pessoa():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f'Hi, my name is {self.name} and i am {self.age} years old'

class Cliente(Pessoa):
    def __init__(self, name, age, email, ltv):
        super().__init__(name, age)
        self.email = email
        self.ltv = ltv

    def introduce(self):
        base_quote = super().introduce()
        return f'{base_quote}. My LifeTime Value is about ${self.ltv}'    

lista_clientes = []
lista_clientes.append(Cliente('Rogerio', 18, 'rogerio@gmail.com', 120))
lista_clientes.append(Cliente('Julia', 20, 'julinha123@gmail.com', 575))

def sum_ltv(clients_list):
    return sum(client.ltv for client in clients_list)

print(f'The sum of all LTVs is: {sum_ltv(lista_clientes)}')

print(lista_clientes[0].introduce())