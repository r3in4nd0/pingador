# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o resto do código da sua aplicação
COPY . .

# Expõe a porta que o servidor Django irá usar
EXPOSE 8000

# Defina o script de entrada
ENTRYPOINT ["./entrypoint.sh"]