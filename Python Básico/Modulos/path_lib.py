# Importa a biblioteca inteira com todas as funcionalidades
import pathlib
# Importa uma unica parte da biblioteca
from pathlib import Path

# Salva o arquivo ou pasta dentro de uma variavel
test_folder = pathlib.Path('teste')

# Verifica se o arquivo existe. False = nao existe, True = existe
print(test_folder.exists())

if test_folder.exists() == False:
    test_folder.mkdir()
    print('Pasta criada com sucesso')
else:
    test_folder.rmdir()
    print('Pasta deletada com sucesso')

# eu = pathlib.Path('path_lib.py')
# if eu.exists() == True:
#     # Deleta um arquivo
#     eu.unlink()

pasta = pathlib.Path('teste')

