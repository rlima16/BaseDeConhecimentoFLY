# base/views.py
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Artigo
from django.contrib.auth.decorators import login_required # Importe isso

@login_required # <-- Isso protege a página, exigindo login
def home(request):
    categorias = Categoria.objects.all()
    artigos_recentes = Artigo.objects.all()[:5]
    return render(request, 'base/home.html', {
        'categorias': categorias,
        'artigos_recentes': artigos_recentes
    })

@login_required
def categoria_detail(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    artigos = Artigo.objects.filter(categoria=categoria)
    return render(request, 'base/categoria_detail.html', {
        'categoria': categoria,
        'artigos': artigos
    })

@login_required
def artigo_detail(request, slug):
    artigo = get_object_or_404(Artigo, slug=slug)
    return render(request, 'base/artigo_detail.html', {'artigo': artigo})