import pytest
import requests

# BASE URL da API ReceitaWS e chave da API
BASE_URL = "https://www.receitaws.com.br/v1/cnpj/"

# CHAVE DA API
API_KEY = "efd7dfcdf8f629707f496d9ffecdb1a4557e04408f4421f63b9090965265ef2d"  # Limite: 3 testes/minuto

                    # ---------------------- TESTES DE VALIDAÇÃO ----------------------

def test_consulta_cnpj_valido():
    """
    Testar consulta com um CNPJ válido.
    """
    cnpj = "00000000000191"  # Exemplo: CNPJ da Receita Federal
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(BASE_URL + cnpj, headers=headers)
    assert response.status_code == 200, "Erro ao acessar API de consulta de CNPJ"
    data = response.json()
    assert "nome" in data, "Campo 'nome' não encontrado na resposta"
    assert data["status"] == "OK", f"Status da resposta não esperado: {data['status']}"
    print(f"Nome da empresa: {data['nome']}")


                      # ---------------------- TESTES PARAMETRIZADOS ----------------------



@pytest.mark.parametrize("cnpj, expected_status, expected_key", [
    ("00000000000191", "OK", "nome"),      # CNPJ válido
    ("00000000000000", "ERROR", "message")   # CNPJ inexistente
])
def test_consulta_cnpj_parametrizado(cnpj, expected_status, expected_key):
    """
    Testar múltiplos casos de consulta de CNPJ em um único teste parametrizado.
    """
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(BASE_URL + cnpj, headers=headers)
    assert response.status_code == 200, f"Erro ao acessar API para CNPJ {cnpj}"
    data = response.json()
    assert data["status"] == expected_status, f"Status inesperado para {cnpj}: {data['status']}"
    assert expected_key in data, f"Chave '{expected_key}' não encontrada na resposta para {cnpj}"
    print(f"Teste bem-sucedido para CNPJ {cnpj}: {data}")
