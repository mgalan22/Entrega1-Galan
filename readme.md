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

### - Home
* Llama a la vista **home(request)**, que carga home.html, que muestra la página principal sin ningún contenido específico

### - Lista de publicaciones
* Llama a la vista **all_posts(request)** llamando a all_posts.html
* all_posts.html utiliza un ciclo for para mostrar todas las publicaciones en la BD correspondientes al modelo Posts

### - Buscar publicaciones
* Llama a la vista **find_posts(request)**, esta toma el formulario **SearchPost** , vinculado a la característica 
```
title=models.CharField(max_length=100)
```
del modelo **Posts**
* Al confirmar por metodo GET, se pasan los datos a la vista **found_posts(request)**
* Todos los títulos obtenidos de la BD se filtran según el texto ingresado por el usuario en el formulario, y se devuelve los resultados con el template **webapp/all_posts.html**

### - Readme
* Se vincula a GitHub donde está cargado el readme.md que se lee en este momento.
