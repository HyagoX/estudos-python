import os

# Adiciona uma nova pasta (diretorio)
os.mkdir('nomedoarquivo')

# Utilizado para apagar uma pasta
os.rmdir('nomedoarquivo')

# Mostra onde está o local do projeto
print(os.getcwd())

# Renomeia um arquivo
# os.rename('script.py', 'import_os.py')

# Retorna um array com todos os arquivos dentro de uma pasta. Se utilizarmos '.' mostra os arquivos dentro da própria pasta do script
print(os.listdir('.'))

