# OITO COMPONENTES BÁSICOS
# Tudo o que o Selenium faz é enviar comandos ao navegador para executar alguma ação ou enviar solicitações de informações. A maior parte do que você fará com o Selenium é uma combinação desses comandos básicos.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# 1. Iniciando a sessão
# O principal argumento exclusivo para iniciar um driver local inclui informações sobre como iniciar o serviço de driver necessário na máquina local.
driver = webdriver.Chrome()

# 2. Execute uma ação no navegador
# Neste exemplo, estamos navegando para uma página da web.
driver.get('https://www.bing.com/')

# 3. Solicitar informações do navegador
# Existem vários tipos de informações sobre o navegador que você pode solicitar, incluindo identificadores de janela, tamanho/posição do navegador, cookies, alertas, etc. Neste caso, estamos apenas salvando o título da página em uma Váriavel
title = driver.title
print(title)

# 4. Estabelecer uma estratégia de espera
# Sincronizar o código com o estado atual do navegador é um dos maiores desafios do Selenium, e fazer isso bem é um tópico avançado.
# Basicamente, você precisa garantir que o elemento esteja na página antes de tentar localizá-lo e que esteja em um estado interativo antes de tentar interagir com ele.
# Uma espera implícita raramente é a melhor solução, mas é a mais fácil de demonstrar, então vamos usá-la como um exemplo provisório.
driver.implicitly_wait(1)

# 5. Encontre um elemento
# A maioria dos comandos na maioria das sessões do Selenium está relacionada a elementos, e você não pode interagir com um elemento sem primeiro encontrá-lo.
search_box = driver.find_element(by=By.CLASS_NAME, value='sb_form_q')

# 6. Tome medidas em relação ao elemento
# Existem apenas algumas ações que você pode realizar em um elemento , mas você as usará com frequência.
def slow_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

slow_typing(search_box, 'Dolar Hoje')
search_box.send_keys(Keys.ENTER)

dolar_price = driver.find_element(By.XPATH, '//div[@class="b_focusTextSmall curr_totxt"]')
driver.implicitly_wait(0.5)

with open("dolar.txt", "w") as arquivo:
    arquivo.write(f"{time.ctime()}: R${dolar_price.text}")