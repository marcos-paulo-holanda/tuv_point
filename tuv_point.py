from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")  # Define um tamanho de janela para forçar a renderização

driver = webdriver.Chrome(service=Service('./chromedriver.exe'), options=options)
driver.get("https://asp4.softtrade.com.br/RHOnline_ELO_TUV/login.xhtml")

# Aguarde a página carregar
time.sleep(3)

# Encontre os elementos de login
username_input = driver.find_element(By.ID, "frmLogin:txtLogin")
password_input = driver.find_element(By.ID, "frmLogin:txtVarSen")
login_button = driver.find_element(By.ID, "frmLogin:entrar")

# Insira as credenciais de login
username_input.send_keys("608350")
password_input.send_keys("gogo123")

# Clique no botão de login
login_button.click()

# Esperar o menu "Ponto" aparecer
menu_ponto = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Ponto']"))
)

# Usar JavaScript para clicar no menu "Ponto"
driver.execute_script("arguments[0].click();", menu_ponto)

# Esperar o elemento "Marcação Ponto" aparecer
marcacao_ponto = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Marcação Ponto']"))
)

# Usar JavaScript para clicar no elemento "Marcação Ponto"
driver.execute_script("arguments[0].click();", marcacao_ponto)

# Insere ponto a ser marcado
now = datetime.now()
current_time = now.strftime("%H:%M")

time.sleep(3)
input_marcacao = driver.find_element(By.XPATH, "//*[@id='formMarcPto:cdDatMarcFun_input']")
input_marcacao.send_keys(current_time)

time.sleep(3)
# Usar JavaScript para clicar no botão de confirmação
btn_confirmar = driver.find_element(By.XPATH, "//*[@id='formMarcPto:btnGerMarcPto']/span[1]")
driver.execute_script("arguments[0].click();", btn_confirmar)

time.sleep(5)

# Finalize o WebDriver
driver.quit()
