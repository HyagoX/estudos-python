# Projeto: Cadastro de lista de compras
# Regras:
# - Ler e exibir a lista
# - Abrir a possibilidade de você adicionar um novo item nessa lista

# Meu código
with open('lista_compras.txt', 'a+', encoding='utf-8') as archive:
    while True:
        decision = input("Add new item? (y/n): ").lower()
        
        if decision == 'y': # Corrigido de 's' para 'y'
            new_item = input('Type new item name: ')
            archive.write(new_item + '\n') # SALVA NO ARQUIVO
            print(f"{new_item} added!")
            
        elif decision == 'n':
            print("\n--- Current Shopping List ---")
            archive.seek(0) # REBOBINA PARA LER DESDE O COMEÇO
            for item in archive:
                print(f"- {item.strip()}")
            break # Encerra o programa

# Código da Aula

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