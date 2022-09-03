from django.urls import path
from webapp.views import home, all_posts, add_post

urlpatterns = [
    path('',home, name='WebappHome'),
    path('post/<str:title>/<str:content>', add_post, name='WebappAdd_post'),
    path('list/', all_posts, name='WebappAll_posts'),

]
