from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from cliente import forms
from cliente.forms import ClienteForm
from cliente.models import Cliente


@login_required
def cliente(request):
    clientes = Cliente.objects.order_by('-id')

    paginator = Paginator(clientes, 10)
    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    return render(request, 'cliente/cliente.html', {
        'clientes': clientes
    })


@login_required
def cadastro(request):
    if request.method != 'POST':
        form = ClienteForm()
        return render(request, 'cliente/cadastro.html', {'form': form})

    form = ClienteForm(request.POST)

    if not form.is_valid():
        form = ClienteForm(request.POST)
        return render(request, 'cliente/cadastro.html', {'form': form})

    form.save()
    return redirect('cliente')


@login_required
def edit(request, pk, template_name='cliente/edit.html'):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = forms.ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente')
    return render(request, template_name, {'form':form})


@login_required
def lista(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 20)

    page = request.GET.get('page')
    clientes = paginator.get_page(page)
    return render(request, 'cliente/lista.html', {
        'clientes': clientes
    })


@login_required(redirect_field_name='login')
def single(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/single.html', {
        'cliente': cliente
    })