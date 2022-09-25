from django.urls import path
from userapp.views import *

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
   
]
