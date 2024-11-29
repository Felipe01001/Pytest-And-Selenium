import pytest
import requests

# URL base da BrasilAPI
BASE_URL = "https://brasilapi.com.br/api"

# ---------------------- TESTES PARAMETRIZADOS ----------------------

@pytest.mark.parametrize("cep, estado_esperado", [
    ("01001000", "SP"),
    ("30140071", "MG"),
    ("20040002", "RJ")
])
def test_parametrized_cep(cep, estado_esperado):
    """Teste parametrizado: Valida CEPs e seus respectivos estados."""
    endpoint = f"/cep/v1/{cep}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, f"Erro ao acessar API para CEP {cep}"
    data = response.json()
    assert data["state"] == estado_esperado, f"Estado incorreto para {cep}: {data['state']}"
    print(f"Rota: {BASE_URL + endpoint} | Objetivo concluído: CEP {cep} no estado {estado_esperado}")

# ---------------------- TESTES DE VALIDAÇÃO ----------------------

def test_get_cep():
    """Teste básico: Recupera informações de um CEP válido."""
    endpoint = "/cep/v1/01001000"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    expected_keys = {"cep", "state", "city", "neighborhood", "street"}
    assert expected_keys.issubset(data.keys()), f"Chaves esperadas não estão presentes: {expected_keys - data.keys()}"
    assert data["cep"].replace("-", "") == "01001000", f"CEP incorreto: {data['cep']}"
    assert data["state"] == "SP", f"Estado incorreto: {data['state']}"
    print(f"Rota: {BASE_URL + endpoint} | Objetivo concluído: Informações do CEP {data['cep']} verificadas com sucesso.")

def test_get_bank():
    """Teste básico: Busca informações de um banco válido."""
    endpoint = "/banks/v1/001"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert str(data["code"]) == "1", f"Código do banco incorreto: {data['code']}"
    assert "BRASIL" in data["name"].upper(), f"Nome do banco incorreto: {data['name']}"
    print(f"Rota: {BASE_URL + endpoint} | Objetivo concluído: Banco {data['name']} encontrado.")

# ---------------------- TESTES DE ERRO ----------------------

def test_invalid_cep():
    """Teste de erro: Verifica comportamento para CEP inválido."""
    endpoint = "/cep/v1/00000000"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "A API deveria retornar erro (404) para CEP inválido"
    data = response.json()
    assert "message" in data, "A resposta de erro deveria conter uma mensagem explicativa"
    print(f"Rota: {BASE_URL + endpoint} | Objetivo concluído: Erro esperado retornado para CEP inválido.")


def test_invalid_cnpj():
    """Teste de erro: Verifica comportamento para CNPJ inválido."""
    endpoint = "/cnpj/v1/123"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 400, "A API deveria retornar erro para CNPJ inválido"
    data = response.json()
    assert "message" in data, "Resposta de erro deveria conter mensagem explicativa"
    print(f"Rota: {BASE_URL + endpoint} | Objetivo concluído: Erro esperado retornado para CNPJ inválido.")
