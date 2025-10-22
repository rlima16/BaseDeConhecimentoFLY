# flypabx_kb/flypabx_kb/urls.py

from django.contrib import admin
from django.urls import path, include # 'include' deve estar aqui

# REMOVA a linha "from . import views" se ela estiver aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', include('base.urls')), # Esta linha importa o outro arquivo
]