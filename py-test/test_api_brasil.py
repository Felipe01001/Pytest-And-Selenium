import pytest
import requests

# URL base da BrasilAPI
BASE_URL = "https://brasilapi.com.br/api"

def test_get_cep():
    # Testa a busca por um CEP
    endpoint = "/cep/v1/01001000"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["cep"].replace("-", "") == "01001000", f"CEP incorreto: {data['cep']}"
    assert data["state"] == "SP", f"Estado incorreto: {data['state']}"
    print("CEP encontrado com sucesso:", data["cep"])

def test_get_bank():
    # Testa a busca por informações de um banco
    endpoint = "/banks/v1/001"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert str(data["code"]) == "1", f"Código do banco incorreto: {data['code']}"
    assert "BRASIL" in data["name"].upper(), f"Nome do banco incorreto: {data['name']}"
    print("Banco encontrado:", data["name"])


def test_fipe_brands():
    # Testa a obtenção de marcas de veículos na tabela FIPE
    endpoint = "/fipe/marcas/v1/carros"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert len(data) > 0, "Nenhuma marca de carro retornada"
    print(f"Marcas de veículos retornadas: {len(data)}")

def test_cnpj():
    # Testa a consulta de informações de um CNPJ
    endpoint = "/cnpj/v1/19131243000197"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert data["cnpj"].replace(".", "").replace("/", "").replace("-", "") == "19131243000197", f"CNPJ incorreto: {data['cnpj']}"
    assert data["razao_social"] == "OPEN KNOWLEDGE BRASIL", f"Razão social incorreta: {data['razao_social']}"
    print("Informações do CNPJ obtidas com sucesso:", data["razao_social"])


def test_invalid_cep():
    # Testa busca por um CEP inválido
    endpoint = "/cep/v1/00000000"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 404, "A API deveria retornar erro (404) para CEP inválido"
    data = response.json()
    assert "message" in data, "A resposta de erro deveria conter uma mensagem explicativa"
    print("Erro esperado retornado para CEP inválido:", data["message"])


def test_invalid_cnpj():
    # Testa consulta de um CNPJ inválido
    endpoint = "/cnpj/v1/123"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 400, "A API deveria retornar erro para CNPJ inválido"
    data = response.json()
    assert "message" in data, "Resposta de erro deveria conter mensagem explicativa"
    print("Erro esperado retornado para CNPJ inválido:", data["message"])

def test_get_cep():
    endpoint = "/cep/v1/01001000"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    
    # Verifica a presença de chaves
    expected_keys = {"cep", "state", "city", "neighborhood", "street"}
    assert expected_keys.issubset(data.keys()), f"Chaves esperadas não estão presentes: {expected_keys - data.keys()}"
    
    # Verifica valores específicos
    assert data["cep"].replace("-", "") == "01001000", f"CEP incorreto: {data['cep']}"
    assert data["state"] == "SP", f"Estado incorreto: {data['state']}"
    print("CEP encontrado com sucesso:", data["cep"])


@pytest.mark.parametrize("cep, estado_esperado", [
    ("01001000", "SP"),
    ("30140071", "MG"),
    ("20040002", "RJ")
])
def test_parametrized_cep(cep, estado_esperado):
    endpoint = f"/cep/v1/{cep}"
    response = requests.get(BASE_URL + endpoint)
    assert response.status_code == 200, f"Erro ao acessar API para CEP {cep}"
    data = response.json()
    assert data["state"] == estado_esperado, f"Estado incorreto para {cep}: {data['state']}"
    print(f"CEP {cep} encontrado com sucesso no estado {estado_esperado}")
