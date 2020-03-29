from stdimage.models import StdImageField
from datetime import  datetime
from django.db import models
from django.utils import timezone

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('data de criação', auto_now_add=True)# atualiza sempre que usado
    modificado = models.DateField('data de atualização', auto_now=True)# atualiza na criação.
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True # classe abistata não é criada no banco de dados


class Produto(Base):# herda de produtos
    lista = (('1', 'unidade'), ('2', 'pacote'), ('3', 'peso'), ('4', 'litro'))
    nome = models.CharField('nome', max_length=100)
    escolha = models.CharField('Precificado por: ',choices=lista, max_length=100)
    valor = models.DecimalField('valor do produto', max_digits=8, decimal_places=2)# 2 numeros depois da virgula
    quantidade = models.IntegerField('quantidade', blank= True, default=1)
    peso = models.DecimalField('peso em KG', max_digits=100, decimal_places=2, blank= True, null= True)
    volume = models.DecimalField('volume em Litro', max_digits=100, decimal_places=2, blank=True, null=True)
    validade = models.DateField('Data de Validade', blank=True, null=True)
    lote = models.CharField('lote', blank=True, max_length=100, default='404')# para não ser obrigatorio
    tag = models.CharField('tag onde sera usado o produto EX: lanche, prato', blank= True, max_length=100, default='outros')
    slug = models.SlugField('Slug', max_length=100,blank=True,editable=False)
    dataCompra = models.DateField('Data da Compra: ',default= timezone.now)

    def _str__(self):# nome do campo aparecer
        return self.nome

def produto_pre_save(signal,instance,sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save,sender=Produto)