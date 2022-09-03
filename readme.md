# Entrega 1 - _Proyecto final Python+Django (Matías Galan)_

_Se intenta cumplir con los requisitos básicos para el funcionamiento de un blog en linea_

_El repositorio de la entrega 1 es el fork **pre-entrega**_

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



#

_Tratandose de un proyecto en desarrollo, hay elementos que aún no tienen uso, y herencias que se deben mejorar_

* Se utiliza mal el template index.html en home.html, se debe eliminar contenido y corregir herencias.
* Se debe cambiar en el modelo Posts, la característica content, para que sea TextArea.
* Se debe integrar el modelo Post_categories, que permitirían asignar categorías a las publicaciones
* Se debe desarrollar e integrar la característica category del modelo Posts para que se le pueda asignar de una lista desplegable la pertenencia.
* Se debe desarrollar e integrar en BD el conteo de elementos de cada categoría para poder mostrar ese dato en las consultas
* Se debe incorporar el botón para inicio de sesión/registro de usuarios que utilizaría el modelo Users
* Cambiar la característica password de User para que se maneje como tal.
* Agregar condicional para la búsqueda de publicaciones con resultado nulo.

