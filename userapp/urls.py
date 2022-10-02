from django.urls import path
from userapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='webapp/home.html') , name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', user_edit, name='user_edit'),
    path('avatar/',upload_avatar, name='upload_avatar')
]
