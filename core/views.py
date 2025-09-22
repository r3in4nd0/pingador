from django.shortcuts import render

# Create your views here.

import os  

def pingar(request,ip):
    import os
    import uuid

    # Gera um nome de arquivo temporário único
    temp_filename = f"temp_output_{uuid.uuid4()}.txt"

    # Comando a ser executado, com redirecionamento para o arquivo temporário
    # O '2>&1' redireciona a saída de erro (stderr) para a mesma saída da saída padrão (stdout)
    command = f"ping -c 1 {ip} > {temp_filename} 2>&1"

    # Executa o comando. O retorno de os.system é o código de saída, não a string
    return_code = os.system(command)

    # Se o comando executou com sucesso (código 0), leia o arquivo
    if return_code == 0:
        try:
            with open(temp_filename, 'r') as file:
                output_string = file.read()
            print("Saída do comando:")
            print(output_string)
        except FileNotFoundError:
            print("Erro: O arquivo temporário não foi criado.")
    else:
        print(f"O comando falhou com o código de saída: {return_code}")

    # Limpa o arquivo temporário, se ele existir
    if os.path.exists(temp_filename):
        os.remove(temp_filename)
        print(f"\nArquivo temporário '{temp_filename}' removido.")
    return render(request,'core/index.html',{'ip':ip,'output':output_string})
def home(request):
    return render(request,'core/index.html')


from django.http import JsonResponse
from django.db.models import Count, Q

from django.http import HttpResponse

from .models import Blog


def blogs(request):
    field = request.GET.get('field', 'title')
    blogs_count = Blog.objects.annotate(**{field: Count("title")})
    print(field)    

    data = ""
    for blog_count in blogs_count:
        data += f"<h2>{blog_count.title}</h2>"
    return HttpResponse(data)