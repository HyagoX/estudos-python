from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import pyautogui

class Automation():
    def __init__(self, website):
        self.website = website
        
        # 1. CONFIGURAÇÃO DO MODO INVISÍVEL (HEADLESS)
        chrome_options = Options()
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        chrome_options.add_argument("--headless=new") # O 'new' é importante para as versões novas do Chrome
        chrome_options.add_argument("--disable-gpu")  # Recomendado para Windows em modo headless
        chrome_options.add_argument("--no-sandbox")   # Evita erros de permissão no Windows
        chrome_options.add_argument("--window-size=1920,1080") # Define um tamanho de tela pro robô não se perder
        
        # 2. INICIA O DRIVER UMA VEZ SÓ (Melhor performance)
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def find_dolar_price(self, search_XPATH, dolar_value_XPATH):
        # 3. SEMPRE reseta para a URL inicial a cada ciclo
        self.driver.get(self.website)
        time.sleep(3) 

        try:
            search_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//{search_XPATH}')))
            search_box.clear()

            for char in 'Dolar Hoje':
                search_box.send_keys(char)
                time.sleep(random.uniform(0.1, 0.2))

            search_box.send_keys(Keys.ENTER)
            
            # 4. Aumentei a espera - sites em headless às vezes demoram mais pra renderizar
            time.sleep(5) 

            dolar_value = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//{dolar_value_XPATH}')))
            clean_value = dolar_value.text.replace(',', '.')

            with open('dolar_value.csv', 'a', encoding='utf-8') as file:
                file.write(f'{time.ctime()};{clean_value}\n')
            
            print(f"📊 Registro feito: R$ {clean_value} às {time.ctime()}")

        except Exception as e:
            print(f"⚠️ Erro no ciclo: {e}")

# --- EXECUÇÃO ---

bot = Automation('https://www.bing.com')
print("🚀 Robô rodando em segundo plano. Pressione Ctrl+C para parar.")

try:
    while True:
        bot.find_dolar_price('textarea[@id="sb_form_q"]', 'div[@class="b_focusTextSmall curr_totxt"]')
        print("💤 Dormindo por 10 minutos...")
        time.sleep(600) 
except KeyboardInterrupt:
    print("\n🛑 Desligando robô...")
    pyautogui.press('shift')
    bot.driver.quit()