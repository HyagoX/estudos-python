
lista = ['Hyago\n', 'Joana\n', 'Heloyse\n']

arquivo = open("lista.txt", 'a') # Com o 'w', caso o arquivo não exista, ele vai criar um arquivo. Caso ele já exista, ele vai ser sobrescrito, apagando o conteudo anterior.
for nome in lista:
    arquivo.write(nome)

arquivo.close()