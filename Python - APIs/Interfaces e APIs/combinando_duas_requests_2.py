import requests
from pprint import pprint
import numpy as np

def fazer_request(url, params=None):
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        response = None
        print('Erro durante a chamada da API')
    else:
        response = response.json()
    return response

def lista_estados():
    params = {
        'view': 'nivelado'
    }

    response = fazer_request('https://servicodados.ibge.gov.br/api/v1/localidades/estados', params=params)
    
    estados_dict = {}

    for item in response:
        element_id = item['UF-id']
        element_nome = item['UF-nome']
        estados_dict[element_id] = element_nome
    return estados_dict



def get_proporcao(nome):
    params = {
        'groupBy': 'localidade',
        'view': 'nivelado'
    }

    response = fazer_request(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}', params)

    proporcao_dict = {}

    for item in response:
        local_id = int(item['localidade'])
        proporção = item['res'][0]['proporcao']
        proporcao_dict[local_id] = proporção
    return proporcao_dict

def media(nome):
    proporcao = get_proporcao(nome)
    dados = []
    for i in proporcao.values():
        dados.append(i)
    np_dados = np.array(dados)
    media = np.mean(np_dados)
    return media

def main(nome):
    print(f'Frequencia do nome {nome} por estado (por 100.000 habitantes):')
    estados_dict = lista_estados()
    proporcao = get_proporcao(nome)
    for id_estado, nome_estado in estados_dict.items():
        try:
            frequencia_estado = proporcao[id_estado]
            print(f'-> {nome_estado} = {frequencia_estado}: ')
        except KeyError as e:
            print(f'-> Ninguem chamado {nome} em {nome_estado}')
            continue
    total = media(nome)
    print(f'-> Média total no brasil: {total:.2f}')


if __name__ == '__main__':
    main('Joana')