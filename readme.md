# Entrega 1 - _Proyecto final Python+Django (Matías Galan)_

_Se intenta cumplir con los requisitos básicos para el funcionamiento de un blog en linea_

_El repositorio de la entrega final es el fork **entrega_final_heroku**_

### Pre-requisitos 📋

_revisar requeriments.txt_

## Datos y conexiones

- La aplicación **webapp** contiene todas las vistas, URLs, modelos y formularios de acceso público.
- La aplicación **userapp** contiene todas las vistas, URLs, modelos y formularios de acceso restringido.
- El sitio utiliza a index.html en el directorio **/templates** para tomar las herencias de diseño y CSS.

## Pantallas y funcionalidades
* _Se intentó agregar un módulo de edición de texto avanzado pero en el proceso la aplicación fallaba, por lo que desistí para aplicarlo habiendo adquirido mayores conocimientos_
* _Se intentaron resolver algunas funcionalidades propuestas por el profesor pero por mis escasos conocimientos no pude lograrlo: Actualización de avatar existente, actualización de datos individuales del usuario, actualización del post CON imagen null


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

### - Menú Login y Registro
* Se verifica el estado de la variable global User, si es "null" el HTML muestra la opción de inicio de sesión. Las vistas marcadas con decoradores @login_required van a solicitar autenticación por parte del usuario (Redactar articulo, edición de usuario, carga de imágenes)
* Si se verifica que la variable global User no es "null", el HTML muestra los datos de la sesión iniciada en el footer
* Se habilita al link de "Conectado como: <nombre de usuario>" para la edición del perfil.

#
_Tratandose de un proyecto en desarrollo, hay elementos que aún no tienen uso, y herencias que se deben mejorar_

* ~~Se utiliza mal el template index.html en home.html, se debe eliminar contenido y corregir herencias.~~
* Se debe cambiar en el modelo Posts, la característica content, para que sea TextArea.
* Se debe integrar el modelo Post_categories, que permitirían asignar categorías a las publicaciones
* Se debe desarrollar e integrar la característica category del modelo Posts para que se le pueda asignar de una lista desplegable la pertenencia.
* Se debe desarrollar e integrar en BD el conteo de elementos de cada categoría para poder mostrar ese dato en las consultas
* Se debe incorporar el botón para inicio de sesión/registro de usuarios que utilizaría el modelo Users
* Cambiar la característica password de User para que se maneje como tal.
* Agregar condicional para la búsqueda de publicaciones con resultado nulo.

