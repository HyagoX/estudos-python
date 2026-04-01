class Conta:
# O python nao tem naturalmente o conceito de atributos protegido, publico e privado, com o Python, nós trabalhamos com convenções
    def __init__(self):
# Utilizamos um underline antes do nome do atributo para demonstrar que ele é privado, e dois underlines para mostrar que ele é protegido. No entanto, esses dados ainda podem ser acessados normalmente. 
# Saldo foi transformado em um atributo Privado
        self._saldo = 0

# Aqui, nós usamos um método chamado saldo, O property, serve para transformar essa função em uma propriedade, ou seja, transforando ele em um atributo, então nao é necessario acessar diretamente o self._saldo, por que aquele atributo acima, é privado
    @property
    def saldo(self):
        return self._saldo

    def deposito(self, valor):
        self._saldo += float(valor)

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= float(valor)
            return True
        else:
            return False

c1 = Conta()

c1.deposito(200)

print(c1.saldo)
qt = float(input('Qual o valor do saque?'))
if c1.sacar(qt) == True:
    print(f'Saque realizado. Saldo atual {c1.saldo}')
else:
    print('Saldo insuficiente')