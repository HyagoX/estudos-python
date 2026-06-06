import requests
from pprint import pprint


def request(url):


    response = requests.get(url)
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
        identif = element['id']
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

verify_town(uf_name='Araguaína')