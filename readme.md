# Proyecto final Python+Django en desarrollo

_Se intenta cumplir con los requisitos básicos para el funcionamiento de un blog en linea_


### Pre-requisitos 📋

_Ninguno, se hizo push del proyecto completo, incluyendo la base de datos que ya está en uso, no se instalaron complementos extra_

## Datos y conexiones

- La applicación **webapp** contiene todas las vistas, URLs, modelos y formularios:
views.py
urls.py
models.py
forms.py

- El sitio utiliza a index.html en el directorio **/templates** para tomar las herencias de diseño y CSS.

## Pantallas y funcionalidades
_Todos los links en el sitio son funcionales_

### - Redactar artículo
* Llama a la vista **post_form(request)**, esta toma el formulario **PostForm** de /webapp/forms.py, vinculado al modelo Posts con sus tres características
```
title=models.CharField(max_length=100)
date=models.DateField()
content=models.TextField()
```
* title y content son recibidos desde el formulario con lo que ingrese el usuario, date toma la fecha actual por función datetime.now() para guardar fecha de creación de la publicación.
* Al confirmar por metodo POST los datos en la BD, se redirecciona a la lista de todos las publicaciones en all_posts.html
