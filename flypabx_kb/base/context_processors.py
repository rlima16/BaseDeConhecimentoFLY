# base/context_processors.py
from .models import Categoria

def all_categories(request):
    """
    Disponibiliza a lista de todas as categorias para todos os templates.
    """
    return {
        'all_categories': Categoria.objects.all()
    }