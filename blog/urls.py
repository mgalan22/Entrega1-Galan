from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings

from userapp.views import upload_avatar

urlpatterns = [
    path('', lambda req: redirect('home')),
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
    path('userapp/', include('userapp.urls'))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)