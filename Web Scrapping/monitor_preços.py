from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

class Automatic():
    def __init__(self, website):
        self.website = website

        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
    def __del__(self):
        self.driver.quit()
        
    def search_products(self, search_product, search_XPATH, products_title_XPATH, products_price_XPATH):
        self.driver.get(self.website)
        time.sleep(3)

        search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'.//{search_XPATH}')))
        for char in search_product:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.1, 0.2))
        
        search_box.send_keys(Keys.ENTER)

        products_title = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f'//{products_title_XPATH}')))

        products_price = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, f'//{products_price_XPATH}')))

        if self.website == 'https://www.mercadolivre.com.br':
            with open('mercadolivre_products.csv', 'w+', encoding='utf-8') as file:
                file.write('product; price\n')
                for product, price in zip(products_title[:20], products_price[:20]):
                    file.write(f'{product.text};{price.text}\n')
        elif self.website == 'https://www.amazon.com.br/':
            with open('amazon_products.csv', 'w+', encoding='utf-8') as file:
                file.write('product; price\n')
                for product, price in zip(products_title[:20], products_price[:20]):
                    file.write(f'{product.text};{price.text}\n')


    def analisar_precos(self, arquivo):
        df = pd.read_csv(arquivo, sep=';', encoding='utf-8', on_bad_lines='skip')

        df[' price'] = df[' price'].astype(str).str.strip()

        df[' price'] = df[' price'].str.replace('R$', '', regex=False)
        df[' price'] = df[' price'].str.replace('.', '', regex=False).str.replace(',', '.')

        df[' price'] = pd.to_numeric(df[' price'], errors='coerce')

        df = df.dropna(subset=[' price'])

        df = df[df[' price'] > 1000]

        if not df.empty:
            print(f"\n--- Relatório: {arquivo} ---")
            print(f"Média de Preço: R$ {df[' price'].mean():.2f}")
            print(f"Mediana: R$ {df[' price'].median():.2f}")
            print(f"Produto mais Caro: R$ {df[' price'].max():.2f}")
            print(f"Produto mais Barato: R$ {df[' price'].min():.2f}")
            print(f"Total de itens válidos: {len(df)}")
            print("-" * 30)
            df[' price'].plot(kind='hist', title=f'Distribuição de Preços - {arquivo}')
            plt.show()
        else:
            print(f"Aviso: O arquivo {arquivo} não contém dados numéricos válidos após a limpeza.")

product = input('Type wich product you want to search: ')

mercadolivre = Automatic('https://www.mercadolivre.com.br')
mercadolivre.search_products(product, 'input[@class="nav-search-input"]', 'a[@class="poly-component__title"]', 'span[@class="andes-money-amount__fraction"]')
mercadolivre.analisar_precos('mercadolivre_products.csv')
del mercadolivre

amazon = Automatic('https://www.amazon.com.br/')
amazon.search_products(product, 'input[@id="twotabsearchtextbox"]', 'h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]', 'span[@class="a-price-whole"]')
amazon.analisar_precos('amazon_products.csv')
del amazon


