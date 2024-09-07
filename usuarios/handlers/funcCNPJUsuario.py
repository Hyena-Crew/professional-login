from core.settings import DEBUG

import requests
import json

def consulta_cnpj(cnpj):
    # Manter apenas os dígitos
    cnpj = ''.join([char for char in cnpj if char.isdigit()])
    
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token": "XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj": cnpj, "plugin": "RF"}

    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)
    
    if resp['status'] == "OK":
        telefone = ''.join([char for char in resp['telefone'] if char.isdigit()])

        DadosUsuario = []
        DadosUsuario.append(resp['nome'])
        DadosUsuario.append(resp['email'])
        DadosUsuario.append(telefone)

        return DadosUsuario
    else:
        if resp['message'] == "not in cache":
            DadosUsuario = "CNPJ não está presente na base de dados da Receita Federal"
        else:
            DadosUsuario = "Ocorreu um erro, por favor entre em contato com os desenvolvedores"
        
        return DadosUsuario

def validar_cnpj(cnpj: str):
    # Remover caracteres não numéricos
    cnpj = ''.join([char for char in cnpj if char.isdigit()])
    
    # Verificar se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return "CNPJ precisa ter 14 digitos"
    
    # Função para calcular o dígito verificador
    def calcular_digito(cnpj, peso):
        soma = 0
        for i in range(len(peso)):
            soma += int(cnpj[i]) * peso[i]
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    # Pesos para cálculo dos dígitos verificadores
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Verificar o primeiro dígito
    primeiro_digito = calcular_digito(cnpj[:12], peso1)
    if primeiro_digito != int(cnpj[12]):
        return "CNPJ inválido"
    
    # Verificar o segundo dígito
    segundo_digito = calcular_digito(cnpj[:13], peso2)
    if segundo_digito != int(cnpj[13]):
        return "CNPJ inválido"
    
    return True    

# Futuramente trocar oq esta abaixo e usar o "Pytest"
if DEBUG == True:
    #cnpj = "98495404000106" # Vai mas não possui na base de dados da receita federal
    cnpj = "27865757000102" # Funciona corretamente(GLOBO)
    
    if validar_cnpj(cnpj):
        dadosUsuarioCNPJ = consulta_cnpj(cnpj)
        print(dadosUsuarioCNPJ)
   







