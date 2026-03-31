# Lista com Strings
lista = [
    'Hyago',
    'Joana'
]

# Lista com dicionários
usuarios = [
    {'nome': 'Hyago', 'idade': 18, 'id': 1},
    {'nome': 'Joana', 'idade': 17, 'id': 2}
]

for usuario in usuarios:
    print(f'Nome: {usuario['nome']} , Idade: {usuario['idade']}, ID: {usuario['id']}')


posts = [
    {'title': 'Titulo do primeiro post', 'author': 'Hyago'},
    {'title': 'Titulo Boladao', 'author': 'Joana'},
    {'title': 'Aprenda abc', 'author': 'Heloyse'}
]

for post in posts:
    print(f'Título do Post: {post['title']}')
    print(f'Autor: {post['author']}')
    print('---------------')
