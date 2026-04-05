from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from urllib.parse import unquote

# 1. Configura o Selenium para conectar no Chrome que já está aberto
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 2. Inicia o driver normal (Não é o UC) conectando na porta 9222
driver = webdriver.Chrome(options=chrome_options)

# A partir daqui, o código é o mesmo! Ele vai controlar a janela que já está aberta.
print("Conectado ao Chrome real! Iniciando extração...")

# Já estamos na página de busca, então não precisamos dar o driver.get() inicial
# Vamos direto capturar a lista:
band_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//tr[@class='odd']/td/a"))
)

links = [band.get_attribute('href') for band in band_list]
print(f'Encontrei {len(links)} links de bandas')

for link in links:
    try:
        # --- ESSAS LINHAS SÃO O QUE FAZEM A PÁGINA ABRIR ---
        driver.execute_script("window.open('');") # Abre aba em branco
        driver.switch_to.window(driver.window_handles[-1]) # Vai para a nova aba
        driver.get(link) # CARREGA O LINK DA BANDA
        
        # Espera humana para o Cloudflare não te barrar de novo
        time.sleep(random.uniform(2, 6)) 
        # --------------------------------------------------

        # Espera a tabela de discografia carregar
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "discog")))
        
        # Pega o último TD da última TR (Ano)
        elemento_ano = driver.find_element(By.XPATH, "(//table[contains(@class, 'discog')]//tr)[last()]/td[last()-1]")
        album_year = elemento_ano.get_attribute('innerText').strip()
        
        # Traduz o nome da banda (resolve o :Nihus:)
        raw_name = link.split("/")[-2]
        band_name = unquote(raw_name).replace("_", " ")
        
        with open('bandas.csv', 'a+', encoding='utf-8') as file:
            file.write(f'{band_name};{album_year}\n')
            
    except Exception as e:
        # Se der erro, tentamos identificar o motivo (pode ser o ban ou banda sem disco)
        print(f'❌ Erro ao processar a banda {link.split("/")[-2]}: {e}')
    
    # Fecha a aba da banda e volta para a lista de busca
    try:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[0])
    except:
        print("🚨 Sessão perdida!")
        break 
    
    # Descanso entre bandas
    time.sleep(random.uniform(1, 3))