from django.urls import path
from . import views  # <-- A importação de views pertence a ESTE arquivo

urlpatterns = [
    # Caminho para a página inicial
    path('', views.home, name='home'),
    
    # Caminho para a nova página de busca
    path('search/', views.search_results, name='search_results'),
    
    # Caminhos para categorias e artigos
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('artigo/<slug:slug>/', views.artigo_detail, name='artigo_detail'),
]