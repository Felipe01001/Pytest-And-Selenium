import pytest
import requests

# Base URL da API
BASE_URL = "https://hp-api.onrender.com/api"

### TESTES PARAMETRIZADOS ###
@pytest.mark.parametrize("endpoint, expected_key", [
    ("/characters", "name"),
    ("/characters/students", "house"),
    ("/characters/staff", "actor"),
])
def test_parametrized_endpoints(endpoint, expected_key):
    """
    Testes parametrizados para múltiplos endpoints.
    """
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, f"Erro ao acessar API para {endpoint}"
    data = response.json()
    assert len(data) > 0, f"Nenhum dado retornado para o endpoint {endpoint}"
    assert expected_key in data[0], f"Chave esperada '{expected_key}' ausente em {endpoint}"
    print(f"Teste bem-sucedido: Endpoint {endpoint} retornou dados com a chave '{expected_key}'.")

@pytest.mark.parametrize("house, expected_count", [
    ("gryffindor", 10),  # Exemplo: Pelo menos 10 estudantes
    ("slytherin", 5),    # Exemplo: Pelo menos 5 estudantes
])
def test_parametrized_houses(house, expected_count):
    """
    Testa a recuperação de estudantes para casas específicas.
    """
    endpoint = f"/characters/house/{house}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, f"Erro ao acessar API para a casa {house}"
    data = response.json()
    assert len(data) >= expected_count, f"Esperava pelo menos {expected_count} estudantes na casa {house}"
    print(f"Teste bem-sucedido: {len(data)} estudantes retornados para a casa {house}.")

### TESTES DE VALIDAÇÃO ###
def test_get_characters():
    """
    Testa a recuperação da lista de personagens.
    """
    endpoint = "/characters"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum personagem foi retornado"

    expected_keys = {"name", "house", "patronus", "actor"}
    assert expected_keys.issubset(data[0].keys()), f"Chaves ausentes no JSON: {expected_keys - data[0].keys()}"
    print(f"Teste bem-sucedido: {len(data)} personagens retornados.")

def test_get_students():
    """
    Testa a recuperação de todos os estudantes.
    """
    endpoint = "/characters/students"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum estudante foi retornado"
    print(f"Teste bem-sucedido: {len(data)} estudantes retornados.")

def test_get_staff():
    """
    Testa a recuperação de todos os membros da staff.
    """
    endpoint = "/characters/staff"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum membro da staff foi retornado"
    print(f"Teste bem-sucedido: {len(data)} membros da staff retornados.")

def test_search_character_by_name():
    """
    Testa a busca de um personagem por nome.
    """
    endpoint = "/characters"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    character_name = "Harry Potter"
    character = next((char for char in data if char["name"] == character_name), None)
    assert character is not None, f"Personagem {character_name} não encontrado"
    print(f"Teste bem-sucedido: Personagem '{character['name']}' encontrado.")

### TESTES DE ERRO ###
def test_invalid_endpoint():
    """
    Testa um endpoint inexistente.
    """
    endpoint = "/invalid_endpoint"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "A API deveria retornar 404 para endpoint inválido"
    print("Teste bem-sucedido: Endpoint inválido retornou o erro esperado.")

def test_invalid_house():
    """
    Testa a recuperação de estudantes de uma casa inexistente.
    """
    endpoint = "/characters/house/unknownhouse"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "A API deveria retornar 200 para casa inexistente"
    data = response.json()
    assert data == [], "A API deveria retornar uma lista vazia para casa inexistente"
    print("Teste bem-sucedido: Casa inexistente retornou lista vazia, conforme esperado.")
