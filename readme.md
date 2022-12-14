# Entrega 1 - _Proyecto final Python+Django (Mat铆as Galan)_

_Se intenta cumplir con los requisitos b谩sicos para el funcionamiento de un blog en linea_

_El repositorio de la entrega final es el fork **entrega_final_heroku**_

### Pre-requisitos 馃搵

_revisar requeriments.txt_

## Datos y conexiones

- La aplicaci贸n **webapp** contiene todas las vistas, URLs, modelos y formularios de acceso p煤blico.
- La aplicaci贸n **userapp** contiene todas las vistas, URLs, modelos y formularios de acceso restringido.
- El sitio utiliza a index.html en el directorio **/templates** para tomar las herencias de dise帽o y CSS.

## Pantallas y funcionalidades
* _Se intent贸 agregar un m贸dulo de edici贸n de texto avanzado pero en el proceso la aplicaci贸n fallaba, por lo que desist铆 para aplicarlo habiendo adquirido mayores conocimientos_
* _Se intentaron resolver algunas funcionalidades propuestas por el profesor pero por mis escasos conocimientos no pude lograrlo: Actualizaci贸n de avatar existente, actualizaci贸n de datos individuales del usuario, actualizaci贸n del post CON imagen null_


### - Redactar art铆culo
* Llama a la vista **post_form(request)**, esta toma el formulario **PostForm** de /webapp/forms.py, vinculado al modelo Posts con sus tres caracter铆sticas
```
title=models.CharField(max_length=100)
date=models.DateField()
content=models.TextField()
```
* title y content son recibidos desde el formulario con lo que ingrese el usuario, date toma la fecha actual por funci贸n datetime.now() para guardar fecha de creaci贸n de la publicaci贸n.
* Al confirmar por metodo POST los datos en la BD, se redirecciona a la lista de todos las publicaciones en all_posts.html

### - Home
* Llama a la vista **home(request)**, que carga home.html, que muestra la p谩gina principal sin ning煤n contenido espec铆fico

### - Lista de publicaciones
* Llama a la vista **all_posts(request)** llamando a all_posts.html
* all_posts.html utiliza un ciclo for para mostrar todas las publicaciones en la BD correspondientes al modelo Posts

### - Buscar publicaciones
* Llama a la vista **find_posts(request)**, esta toma el formulario **SearchPost** , vinculado a la caracter铆stica 
```
title=models.CharField(max_length=100)
```
del modelo **Posts**
* Al confirmar por metodo GET, se pasan los datos a la vista **found_posts(request)**
* Todos los t铆tulos obtenidos de la BD se filtran seg煤n el texto ingresado por el usuario en el formulario, y se devuelve los resultados con el template **webapp/all_posts.html**

### - Readme
* Se vincula a GitHub donde est谩 cargado el readme.md que se lee en este momento.

### - Men煤 Login y Registro
* Se verifica el estado de la variable global User, si es "null" el HTML muestra la opci贸n de inicio de sesi贸n. Las vistas marcadas con decoradores @login_required van a solicitar autenticaci贸n por parte del usuario (Redactar articulo, edici贸n de usuario, carga de im谩genes)
* Si se verifica que la variable global User no es "null", el HTML muestra los datos de la sesi贸n iniciada en el footer
* Se habilita al link de "Conectado como: <nombre de usuario>" para la edici贸n del perfil.

#
_Tratandose de un proyecto en desarrollo, hay elementos que a煤n no tienen uso, y herencias que se deben mejorar_

* ~~Se utiliza mal el template index.html en home.html, se debe eliminar contenido y corregir herencias.~~
* ~~Se debe cambiar en el modelo Posts, la caracter铆stica content, para que sea TextArea.~~
* Se debe integrar el modelo Post_categories, que permitir铆an asignar categor铆as a las publicaciones
* Se debe desarrollar e integrar la caracter铆stica category del modelo Posts para que se le pueda asignar de una lista desplegable la pertenencia.
* Se debe desarrollar e integrar en BD el conteo de elementos de cada categor铆a para poder mostrar ese dato en las consultas
* ~~Se debe incorporar el bot贸n para inicio de sesi贸n/registro de usuarios que utilizar铆a el modelo Users~~
* ~~Cambiar la caracter铆stica password de User para que se maneje como tal.~~
* ~~Agregar condicional para la b煤squeda de publicaciones con resultado nulo.~~

