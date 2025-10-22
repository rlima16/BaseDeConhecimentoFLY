# base/models.py
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField # <-- 1. IMPORTE ESTA LINHA

class Categoria(models.Model):
    # ... seu modelo de Categoria fica igual ...
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)

    # conteudo = models.TextField(help_text="Use HTML para formatar se necessário.") <-- 2. APAGUE OU COMENTE A LINHA ANTIGA
    conteudo = RichTextField() # <-- 3. ADICIONE ESTA LINHA NOVA

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="artigos")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_criacao']