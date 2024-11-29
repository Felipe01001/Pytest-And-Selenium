import pytest
import requests

# BASE URL da API ReceitaWS e chave da API
BASE_URL = "https://www.receitaws.com.br/v1/cnpj/"

# CHAVE DA API
API_KEY = "efd7dfcdf8f629707f496d9ffecdb1a4557e04408f4421f63b9090965265ef2d"  #(SÓ PODEM SER RODADOS 3 TESTES POR MINUTO)
                                # ^ CHAVE DA API ^ #

def test_consulta_cnpj_valido():
    # Testar consulta com um CNPJ válido
    cnpj = "00000000000191"  # Exemplo: CNPJ da Receita Federal
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(BASE_URL + cnpj, headers=headers)
    assert response.status_code == 200, "Erro ao acessar API de consulta de CNPJ"
    data = response.json()
    assert "nome" in data, "Campo 'nome' não encontrado na resposta"
    assert data["status"] == "OK", f"Status da resposta não esperado: {data['status']}"
    print(f"Nome da empresa: {data['nome']}")

def test_consulta_cnpj_invalido():
    # Testar consulta com um CNPJ inválido
    cnpj = "12345678000100"  # CNPJ fictício inválido
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(BASE_URL + cnpj, headers=headers)
    assert response.status_code == 200, "Erro ao acessar API de consulta de CNPJ"
    data = response.json()
    assert data["status"] == "ERROR", f"Status da resposta não esperado: {data['status']}"
    assert "message" in data, "Mensagem de erro não encontrada na resposta"
    print(f"Erro retornado: {data['message']}")

def test_consulta_cnpj_sem_autorizacao():
    cnpj = "00000000000191"
    response = requests.get(BASE_URL + cnpj)  # Sem cabeçalho de autorização
    assert response.status_code == 200, "Esperado código 200 para consultas sem autenticação"
    data = response.json()
    assert "erro" in data or "status" in data, "A resposta deveria conter um campo indicando erro ou limitação de acesso"




