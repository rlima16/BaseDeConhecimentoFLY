# base/urls.py

from django.urls import path
from . import views  # <-- A linha pertence a este arquivo

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('artigo/<slug:slug>/', views.artigo_detail, name='artigo_detail'),
]