from django.urls import path
from .views import index, contato, produto, estoque

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('estoque/', estoque, name='estoque'),
]