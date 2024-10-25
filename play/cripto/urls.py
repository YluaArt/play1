from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
path('', home, name='home'),
path('contacts/', contacts, name='contacts'),
path('rules/', rules, name='rules'),
path('policy/', policy, name='policy'),
path('about/', about, name='about'),

]