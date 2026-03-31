# with open('lista.txt', 'r') as lista:
#     for item in lista:
#         print(f'- {item.strip()}')
    
# print('-----------')

# with open('lista.txt', 'a') as lista:
#     novo_item = input('Digite o novo item: ')
#     if novo_item != '':
#         lista.write(f'{novo_item}\n')
#         print('Item adicionado com sucesso')
#     else:
#         print('Você nao digitou nada')

class List:
    def __init__(self, name):
        self._filename = f'{name}.txt'
        
    def get_list(self):
        list = []
        with open(self._filename, 'r') as file:
            for iten in file:
                list.append(iten.strip())
        return list
    
    def set_new_item(self, new_item):
        with open(self._filename, 'a') as file:
            if new_item != '':
                file.write(f'{new_item}\n')
                print('Item adicionado')
            else:
                print('Voce nao escreveu nada')
lista = List('lista')

def init_project(lista):
    while True:
        decisao = input('''Add new item? (y/n): ''')
        if decisao == 'y':
            novo_item = input('Type new item name: ')
            lista.set_new_item(novo_item)
        elif decisao == 'n':
            for item in lista.get_list():
                print(f'- {item}')
            break
        else:
            print('Please, type "y" (yes) or "n"(no): ')

init_project(lista)