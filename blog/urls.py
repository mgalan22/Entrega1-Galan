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
from unicodedata import name
from django.contrib import admin
from django.urls import path

from webapp.views import about_me, del_post, edit_post, new_user, read_more, view_all_posts, home, add_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',home, name='home'),
    path('about/', about_me, name='about'),
    path('pages/<pageId>',read_more, name='read_more'),
    path('alta/', new_user, name='new_user'),
    path('post/<str:title>/<str:content>', add_post,name='add_post'),
    path('edit_post/', edit_post, name='edit_post'),
    path('del_post/', del_post, name='del_post'),
    path('blog/', view_all_posts,name='view_all_posts'),

]
