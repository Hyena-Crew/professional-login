from core.settings import DEBUG

def validar_cpf(cpf: str) -> bool:
    # Remove caracteres que não são dígitos
    cpf = ''.join([char for char in cpf if char.isdigit()])

    # Verifica se o CPF tem 11 dígitos ou se todos os números são iguais
    if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verifica se os dígitos calculados são iguais aos dígitos fornecidos
    return cpf[-2:] == f'{digito1}{digito2}'

# Futuramente trocar oq esta abaixo e usar o "Pytest"
if DEBUG == True:
    # Exemplo de uso:
    cpf = "529.982.247-25"
    if validar_cpf(cpf):
        print("CPF válido")
    else:
        print("CPF inválido")

