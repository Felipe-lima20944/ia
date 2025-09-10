from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]

# Adiciona as URLs para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
