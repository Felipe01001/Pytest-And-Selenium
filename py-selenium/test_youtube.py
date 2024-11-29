from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_youtube_search_and_play():
    driver = webdriver.Chrome()  # Configure o driver de acordo com o seu navegador
    driver.get("https://www.youtube.com")
    
    # Esperar pela página carregar
    time.sleep(3)
    
    # Aceitar cookies, se necessário
    try:
        consent_button = driver.find_element(By.XPATH, '//button[text()="Concordo"]')
        consent_button.click()
    except:
        pass  # Se não houver botão de consentimento, continuar
    
    # Procurar pelo campo de busca
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("Python Selenium tutorial")
    search_box.send_keys(Keys.RETURN)
    
    # Esperar pelos resultados
    time.sleep(3)
    
    # Clicar no primeiro vídeo
    video = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
    video.click()
    
    # Esperar para ver o vídeo iniciar
    time.sleep(10)
    
    driver.quit()