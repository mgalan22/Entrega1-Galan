from django import forms


class PostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length= 200)
    contenido = forms.CharField()
    foto = forms.ImageField(allow_empty_file=True)


class SearchPost(forms.Form):
    buscar = forms.CharField(max_length=100)