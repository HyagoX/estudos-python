# Listas

lista = ['arroz', 'feijao', 'carne']
lista2 = [10, 5, 3, 4, 198]
lista3 = ['Hyago', 9, 'feijao', True]
# Composto por um índice, o indice do primeiro item na primeira lista(arroz) é 0, dentro daquele lista. Se quisermos imprimir esse item, nós podemos da um comando para printar a lista, mas logo em frente, colocamos a chave do item que queremos printar no terminal(Lembre-se, todas as listas tem seus itens começando nao pelo 1, mas pelo 0)
print(lista[0])
lista[0] = 'bosta'
print(lista[0])

# Tuplas (ou coleções)
# Coleções (ou tuplas) são listas que NAO podem ser modificadas
# Geralmente usada quando temos uma lista de coisas que nao queremos modificar, por exemplo uma lista de configurações
tupla = ('Hyago', 'Joana', 'Heloyse')
# tupla[1] = 'Perfeição'
# A linha de cima nós retornará um erro no terminal: ''tuple' object does not support item assignment'

# Dicionários
pessoa = {
    'nome': 'Hyago',
    'idade': 18,
    'pais': 'Brasil'
}

print(pessoa['nome'])