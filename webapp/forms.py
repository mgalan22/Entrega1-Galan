from django import forms


class PostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length= 100)
    contenido = forms.CharField()
    foto = forms.ImageField()


class SearchPost(forms.Form):
    buscar = forms.CharField(max_length=100)