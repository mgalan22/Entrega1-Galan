from dataclasses import fields
from pyexpat import model
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User 
        fields = ('username','email','name','last_name')