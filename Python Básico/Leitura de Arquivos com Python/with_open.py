lista = ['Hyago\n', 'Joana\n', 'Heloyse\n']

with open('lista.txt', 'w') as arquivo:
    for name in lista:
        arquivo.write(name)
    for linha in arquivo:
        print(linha.strip())