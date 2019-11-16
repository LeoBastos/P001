from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from servico import forms
from servico.forms import FormServico
from servico.models import Servico


@login_required(redirect_field_name='login')
def servico(request):
    servicos = Servico.objects.order_by('status')
    paginator = Paginator(servicos, 10)

    page = request.GET.get('page')
    servicos = paginator.get_page(page)
    return render(request, 'servico/servico.html', {
        'servicos': servicos
    })


@login_required(redirect_field_name='login')
def listar(request):
    servicos = Servico.objects.all()
    paginator = Paginator(servicos, 20)

    page = request.GET.get('page')
    servicos = paginator.get_page(page)
    return render(request, 'servico/listar.html', {
        'servicos': servicos
    })


@login_required(redirect_field_name='login')
def ver_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    return render(request, 'servico/ver_servico.html', {
        'servico': servico
    })


@login_required(redirect_field_name='login')
def cadastrar(request):
    if request.method != 'POST':
        form = FormServico()
        return render(request, 'servico/cadastrar.html', {'form': form})

    form = FormServico(request.POST)

    if not form.is_valid():
        form = FormServico(request.POST)
        return render(request, 'servico/cadastrar.html', {'form': form})

    form.save()
    messages.success(request, 'Serviço Cadastrado com Sucesso')
    return redirect('listar')


@login_required(redirect_field_name='login')
def editar(request, pk, template_name='servico/editar.html'):
    servico = get_object_or_404(Servico, pk=pk)
    form = forms.FormServico(request.POST or None, instance=servico)
    if form.is_valid():
        form.save()
        messages.success(request, 'Serviço Editado com sucesso')
        return redirect('servico')
    return render(request, template_name, {'form':form})


@login_required(redirect_field_name='login')
def historico(request):
    historys = Servico.objects.all()
    context = {
        'historys': historys
    }
    return render(request, 'servico/ver_servico.html', context)