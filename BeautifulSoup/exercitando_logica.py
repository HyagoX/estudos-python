from bs4 import BeautifulSoup

with open('site.html', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

# Você só precisa passar a string 'lxml' aqui. 
# O BeautifulSoup já procura a biblioteca no seu PC sozinho!
ex = BeautifulSoup(conteudo, 'lxml')
tags = ex.find_all(class_='Lista')

for tag in tags:
    print(tag.text)