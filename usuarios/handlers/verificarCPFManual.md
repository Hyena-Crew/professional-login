# Como Saber se um CPF é valido:
Para determinar se um CPF é válido, é necessário seguir algumas regras específicas definidas pelo algoritmo do CPF. Abaixo estão as principais especificações:

1. Formato do CPF:
- O CPF é composto por 11 dígitos numéricos.
- Embora o formato mais comum seja "XXX.XXX.XXX-XX", durante a validação é importante considerar apenas os números, ignorando pontos e traços.

2. Proibição de números repetidos:
- Um CPF válido não pode ser composto por uma sequência de números repetidos (ex: "111.111.111-11", "222.222.222-22", etc.). Essas sequências são consideradas inválidas, embora estejam no formato correto.

3. Dígitos verificadores:
- Os dois últimos dígitos do CPF (dígitos verificadores) são calculados a partir dos nove primeiros dígitos. O processo de cálculo envolve um algoritmo específico que garante a validade desses dígitos.

4. Cálculo do primeiro dígito verificador:
- Pegue os 9 primeiros dígitos do CPF e multiplique cada um deles por um número sequencial decrescente de 10 a 2.
Some os resultados dessas multiplicações.
- O resultado dessa soma deve ser multiplicado por 10 e, em seguida, tirado o módulo 11 ((soma * 10) % 11).
Se o resultado for 10 ou maior, o dígito verificador será 0. Caso contrário, o resultado da operação será o primeiro dígito verificador.

5. Cálculo do segundo dígito verificador:
- Agora, considere os 9 primeiros dígitos do CPF mais o primeiro dígito verificador calculado.
- Multiplique-os por números sequenciais decrescentes de 11 a 2.
- Some os resultados dessas multiplicações.
- O resultado dessa soma é multiplicado por 10 e tirado o módulo 11 ((soma * 10) % 11).
- Se o resultado for 10 ou maior, o segundo dígito verificador será 0. Caso contrário, o resultado da operação será o segundo dígito verificador.

6. Comparação final:
- Os dois dígitos verificadores calculados devem corresponder aos dois últimos dígitos do CPF informado. Se ambos forem iguais, o CPF é considerado válido.