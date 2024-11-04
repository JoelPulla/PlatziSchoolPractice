"""
    GLOBAL URLS 
"""
from django.contrib import admin
from django.urls import path, include

# libreria para las imagenes 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('products.urls')),
    path('users/', include('users.urls'))  
    
    # urls de las imagenes 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

