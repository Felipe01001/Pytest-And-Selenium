import pytest
import requests

# Configurações da API
BASE_URL = "https://api.themoviedb.org/3"

# Chave pessoal da API para obter os testes
API_KEY = "a97bd91ab42ded2e603828674bccfa6f"  # <----- CHAVE DA API 

def test_invalid_api_key():
    # Testa o comportamento da API com uma chave inválida
    endpoint = "/movie/550"
    params = {"api_key": "INVALID_KEY"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 401, "A API não retornou erro para chave inválida"
    data = response.json()
    assert data["status_message"] == "Invalid API key: You must be granted a valid key.", f"Erro inesperado: {data['status_message']}"
    print("Teste de chave inválida bem-sucedido")

def test_valid_movie_request():
    # Testa a consulta a um filme válido (exemplo: filme 'Fight Club')
    endpoint = "/movie/550"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "A API não retornou sucesso para um filme válido"
    data = response.json()
    assert "title" in data, "O título do filme não foi encontrado na resposta"
    assert data["id"] == 550, f"ID do filme esperado: 550, mas foi {data['id']}"
    print(f"Filme encontrado: {data['title']}")

def test_movie_not_found():
    # Testa a consulta para um filme inexistente com ID mais alto
    endpoint = "/movie/99999999"  # ID de filme fictício mais alto
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    
    # Verifica se o código de status é 404 ou 200
    assert response.status_code in [404, 200], "A API retornou um status inesperado para filme inexistente"

    # Depurar o conteúdo do corpo da resposta
    data = response.json()
    print(data)  # Adicionar para entender o que está sendo retornado

    # Validar se o recurso não foi encontrado
    if response.status_code == 200:
        assert "status_code" in data and data["status_code"] == 34, (
            "A API não indicou 'recurso não encontrado' no corpo da resposta"
        )




def test_missing_api_key():
    # Testa o comportamento da API sem a chave de API
    endpoint = "/movie/550"
    response = requests.get(BASE_URL + endpoint)  # Sem chave
    assert response.status_code == 401, "A API deveria retornar erro 401 quando a chave não for fornecida"
    data = response.json()
    assert data["status_message"] == "Invalid API key: You must be granted a valid key.", f"Erro inesperado: {data['status_message']}"
    print("Teste de chave faltando bem-sucedido")

def test_check_media_type():
    # Verificar se o tipo de mídia retornado é filme
    endpoint = "/movie/550"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar a API do filme"
    
    data = response.json()
    # Validar um campo existente no JSON retornado
    assert "title" in data, "Campo 'title' não encontrado"
    assert data["id"] == 550, "O ID do filme não corresponde ao esperado"

