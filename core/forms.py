from django import forms
from datetime import datetime
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

"""
class ProdutoForm(forms.Form):

    lista = [('1','unidade'), ('2','pacote'),('3', 'peso'),('4','litro')]
    nome = forms.CharField(label='nome', max_length= 100)
    escolha = forms.ChoiceField(label='Precificado por: ',widget=forms.RadioSelect, choices=lista)
    valor = forms.DecimalField(label='valor do produto')
    quantidade = forms.IntegerField(label='quantidade')
    peso = forms.DecimalField(label='peso em KG')
    validade = forms.DateField(label='Data de Validade')
    lote = forms.CharField(label='lote', required=False)
    dataCompra = forms.DateTimeField(label='Data da Compra: ',initial=datetime.now())
"""

class ProdutoModelForm(forms.ModelForm):
     class Meta: # não cria no banco de dados
        model = Produto
        fields = ['nome', 'escolha', 'valor', 'quantidade', 'peso', 'validade', 'volume','lote', 'tag','dataCompra']
