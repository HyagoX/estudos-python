import requests
from pprint import pprint
import streamlit as st
import pandas as pd


def fazer_request(url, params=None):
    response = requests.get(url, params=params)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print('Erro ao acessar API')
        response = None
    else:
        response = response.json()
    return response

def verify_name(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

    response = fazer_request(url)

    if not response:
        return None

    frequencia_dict = {}

    for element in response[0]['res']:
        periodo = element['periodo']
        frequencia = element['frequencia']
        frequencia_dict[periodo] = frequencia
    return frequencia_dict

def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/v2/censos/nomes/)')
    
    nome = st.text_input('Consulte o nome')
    if not nome:
        st.stop()

    dict_decadas = verify_name(nome)
    if not dict_decadas:
        st.warning(f'Nenhum dado encontrado para {nome}')
        st.stop()

    df = pd.DataFrame.from_dict(dict_decadas,orient='index')
    col1, col2 = st.columns([0.3, 0.7])

    with col1:
        st.write('Frequencia por década:')
        st.dataframe(df)
    with col2:
        st.write('Evolução por tempo')
        st.line_chart(df)


if __name__ == '__main__':
    main()