from dataclasses import fields
from pyexpat import model
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from userapp.models import Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields= "__all__"

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    first_name= forms.CharField()
    last_name= forms.CharField()
        

    class Meta:
        model = User 
        fields = ('username','email','first_name','last_name')