

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
def home(request):
    return render (request, 'cripto/home.html') 
# Create your views here.
def contacts(request):


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            for f in form.cleaned_data:
                print(f)

            print('form')
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            message = form.cleaned_data['message']
            print(name)
            print(email)
            print(message)
        else:
            print('form novalid')
    else:
        form = ContactForm()
    
    return render(request, 'cripto/contacts.html', {'form': form})
def rules(request):
    return render (request, 'cripto/rules.html')
def policy(request):
    return render (request, 'cripto/policy.html')
def about(request):
    return render (request, 'cripto/about.html')