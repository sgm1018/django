from socket import fromshare
from django import forms

class RegisterForm(forms.Form):
    nombre=forms.CharField(max_length=100)
    edad= forms.IntegerField()
    
