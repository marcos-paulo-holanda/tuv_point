from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

options = webdriver.ChromeOptions()
options.add_argument("--lang=pt-BR")
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=options)
driver.get("https://asp4.softtrade.com.br/RHOnline_ELO_TUV/login.xhtml")

# Aguarde a página carregar (você pode ajustar o tempo de espera conforme necessário)
time.sleep(3)

# Encontre os elementos de login (ajuste os seletores conforme necessário)
username_input = driver.find_element(By.ID, "frmLogin:txtLogin")
password_input = driver.find_element(By.ID, "frmLogin:txtVarSen")
login_button = driver.find_element(By.ID, "frmLogin:entrar")

# Insira as credenciais de login (substitua 'your_username' e 'your_password')
username_input.send_keys("608350")
password_input.send_keys("gogo123")

# Clique no botão de login
login_button.click()

menu_ponto = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Ponto']"))
)

# Cria uma ação para mover o mouse sobre o menu "Ponto"
actions = ActionChains(driver)
actions.move_to_element(menu_ponto).perform()

# Clica no elemento "Marcação Ponto"
marcacao_ponto = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[text()='Marcação Ponto']"))
)
marcacao_ponto.click()

# Insere ponto a ser marcado
now = datetime.now()
current_time = now.strftime("%H:%M")
driver.find_element(By.XPATH, "//*[@id=\"formMarcPto:cdDatMarcFun_input\"]").send_keys(current_time)

time.sleep(3)
driver.find_element(By.XPATH, "//button[.//span[@class='ui-button-text ui-c']]").click()
driver.find_element(By.XPATH, "//*[@id=\"formMarcPto:btnGerMarcPto\"]/span[1]").click()
time.sleep(5)

# Finalize o WebDriver
driver.quit()
