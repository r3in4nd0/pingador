#!/bin/bash

# Espera o banco de dados ficar disponível
echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database started!"

# Executa as migrações do Django
python manage.py migrate

# Cria um superusuário se ele ainda não existir
python manage.py createsuperuser --username admin --email "" --noinput || true

# Define a senha para o superusuário
# Isso é necessário porque o --noinput não permite definir a senha
# A linha || true é para ignorar o erro caso o superusuário já exista
echo "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='admin'); user.set_password('admin'); user.save()" | python manage.py shell

# Inicia o servidor de desenvolvimento do Django
exec "$@"