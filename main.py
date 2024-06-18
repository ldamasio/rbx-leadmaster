from decouple import config
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By

TARGET_USERNAME = config('TARGET_USERNAME')

USERNAME = config('USERNAME')
PASSWORD = config('PASSWORD')

PATH = config('PATH')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument('--executable_path='+PATH)

driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(2)

# Fazer o login
tempo_aleatorio = random.randint(2, 10)
tempo_aleatorio_alt = random.randint(2, 10)
tempo_aleatorio_alternative = random.randint(2, 10)
time.sleep(tempo_aleatorio)
username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username.send_keys(USERNAME)
time.sleep(tempo_aleatorio_alt)
password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.send_keys(PASSWORD)
time.sleep(tempo_aleatorio_alternative)
login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)                                                                        

# Recusar os alertas de notificações
try:
  wait = WebDriverWait(driver, 10)  # Set a 10-second timeout
  button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
  button.click()
except:
  print("Button 'Not Now' not found or not clickable within 10 seconds")
time.sleep(3)

# Alvo do scraping (substitua por "@ldamasio.rbx")
target_username = TARGET_USERNAME
profile_url = f"https://www.instagram.com/{target_username}/followers"
driver.get(profile_url)
time.sleep(2)

# Localizar número total de seguidores
try:
    followers_count = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"mount_0_0_w6\"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span")))
    print (followers_count.get_attribute("outerHTML"))
except:
    print("Não foi possível localizar o número de seguidores")

time.sleep(3)

# Localizar botão de seguidores
try:
  wait = WebDriverWait(driver, 10)  # Set a 10-second timeout
  button = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "follower")))
  button.click()
except:
  print("Button 'follower' not found or not clickable within 10 seconds")
time.sleep(3)

try:
    # Localizar janela pop-up
    followers_popup = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
except:
    print("Não foi possível localizar a janela pop-up")

time.sleep(2)

# Rola para baixo até o final
# last_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)
total = 330

for i in range(total):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
    time.sleep(8)

time.sleep(2)

# Salvar todo o código da div
try:
    codigo_fonte = followers_popup.get_attribute("outerHTML")
    with open("data/codigo_fonte_007.html", "w", encoding="utf-8") as file:
        file.write(codigo_fonte)
except:
    print("Não foi possível salvar")

# while True:
    
#     time.sleep(5)  # Aguarde o carregamento
    
#     new_height = driver.execute_script("return arguments[0].scrollHeight", followers_popup)
#     if new_height == last_height:
#         break
#     last_height = new_height

time.sleep(2)
# follower_links = [followers_popup.get_attribute('href') for followers_popup in followers_popup]

time.sleep(2)
#Salva os links em um arquivo de texto
# with open('seguidores.txt', 'w') as file:
#     for link in follower_links:
#         file.write(link + '\n')

# body > div.x1n2onr6.xzkaem6 > div:nth-child(2) > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6
# /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]

# pop_up_window = WebDriverWait( 
#     driver, 2).until(EC.element_to_be_clickable( 
#         (By.XPATH, "//div[@class='isgrP']"))) 


# Wait for the followers popup to load
# followers_popup = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//div[@class="isgrP"]'))
# )

# pop_up_window = WebDriverWait( 
#     driver, 10).until(EC.element_to_be_clickable( 
#         (By.XPATH, "//div[@class='isgrP']"))) 
  
# Scroll till Followers list is there 
# while True: 
#     driver.execute_script( 
#         'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',  
#       pop_up_window) 
#     time.sleep(1) 

time.sleep(5000)

# # Extrai os links dos seguidores
# followers = driver.find_elements_by_xpath('//a[contains(@href, "/followers/")]')
# follower_links = [follower.get_attribute('href') for follower in followers]

# Salva os links em um arquivo de texto
# with open('seguidores.txt', 'w') as file:
#     for link in follower_links:
#         file.write(link + '\n')

# Encerra o navegador
driver.quit()