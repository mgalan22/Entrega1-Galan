"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import about_me, alta_usuario, crear_publicacion, del_publicacion, editar_publicacion, home, leer_mas, ver_publicaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',home),
    path('about/', about_me),
    path('pages/<pageId>',leer_mas),
    path('alta/', alta_usuario),
    path('post/', crear_publicacion),
    path('edit_post/', editar_publicacion),
    path('del_post/', del_publicacion),
    path('blog/', ver_publicaciones),

]
