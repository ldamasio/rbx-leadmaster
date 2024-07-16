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
  wait = WebDriverWait(driver, 10)
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

total = 330

for i in range(total):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
    time.sleep(8)

time.sleep(2)

try:
    codigo_fonte = followers_popup.get_attribute("outerHTML")
    with open("data/" + TARGET_USERNAME, "w", encoding="utf-8") as file:
        file.write(codigo_fonte)
except:
    print("Não foi possível salvar")

# Encerra o navegador
driver.quit()
