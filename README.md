# Sobre o projeto
Este projeto é um sistema de cadastro e login de usuários incluindo redefinição de senha e autenticação em duas etapas via SMS, sendo esse um modelo para projetos futuros.

## Integrantes
- Breno Ferreira Gomes;
- David Castanheira de Souza;
- Rafael Nascimento de Souza

## Indice
- [Funcionalidades](#funcionalidades)
- [Ferramentas e tecnologias](#ferramentas-e-tecnologias)
- [Gerenciamento](#gerenciamento)
- [Versionamento](#versionamento)

## Funcionalidades
• **Cadastro de usuário**: Permite que novos usuários se registrem no sistema;

• **Login de usuário**: Autenticação de usuários registrados;

• **Redefinição de senha**: Possibilidade de redefinir a senha através do e-mail cadastrado através do consumo da API da Twilio Sendgrid;

• **Confirmação em duas ou multi etapas** Camadas adicionais como confirmação via SMS, e-mail para ganho de segurança. 

## Ferramentas e tecnologias
• **Back-end**: Python, framework Django;

• **Front-end**: HTML5, CSS3 (Bootstrap), JavaScript (React.js);

• **Arquitetura do projeto**: Microsserviços;

• **Containers e orquestração**: Docker e Compose;

• **Padrão do projeto**: MVT (Model View Template) - Nativo do framework Django

• **Hospedagem**: AWS;

• **Banco de dados**: MySQL;

• **Autenticação**: Uso de biblioteca nativa do framework Django;

• **Código por e-mail**: Twilio Sendgrid;

• **Envio de SMS**: Twilio;

## Gerenciamento

O projeto será gerenciado com três branches principais:

- **Main**: Branch onde o projeto estará 100% funcional e pronto para produção.
- **Homologação**: Branch destinada à integração das lógicas desenvolvidas, para testes de validação antes de irem para a branch Main.
- **Testes**: Branch utilizada para o desenvolvimento e teste de novas lógicas e funcionalidades.

## Versionamento

O controle de versão será realizado utilizando o padrão `1.0.0`, onde cada número representa:

- **1**: Grandes alterações que modificam drasticamente a aplicação.
- **0**: Novas funcionalidades adicionadas. Exemplo: inclusão de uma nova tela com novas funções.
- **0**: Pequenas melhorias ou correções. Exemplo: adição de uma nova função a uma funcionalidade já existente, ou modificações menores em HTML, CSS, Python, etc.
