# Comandos git:
- Para fazer pull request pela primeira vez siga esses passos:
    ```bash
    git init
    git remote add origin https://github.com/BredexBR/professionalLogin.git
    git pull origin main

## Commit
- Para fazer um commit
    ```bash
    git status
    git add .
    git commit -m "Mensagem commit"
    git push -u origin main

# Iniciando as configurações(Linux):
- Para criar a venv:
    ```bash
    python3 -m venv venv

- Para ativar a venv:
    ```bash
    source venv/bin/activate

# Iniciando as configurações(Windows):
- Para criar a venv:
    ```bash
    python -m venv venv

- Para ativar a venv(Não funciona no Git Bash):
    ```bash
    .\venv\Scripts\activate

# Criando Usuário Admin:
- Para criar um usuario admin basta rodar o codigo abaixo e seguir o passo a passo:
    ```bash
    python manage.py createsuperuser

# Bibliotecas dependentes:
- Para instalar as bibliotecas:
    ```bash
    pip install django
    pip install pillow


# Documentos / Sites Consulta
 - https://grizzly-amaranthus-f6a.notion.site/Aula-1-05f0cce37def4684a07b3e7593ac6fa8?pvs=4
 - https://grizzly-amaranthus-f6a.notion.site/Aula-2-7413f7b7bcfa46ac90a8a468f16b59f2?pvs=4
 - https://grizzly-amaranthus-f6a.notion.site/Aula-3-f86922b024ef4456b49bddeb77fbb9cd?pvs=4
    