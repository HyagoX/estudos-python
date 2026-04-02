import pandas as pd

# 1. Carrega os dados (com o ajuste que vimos antes)
df = pd.read_csv('vendas_tech.csv', encoding='utf-8')

# 2. Deixa os nomes das lojas bonitos (para garantir que 'Belo Horizonte' seja encontrado)
df['Loja'] = df['Loja'].str.title()

# --- O DESAFIO ---

# PASSO A: Filtrar apenas as vendas de BH
vendas_bh = df.loc[df['Loja'] == 'Belo Horizonte']

# PASSO B: Agrupar por 'Produto' e somar a coluna 'Qtd'
# O reset_index() serve para ele continuar parecendo uma tabela bonitinha no final
ranking_produtos = vendas_bh.groupby('Produto')['Qtd'].sum().reset_index()

# PASSO C: Ordenar do maior para o menor (ascending=False)
ranking_produtos = ranking_produtos.sort_values(by='Qtd', ascending=False)

# PASSO D: Mostrar o primeirão da lista
print("O produto mais vendido em BH foi:")
print(ranking_produtos.iloc[0])