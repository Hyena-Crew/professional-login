# pip install twilio
from twilio.rest import Client
from core.settings import DEBUG
from var_ignore import account_sid_admin, tokenAdmin, telefoneAdminTwilio
import random

def gerarNumeroRandomico():
     # Primeiro dígito é sempre 1
    primeiro_digito = '1'
        
    # Gerar os outros 5 dígitos aleatórios
    outros_digitos = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        
    # Combinar o primeiro dígito com os outros
    codigo = primeiro_digito + outros_digitos

    return codigo

def enviarCodigoAutenticacaoSmsTwilio(account_sid_admin, auth_token, telefoneUsuario, telefoneAdminTwilio):
    client = Client(account_sid_admin, auth_token)
    codigoRandomico = gerarNumeroRandomico()

    message = client.messages.create(
        body=f"Seu código de confirmação é {codigoRandomico} para utilizar no login Hyena Crew.",
        from_= telefoneAdminTwilio,
        to= telefoneUsuario,
    )

    print(message.body)
    return codigoRandomico

def confirmarCodigoSms(codigoRandomicoConfirmacao, codigoUsuario):
    if codigoRandomicoConfirmacao == codigoUsuario:
        return True


if DEBUG == True:
    telefoneUsuario = ""
    codigoRandomicoConfirmacao = ""
    codigoUsuario = ""

    codigoRandomicoConfirmacao = enviarCodigoAutenticacaoSmsTwilio(account_sid_admin, tokenAdmin, telefoneUsuario, telefoneAdminTwilio)
    confirmacaoBooleano = confirmarCodigoSms()
    if confirmacaoBooleano:
        print("deu certo")
    else:
        print("usuario digitou numero errado")