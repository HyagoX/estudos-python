# r = read
# w = write (escreve por cima do que já existe no arquivo, substituindo-o)
# a = append (escreve adicionando ao final do conteudo que já existe, sem substitui-lo)
# x = create

# arquivo = open("lista.txt", "r")
# conteudo = arquivo.read()

# print(conteudo)

arquivo = open('lista.txt', 'r')
linhas = arquivo.readlines()

i = 0
for linha in linhas:
    print(f'Linha {i}: {linha.strip()}')
    i+=1