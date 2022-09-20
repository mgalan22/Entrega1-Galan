from unicodedata import name
from django import forms

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    contenido = forms.CharField(max_length=500)


class SearchPost(forms.Form):
    buscar = forms.CharField(max_length=100)