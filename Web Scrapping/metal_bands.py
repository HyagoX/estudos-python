from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from urllib.parse import unquote

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=chrome_options)

print("Conectado ao Chrome real! Iniciando extração...")

band_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//tr[@class='odd']/td/a"))
)

links = [band.get_attribute('href') for band in band_list]
print(f'Encontrei {len(links)} links de bandas')

for link in links:
    try:
        driver.execute_script("window.open('');") # Abre aba em branco
        driver.switch_to.window(driver.window_handles[-1]) # Vai para a nova aba
        driver.get(link) # CARREGA O LINK DA BANDA
        
        time.sleep(random.uniform(2, 6)) 

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "discog")))
        
        elemento_ano = driver.find_element(By.XPATH, "(//table[contains(@class, 'discog')]//tr)[last()]/td[last()-1]")
        album_year = elemento_ano.get_attribute('innerText').strip()
        
        raw_name = link.split("/")[-2]
        band_name = unquote(raw_name).replace("_", " ")
        
        with open('bandas.csv', 'a+', encoding='utf-8') as file:
            file.write(f'{band_name};{album_year}\n')
            
    except Exception as e:
        print(f'❌ Erro ao processar a banda {link.split("/")[-2]}: {e}')
    
    try:
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[0])
    except:
        print("🚨 Sessão perdida!")
        break 
    
    time.sleep(random.uniform(1, 3))