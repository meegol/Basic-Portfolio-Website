# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def languages(request):
    return render(request, 'main/languages.html')

def projects(request):
    return render(request, 'main/projects.html')
