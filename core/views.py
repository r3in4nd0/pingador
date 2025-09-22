from django.shortcuts import render

# Create your views here.

import os  

def pingar(request,ip):
    command = f'ping -c 1 {ip}'
    os.system(command)
    return render(request,'core/index.html',{'ip':ip})
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