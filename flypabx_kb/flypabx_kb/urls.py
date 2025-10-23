# Em flypabx_kb/flypabx_kb/urls.py
from django.contrib import admin
from django.urls import path, include # <-- Importante ter o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta é a linha principal:
    # Ela diz: "Qualquer URL que chegar na raiz ('')
    # deve ser enviada para o arquivo urls.py do app 'base'"
    path('', include('base.urls')),
]