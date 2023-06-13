from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello<h1>')

def home(request):
    return render(request, 'myapp/home.html')