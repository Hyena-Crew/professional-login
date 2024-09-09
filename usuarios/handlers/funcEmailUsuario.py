import smtplib
import random
from core.settings import DEBUG
from var_ignore import emailHyenaCrew, senhaAPPEmailHyenaCrew
from email.message import EmailMessage

def gerarNumeroRandomico():
     # Primeiro dígito é sempre 1
    primeiro_digito = '1'
        
    # Gerar os outros 5 dígitos aleatórios
    outros_digitos = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        
    # Combinar o primeiro dígito com os outros
    codigo = primeiro_digito + outros_digitos

    return codigo

# Configurar email, senha
def enviarCodigoVerificacaoEmail(UsuarioGmail, emailAdmin, senhaAdmin):
    EMAIL_ADDRESS = emailAdmin
    EMAIL_PASSWORD = senhaAdmin
    codigo_randomico = gerarNumeroRandomico()

    # Criar um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Seu codigo de verificação de usuário'
    msg['From'] = emailAdmin
    msg['To'] = UsuarioGmail
    conteudo_html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #121212; margin: 0; padding: 0;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: #1e1e1e; padding: 20px; border-radius: 10px;">
        <tr>
            <td align="center" style="padding: 10px 0;">
            <h2 style="color: #f1f1f1; font-size: 24px;">Código de Autenticação</h2>
            </td>
        </tr>
        <tr>
            <td align="center" style="padding: 20px; background-color: #2c2c2c; border-radius: 5px;">
            <p style="font-size: 18px; color: #e0e0e0; margin: 0;">Seu código de autenticação é:</p>
            <p style="font-size: 32px; font-weight: bold; color: #bb86fc; margin: 10px 0;">{codigo_randomico}</p>
            </td>
        </tr>
        <tr>
            <td align="center" style="padding: 20px 0;">
            <p style="font-size: 14px; color: #a8a8a8; margin: 0;">Por favor, insira este código no campo requisitado para continuar.</p>
            </td>
        </tr>
        </table>
    </body>
    </html>
    """
    msg.set_content(conteudo_html, subtype='html')

    # Enviar um e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return 

if DEBUG == True:
    usuarioGmail = "" #insira um email válido (gmail ou outlook)
    enviarCodigoVerificacaoEmail(usuarioGmail, emailHyenaCrew, senhaAPPEmailHyenaCrew)
    