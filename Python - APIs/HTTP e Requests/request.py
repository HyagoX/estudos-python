import requests

url = 'https://www.google.com?param1=valor1' #?acesso=admin&filtro=janeiro <-- isto é um parametro da requisição

response = requests.get(url, timeout=10)
response.raise_for_status()

print(response)
# Response[200] = Retornou a página corretamente


with open('pagina_google.html', 'w') as archive:
    archive.write(response.text)