## Passo 1: Configurar o Ambiente

Primeiro, crie um ambiente virtual para isolar as dependências do seu projeto e ative-o.

**Windows**
```sh
python -m venv env
env\Scripts\activate
```

**Linux e Mac**
```sh
python3 -m venv env
source env/bin/activate
```

## Passo 2: Instalar o Django

Com o ambiente virtual ativado, instale o Django usando o pip.

```sh
pip install django
```

## Passo 3: Criar o Projeto e o App

Crie a estrutura do projeto principal e, em seguida, crie um novo aplicativo chamado `core`.

```sh
django-admin startproject pingador .
django-admin startapp core
```

## Passo 4: Executar as Migrações

Execute as migrações iniciais para configurar o banco de dados para os aplicativos padrão do Django.

```sh
python3 manage.py migrate
```

## Passo 5: Rodar o Servidor de Desenvolvimento

Agora você pode iniciar o servidor local para ver o seu projeto em ação.

```sh
python3 manage.py runserver
```

Após executar este comando, o servidor estará disponível