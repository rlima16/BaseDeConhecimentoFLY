# Em flypabx_kb/base/urls.py
from django.urls import path
from . import views # O '.' importa o views.py da mesma pasta

urlpatterns = [
    # Esta linha diz: "A URL raiz ('') que o projeto nos enviou
    # será tratada pela função 'views.home'"
    path('', views.home, name='home'),
    
    # Suas outras URLs:
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('artigo/<slug:slug>/', views.artigo_detail, name='artigo_detail'),
    path('search/', views.search_results, name='search_results'),
]