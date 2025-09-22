# Security Scan Workflow

Este repositório inclui um workflow GitHub Actions para realizar varreduras de segurança automatizadas em projetos Python/Django.

## Funcionalidades

- **Trivy**: Escaneia vulnerabilidades em dependências e arquivos do projeto.
- **Bandit**: Analisa o código-fonte Python em busca de falhas de segurança.
- **OWASP ZAP**: Realiza um scan de segurança automatizado na aplicação Django em execução.

## Como funciona

O workflow é executado em cada push para qualquer branch e realiza as seguintes etapas:

1. Faz checkout do repositório.
2. Configura o Python 3.9.
3. Instala as dependências do projeto.
4. Executa o Trivy para identificar vulnerabilidades.
5. Executa o Bandit para análise estática do código.
6. Inicia o servidor de desenvolvimento Django.
7. Executa o OWASP ZAP para análise dinâmica da aplicação.
8. Encerra o servidor Django.

## Exemplo de uso

Adicione o arquivo abaixo em `.github/workflows/security-scan.yml`:

```yaml
name: Security Scan

on:
    push:
        branches:
            - '*'

jobs:
    security:
        name: Security Scan
        runs-on: ubuntu-latest

        steps:
            - name: Checkout repository
                uses: actions/checkout@v2

            - name: Set up Python
                uses: actions/setup-python@v2
                with:
                    python-version: 3.9  
            - name: Install dependencies
                run: |
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                
            - name: Run Trivy vulnerability scanner in fs mode
                uses: aquasecurity/trivy-action@0.20.0
                with:
                        scan-type: 'fs'
                        scan-ref: '.'
            - name: Run Bandit
                run: |
                    pip install bandit
                    bandit -r . || true 

            - name: Start Django development server
                run: |
                    python manage.py migrate 
                    python manage.py runserver &

            - uses: actions/checkout@v3
            - name: OWASP ZAP Baseline Scan
                uses: zaproxy/action-baseline@v0.7.0
                with:
                    target: "http://127.0.0.1:8000"
                    docker_name: ghcr.io/zaproxy/zaproxy:stable
                    sarif_output: zaproxy.sarif
                continue-on-error: true
            - name: Stop Django development server
                run: |
                    pkill -f "python manage.py runserver"
```

## Requisitos

- Projeto Python/Django com arquivo `requirements.txt`.
- GitHub Actions habilitado no repositório.

## Observações

- O workflow pode ser customizado conforme as necessidades do projeto.
