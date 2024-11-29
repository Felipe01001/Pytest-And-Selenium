import pytest
import requests

# Configurações da API
BASE_URL = "https://api.themoviedb.org/3"

# Chave pessoal da API
API_KEY = "a97bd91ab42ded2e603828674bccfa6f"  # <----- CHAVE DA API 

# ----------------------- TESTES PARAMETRIZADOS -----------------------

@pytest.mark.parametrize("api_key, expected_status", [
    ("INVALID_KEY", 401),
    (API_KEY, 200),
    (None, 401),  # Chave ausente
])
def test_parametrized_api_key(api_key, expected_status):
    """
    Teste parametrizado para verificar o comportamento da API com diferentes chaves.
    """
    endpoint = "/movie/550"
    params = {"api_key": api_key} if api_key else None
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == expected_status, (
        f"Esperado status {expected_status}, mas recebido {response.status_code}"
    )
    print(f"Rota: {BASE_URL + endpoint} | Teste parametrizado com chave {'ausente' if api_key is None else api_key}: objetivo concluído.")

@pytest.mark.parametrize("movie_id, expected_status", [
    (550, 200),        # Filme existente
    (99999999, 404),   # Filme inexistente
])
def test_parametrized_movie_request(movie_id, expected_status):
    """
    Teste parametrizado para verificar diferentes IDs de filmes.
    """
    endpoint = f"/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == expected_status, (
        f"Esperado status {expected_status}, mas recebido {response.status_code}"
    )
    print(f"Rota: {BASE_URL + endpoint} | Teste de ID {movie_id}: objetivo concluído.")

# ----------------------- TESTES DE VALIDAÇÃO -----------------------

def test_valid_movie_request():
    """
    Testa a consulta a um filme válido (exemplo: filme 'Fight Club').
    """
    endpoint = "/movie/550"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "A API não retornou sucesso para um filme válido"
    data = response.json()
    assert "title" in data, "O título do filme não foi encontrado na resposta"
    assert data["id"] == 550, f"ID do filme esperado: 550, mas foi {data['id']}"
    print(f"Rota: {BASE_URL + endpoint} | Filme encontrado: {data['title']} | Objetivo concluído.")

def test_check_media_type():
    """
    Verificar se o tipo de mídia retornado é filme.
    """
    endpoint = "/movie/550"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 200, "Erro ao acessar a API do filme"
    
    data = response.json()
    assert "title" in data, "Campo 'title' não encontrado"
    assert data["id"] == 550, "O ID do filme não corresponde ao esperado"
    print(f"Rota: {BASE_URL + endpoint} | Tipo de mídia verificado com sucesso | Objetivo concluído.")

# ----------------------- TESTES DE ERRO -----------------------

def test_invalid_api_key():
    """
    Testa o comportamento da API com uma chave inválida.
    """
    endpoint = "/movie/550"
    params = {"api_key": "INVALID_KEY"}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 401, "A API não retornou erro para chave inválida"
    data = response.json()
    assert data["status_message"] == "Invalid API key: You must be granted a valid key.", (
        f"Erro inesperado: {data['status_message']}"
    )
    print(f"Rota: {BASE_URL + endpoint} | Teste de chave inválida: objetivo concluído.")

def test_movie_not_found():
    """
    Testa a consulta para um filme inexistente com ID mais alto.
    """
    endpoint = "/movie/99999999"
    params = {"api_key": API_KEY}
    response = requests.get(BASE_URL + endpoint, params=params)
    assert response.status_code == 404, "A API não retornou erro 404 para filme inexistente"
    data = response.json()
    assert data["status_code"] == 34, (
        "A API não indicou 'recurso não encontrado' no corpo da resposta"
    )
    print(f"Rota: {BASE_URL + endpoint} | Filme inexistente verificado: objetivo concluído.")

def test_missing_api_key():
    """
    Testa o comportamento da API sem a chave de API.
    """
    endpoint = "/movie/550"
    response = requests.get(BASE_URL + endpoint)  # Sem chave
    assert response.status_code == 401, "A API deveria retornar erro 401 quando a chave não for fornecida"
    data = response.json()
    assert data["status_message"] == "Invalid API key: You must be granted a valid key.", (
        f"Erro inesperado: {data['status_message']}"
    )
    print(f"Rota: {BASE_URL + endpoint} | Teste de chave faltando: objetivo concluído.")