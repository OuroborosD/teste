from django.contrib import admin
from .models import Produto
# Register your models here.

@admin.register(Produto) # decorador para só conseguir cadatras usários logados
class ProdutoAdmin(admin.ModelAdmin):
         list_display = ('nome', 'valor', 'quantidade', 'peso' , 'validade', 'volume', 'escolha', 'validade', 'lote', 'tag', 'criado', 'slug')