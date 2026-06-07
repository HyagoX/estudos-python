import requests
from pprint import pprint


def request(url, params=None):


    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no Request. Erro: {e}')
        return
    else:
        response=response.json()
        return response

def verify_state(nome='None', sexo='Nones', localidade='None'):
    response = request('https://servicodados.ibge.gov.br/api/v1/localidades/estados')

    estados_dict = {}

    for i, element in enumerate(response):
        nome = element['nome']
        identif = int(element['id'])
        estados_dict[identif] = nome
    return(estados_dict)
    

def verify_town(uf_id='None', uf_name='None'):

    response = request('https://servicodados.ibge.gov.br/api/v1/localidades/municipios')

    town = ''

    for i, element in enumerate(response):
        if element['nome'] == uf_name or element['id'] == uf_id:
            town = f'{element["nome"]} - {element["id"]} - {element["microrregiao"]["nome"]} - {element["regiao-imediata"]["nome"]}'            
            return(town)
    if town == '':
        print('Cidade nao existe ou nome está incorreto')

def verify_name(nome, sexo='Nones', localidade=None):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

    params = {
        'sexo': sexo,
        'localidade': localidade
    }
    response = request(url, params)

    if not response:
        print('Nenhum resultado encontrado para esses parametros')
        return

    estados = verify_state()

    estado = 'Não informado!'

    if localidade != None:
        estado = estados[localidade]

    frequencias = response[0]["res"]

    if response[0]['sexo'] == None:
        response[0]['sexo'] = 'Ambos'

    print(f'''
        Nome: {response[0]['nome']}
        Sexo: {response[0]['sexo']}
        Estado: {estado}
    ''')

    total = 0

    for item in frequencias:
        total += item['frequencia']
        print(f"Período: {item['periodo']} - Frequência: {item['frequencia']}")
    print(f'Total: {total}')

verify_name('Joana', localidade=32)