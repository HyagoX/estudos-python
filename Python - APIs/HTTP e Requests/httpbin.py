import requests

url = 'https://httpbin.org/post'

data = {
    'meus_dados': [1, 2, 3, 4],
    'pessoa': {
        'nome': 'Hyago',
        'aluno': True
    }
}

params = {
    'data_inicio': '2024-01-01',
    'data_fim': '2026-05-06'
}

response = requests.post(url, json=data, params=params)
response.raise_for_status()

print(response.json())


