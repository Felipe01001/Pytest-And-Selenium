from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_google_search_and_open_result():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    # Aceitar cookies, se necessário
    try:
        consent_button = driver.find_element(By.XPATH, '//button[text()="Aceitar tudo"]')
        consent_button.click()
    except:
        pass  # Se não houver botão de consentimento, continuar
    
    # Procurar pelo campo de busca
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    
    # Esperar pelos resultados
    time.sleep(3)
    
    # Clicar no primeiro link
    first_result = driver.find_element(By.XPATH, '(//h3)[1]')
    first_result.click()
    
    # Esperar para carregar o site
    time.sleep(5)
    
    driver.quit()