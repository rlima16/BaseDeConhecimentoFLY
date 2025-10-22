from django.contrib import admin
from django.urls import path, include

#
# Observe que a linha "from . import views" NÃO ESTÁ AQUI.
# Esta é a correção principal.
#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('base.urls')), # Envia todo o tráfego principal para o app 'base'
]