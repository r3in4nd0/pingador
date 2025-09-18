# Pingador3

Projeto Django para realizar pings em endereços IP via interface web.

## Configuração Inicial

1. **Adicione o app `core` em `INSTALLED_APPS`**
   
   No arquivo `pingador/settings.py`, inclua `'core',` na lista `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # ...outros apps...
       'core',
   ]
   ```

2. **Estrutura de Templates**
   ```bash
   cd core
   mkdir -p templates/core
   cd ../..
   ```

3. **Configuração de URLs do Projeto**
   
   No arquivo `pingador/urls.py`, adicione:
   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('core.urls')),
   ]
   ```

4. **URLs do App**
   
   Crie o arquivo `core/urls.py` com:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('pingar/<ip>', views.pingar),
       path('', views.home),
   ]
   ```

5. **Views**
   
   No arquivo `core/views.py`, adicione:
   ```python
   from django.shortcuts import render
   import os

   def pingar(request, ip):
       command = f'ping {ip}'
       os.system(command)
       return render(request, 'core/index.html', {'ip': ip})

   def home(request):
       return render(request, 'core/index.html')
   ```

6. **Templates**
   
   Crie o arquivo `core/templates/core/index.html` para a interface.

7. **Create git ignore**
   
   
   ```
   # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class

    # C extensions
    *.so

    # Virtual environment
    env/
    venv/
    ENV/
    .venv/
    env.bak/

    # Distribution / packaging
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST

    # Django stuff:
    *.log
    *.pot
    *.pyc
    *.pyo
    *.db
    *.sqlite3
    db.sqlite3
    media/
    staticfiles/
    static_root/
    *.mo

    # Django migrations
    **/migrations/*.py
    !**/migrations/__init__.py

    # PyInstaller
    *.manifest
    *.spec

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py,cover
    .hypothesis/
    .pytest_cache/

    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json

    # Pyre type checker
    .pyre/

    # VS Code
    .vscode/

    # PyCharm
    .idea/
    *.iml

    # macOS
    .DS_Store

    # Windows
    Thumbs.db
    ehthumbs.db
    Desktop.ini
    $RECYCLE.BIN/

    # Others
    *.swp
    *.swo
    *.bak
    *.tmp
    *.orig

   ```
---

Siga esses passos para configurar as rotas, views, templates e apps do seu sistema