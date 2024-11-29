from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_github_forgot_password():
    driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver está configurado corretamente
    driver.get("https://github.com/login")
    
    # Inserir e-mail falso
    email_box = driver.find_element(By.ID, "login_field")
    email_box.send_keys("email_falso@exemplo.com")
    
    # Inserir senha falsa
    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("senha_invalida")
    password_box.send_keys(Keys.RETURN)
    
    # Esperar a página carregar
    time.sleep(2)
    
    # Clicar em "Esqueci minha senha"
    forgot_password_link = driver.find_element(By.XPATH, '//a[text()="Forgot password?"]')
    forgot_password_link.click()
    
    # Esperar a página de redefinição carregar
    time.sleep(3)
    
    # Voltar para a página inicial ou sair
    driver.get("https://github.com")  # Simula "sair"
    time.sleep(2)
    
    driver.quit()
