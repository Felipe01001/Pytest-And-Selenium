import pytest
import requests

# Base URL da API
BASE_URL = "https://hp-api.onrender.com/api"

def test_get_characters():
    # Testa a recuperação da lista de personagens
    endpoint = "/characters"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum personagem foi retornado"

    # Verifica se as chaves esperadas estão presentes no primeiro personagem
    expected_keys = {"name", "house", "patronus", "actor"}
    assert expected_keys.issubset(data[0].keys()), f"Chaves ausentes no JSON: {expected_keys - data[0].keys()}"

    print(f"Personagens retornados: {len(data)}")


def test_get_students():
    # Testa a recuperação de todos os estudantes
    endpoint = "/characters/students"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum estudante foi retornado"
    print(f"Estudantes retornados: {len(data)}")

def test_get_staff():
    # Testa a recuperação de todos os membros da staff
    endpoint = "/characters/staff"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum membro da staff foi retornado"
    print(f"Membros da staff retornados: {len(data)}")

def test_get_gryffindor_students():
    # Testa a recuperação dos estudantes da casa Gryffindor
    endpoint = "/characters/house/gryffindor"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhum estudante da Gryffindor foi retornado"
    print(f"Estudantes da Gryffindor retornados: {len(data)}")

def test_search_character_by_name():
    # Testa a busca de um personagem por nome
    endpoint = "/characters"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    character_name = "Harry Potter"
    character = next((char for char in data if char["name"] == character_name), None)
    assert character is not None, f"Personagem {character_name} não encontrado"
    print(f"Personagem encontrado: {character['name']}")

def test_invalid_endpoint():
    # Testa um endpoint inexistente
    endpoint = "/invalid_endpoint"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "A API deveria retornar 404 para endpoint inválido"
    print("Endpoint inválido retornou o erro esperado.")

def test_invalid_house():
    # Testa a recuperação de estudantes de uma casa inexistente
    endpoint = "/characters/house/unknownhouse"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "A API deveria retornar 200 para casa inexistente"
    
    data = response.json()
    assert data == [], "A API deveria retornar uma lista vazia para casa inexistente"
    print("Casa inexistente retornou lista vazia, conforme esperado.")


