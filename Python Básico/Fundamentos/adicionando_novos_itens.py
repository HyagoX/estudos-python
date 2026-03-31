usuarios = [
    { 'nome': 'Hyago', 'idade': 18 },
    { 'nome': 'Joana', 'idade': 17 }
] 

def novo_usuario(nome, idade):
        usuarios.append({'nome': nome, 'idade': idade})

novo_usuario('Thaynara', 18)
novo_usuario('Jussara', 37)

for usuario in usuarios:
        print(f'Nome: {usuario['nome']}, Idade: {usuario['idade']}')
        print('-------------------')