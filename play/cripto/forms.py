from django import forms
from .models import *
class ContactForm(forms.Form):
 class  Meta:
    model = Contact
    fields = ('name', "email", "message")