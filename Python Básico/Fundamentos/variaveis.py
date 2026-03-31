# Nomeie suas váriaveis de forma a deixa-las o auto-explicativas. Nomes de Variaveis jamais começam com um número
# No Python, temos várias convenções para váriaveis, entre elas temos que:
# 1. Salvar nome de váriaveis sempre em letras minúsculas
# 2. Utilizar o padrão snake_case, para separar palavras nos nomes das váriaveis, utilizando o _ no lugar do espaço
# 3. Tente colocar o nome das suas váriaveis em inglês por padrão

name = 'Hyago'; # Valor String
full_name = name + ' Jose Maria'
age = '18'; # Valor inteiro(int)
saved_money = 1500.50 # Valor de ponto flutuante(float)
adm = False; # Valor booleano

print(name)
print(full_name)
print(age)
print(saved_money)
print(adm)

# Se definirmos o valor de uma variavel de uma forma, e depois nas linhas abaixo definirmos outra variável com o mesmo nome, porem com o valor diferente, o valor dessa váriavel abaixo da nova definição vai ser substituido pelo novo valor nas linhas abaixo
# EXEMPLO:

variable = 'Joana'
print(variable)

variable = 'Heloyse'
print(variable)