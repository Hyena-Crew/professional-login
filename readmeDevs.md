# Comandos git para importar o projeto
- Para fazer pull request pela primeira vez siga esses passos:
    ```bash
    git init
    git remote add origin https://github.com/Hyena-Crew/professionalLogin.git
    git pull origin main

## Comandos git para commit
- Para realizar um commit:
    ```bash
    git status
    git add .
    git commit -m "Mensagem de commit detalhando o máximo possível"
    git push -u origin main
    ```

# Iniciando as configurações (Linux):
- Para criar a venv:
    ```bash
    python3 -m venv venv
    ```

- Para ativar a venv:
    ```bash
    source venv/bin/activate
    ```

# Iniciando as configurações (Windows):
- Para criar a venv:
    ```bash
    python -m venv venv
    ```

- Para ativar a venv (não funciona no Git Bash):
    ```bash
    .\venv\Scripts\activate
    ```

# Criando usuário admin:
- Para criar um usuario admin basta rodar o codigo abaixo e seguir o passo a passo:
    ```bash
    python manage.py createsuperuser
    ```

# Bibliotecas dependentes:
- Para instalar as bibliotecas:
    ```bash
    pip install django
    pip install pillow
    ```

## Criação do Dockerfile 
O Dockerfile permite a construção de uma imagem própria da aplicação, sem a necessidade e o dever de executá-la localmente. Para criá-lo, basta executar o seguinte comando:
```
docker image build -t professional-login .
```
Obs: É muito importante se atentar e não esquecer do ponto final 

Após isso, execute:
```
docker run -p 5000:5000 -d professional-login
```

### Criação do Docker Compose 
Para executar o Docker Compose, é necessário que os containers sejam parados. Liste todos para recuperar o ID e então:
```
docker stop id-container-1 (aplicação)
docker stop id-container-2 (banco de dados)
```
Agora sim, o compose pode ser executado:
```
docker compose up -d
```
Obs: Será necessário recriar o próprio banco e tabelas e é importante que antes desse comando ser rodado, a tag definida no arquivo .yml seja alterada nas configuração do banco, mais especificamente na chave "host" ao invés do ID do container Docker

Em caso de uma eventual mudança ou restabelecimento:
```
docker compose stop
docker compose down 
```

# Documentos / Referências
 - https://grizzly-amaranthus-f6a.notion.site/Aula-1-05f0cce37def4684a07b3e7593ac6fa8?pvs=4
 - https://grizzly-amaranthus-f6a.notion.site/Aula-2-7413f7b7bcfa46ac90a8a468f16b59f2?pvs=4
 - https://grizzly-amaranthus-f6a.notion.site/Aula-3-f86922b024ef4456b49bddeb77fbb9cd?pvs=4
    