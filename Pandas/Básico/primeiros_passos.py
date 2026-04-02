# A biblioteca pandas, é a principal biblioteca usada para análise de dados atualmente. A base de tudo sao duas estruturas principais que precisam ser entendidas:

# Séries: é como se fosse uma única coluna de dados de uma tabela. É uma lista de dados de uma dimensão
# DataFrame: É a tabela inteira. É um conjunto de séries coladas umas nas outras. Tem linhas e colunas

import pandas as pd

catálogo = {
    'Banda': ['Darkthrone', 'Mayhem', 'Burzum', 'Bathory'],
    'Subgenero': ['Black-Metal', 'Black-Metal', 'Black-Metal', 'Black/Viking Metal'],
    'Pais': ['Noruega', 'Noruega', 'Noruega', 'Suécia'],
    'Ano': [1986, 1984, 1991, 1992]
}

df_pandas = pd.DataFrame(catálogo)

print(df_pandas)

# Essa é a ferramenta que faz toda etada de ETL = Extract, Transform e Load
# Quando se faz um projeto com uma base de dados, precisamos extrair os dados dessa base(Extract). Então transformar esses dados para poder serem utilizados da melhor forma(Transformar), e por fim carregar esses dados(Load). Porem no pandas, alem de carregar esses dados, é possivel com essa biblioteca fazer as análises dentro dela