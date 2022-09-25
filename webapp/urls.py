from django.urls import path
from webapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('all_posts/', all_posts, name='all_posts'),
    path('create/',post_form, name='post_form'),
    path('find_post/',find_post, name='find_post'),
    path('found_posts/',found_posts, name='found_posts'),
    path('readme/',read_me, name='readme'),
    path('del_post/<int:id>',del_post, name='del_post'),
    path('edit_post/<int:post_id>',edit_post, name='edit_post'),
]
