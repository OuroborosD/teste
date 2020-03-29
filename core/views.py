from django.shortcuts import render, redirect, get_object_or_404
from .forms import  ContatoForm,  ProdutoModelForm
from django.contrib import  messages
from .models import  Produto



def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)  # pode vir as informações ou não da página contato
    if str(request.method) == 'POST': # se o metodo que ele recebeu é 'POST'
        if form.is_valid():  #checa se os dados são validos
            nome = form.cleaned_data['nome']# converte os dados para python
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada!')
            print(f'Nome : {nome}')
            print(f'E-mail: {email}')
            print(f'assunto:    {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, ' Email enviado com sucesso!')  # irá aparecer um pop up com a mensagem
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar email')
    context = {
        'contato': form
    }
    return render(request,'contato.html',context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
            if str(request.method) == 'POST':
                    form = ProdutoModelForm(request.POST)
                    if form.is_valid():
                        form.save()  # vai salver no banco de dados
                        form = ProdutoModelForm() # vai limpar os dados
                        messages.success(request,'Produto salvo com sucesso')

                    else:
                        messages.error("erro ao salvar produto")

            else:
                form = ProdutoModelForm()
            context = {
                'produto': form
            }
            return render(request,'produto.html', context)

    else:
        return redirect('index')  # manda para a tela de cadratro, caso não seja usuário logado




    """
    form = ProdutoForm(request.POST or None)  # pode vir as informações ou não da página contato
    if str(request.method) == 'POST': # se o metodo que ele recebeu é 'POST'
        if form.is_valid():  #checa se os dados são validos
            nome = form.cleaned_data['nome']# converte os dados para python
            valor = form.cleaned_data['valor']
            validade = form.cleaned_data['validade']
            lote = form.cleaned_data['lote']
            data = form.cleaned_data['dataCompra']
            peso = form.cleaned_data['peso']
            quantidade = form.cleaned_data['quantidade']
            escolha = form.cleaned_data['escolha']

            print('Mensagem enviada!')
            print(f'Nome : {nome}')
            print(f'valor:    {valor}')
            print(f'validade: {validade}')
            print(f'data: {data}')
            print(f'peso: {peso}')
            print(f'quantidade: {quantidade}')
            print(f'lote: {lote}')
            print(f'esclha: {escolha}')

            messages.success(request, ' produto cadastrado com sucesso!')  # irá aparecer um pop up com a mensagem
            form = ProdutoForm()
        else:
            messages.error(request, 'erro ao cadastrar produto')
    context = {
        'prod': form
    }
    return render(request,'produto.html',context)
    """

def estoque(request):
    if str(request.user) != 'AnonymousUser':
        context = {
             'produto_estoque' : Produto.objects.all()
        }
        return render(request,'estoque.html',context)
    else:
        return redirect('index')  # manda para a tela de cadratro, caso não seja usuário logado