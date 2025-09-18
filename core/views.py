from django.shortcuts import render

# Create your views here.

import os  

def pingar(request,ip):
    command = f'ping -c 1 {ip}'
    os.system(command)
    return render(request,'core/index.html',{'ip':ip})
def home(request):
    return render(request,'core/index.html')
