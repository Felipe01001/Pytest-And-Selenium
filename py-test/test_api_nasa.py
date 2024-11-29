import pytest
import requests

# BASE URL da NASA API e chave da API
BASE_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "MEY3OkcNh5Yfi4tTQVT3gsfnYcz8THvzpUqCh9t7"  # Chave pública de exemplo

def test_apod():
    # Teste básico: buscar a Astronomy Picture of the Day (APOD)
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "title" in data, "Título não encontrado na resposta"
    assert "url" in data, "URL da imagem não encontrada"
    print(f"Título: {data['title']} | URL da Imagem: {data['url']}")

def test_apod_date():
    # Testar busca pela data de uma imagem específica
    params = {"api_key": API_KEY, "date": "2024-11-25"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["date"] == "2024-11-25", f"A data retornada é incorreta: {data['date']}"
    print(f"Imagem do dia ({data['date']}): {data['title']}")


def test_apod_copyright():
    # Testa se a resposta contém o campo de copyright
    params = {"api_key": "DEMO_KEY"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, f"Erro ao acessar API. Status Code: {response.status_code}"
    data = response.json()
    assert "copyright" in data, "Campo 'copyright' não encontrado na resposta"
    print(f"Copyright: {data['copyright']}")


def test_apod_media_type():
    # Verificar o tipo de mídia (imagem ou vídeo)
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "media_type" in data, "Tipo de mídia não encontrado"
    assert data["media_type"] in ["image", "video"], f"Tipo de mídia inválido: {data['media_type']}"
    print(f"Tipo de mídia: {data['media_type']}")

def test_apod_description():
    # Verificar a descrição da imagem do dia
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "explanation" in data, "Descrição (explicação) não encontrada"
    assert len(data["explanation"]) > 10, "A explicação é muito curta"
    print(f"Descrição da imagem do dia:\n{data['explanation']}")


def test_apod_future_date():
    params = {"api_key": API_KEY, "date": "2050-01-01"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 400, "A API deveria retornar 400 para datas futuras"
    print("Erro retornado para data futura, conforme esperado.")

def test_apod_missing_api_key():
    response = requests.get(BASE_URL)
    assert response.status_code == 403, "A API deveria retornar 403 quando a chave está ausente"
    print("Erro retornado para requisição sem chave de API, conforme esperado.")


def test_apod_invalid_api_key():
    params = {"api_key": "INVALID_KEY"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 403, "A API deveria retornar 403 para chave inválida"
    print("Erro retornado para chave inválida, conforme esperado.")

