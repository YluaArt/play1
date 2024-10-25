

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render (request, 'cripto/home.html') 
def contacts(request):
    return render (request, 'cripto/contacts.html')
def rules(request):
    return render (request, 'cripto/rules.html')
def policy(request):
    return render (request, 'cripto/policy.html')
def about(request):
    return render (request, 'cripto/about.html')