from django.urls import path
from webapp.views import home, view_all_posts, add_post

urlpatterns = [
    path('',home, name='WebappHome'),
    path('post/<str:title>/<str:content>', add_post, name='WebappAdd_post'),
    path('blog/', view_all_posts, name='WebappView_all_posts'),

]
