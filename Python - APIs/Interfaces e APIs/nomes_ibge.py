import requests


def verify_name(nome, sexo='Nones', localidade='None'):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

    params = {
        'sexo': sexo,
        'localidade': localidade
    }

    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no Request. Erro: {e}')
        return
    else:
        response=response.json()

    if not response:
        print('Nenhum resultado encontrado para esses parametros')
        return
    
    print(response[0]['res'])

verify_name('Hyago', 'F')