from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('home')),
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('userapp/', include('userapp.urls'))
]
