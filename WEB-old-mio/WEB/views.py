from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> HOLA MUNDO! </h1>")

def servicioCl(request):
    return render(request, 'servicioCl.html')