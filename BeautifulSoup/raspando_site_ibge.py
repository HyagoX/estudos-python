import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def acessar_site():
    states = [
  "ac", "al", "ap", "am", "ba", "ce", "df", "es",
  "go", "ma", "mt", "ms", "mg", "pa", "pb", "pr",
  "pe", "pi", "rj", "rn", "rs", "ro", "rr", "sc",
  "sp", "se", "to"
];
    
    for state in states:
        try:
            url = f'https://www.ibge.gov.br/cidades-e-estados/{state}.html'
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()    
        except:
            print('Erro ao carregar url')
            exit(0)

        soup = BeautifulSoup(response.text, 'html.parser')
        desc = soup.find_all(class_='ind-label')
        value = soup.find_all(class_='ind-value')
        with open('dados.csv', 'a+', encoding='utf-8') as arquivo:
            arquivo.write(f'{state}\n')
            for descrição, valor in zip(desc, value):
                year = valor.find('small')
                if year:
                    year.extract()
                    arquivo.write(f'{descrição.text}; {valor.text}\n')

acessar_site()