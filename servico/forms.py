from django import forms

from servico.models import Servico


class FormServico(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'fabricante', 'carro', 'placa', 'ano', 'modelo', 'pintura', 'motor', 'combustivel', 'tipo', 'descricao', 'solucao', 'pecas', 'status', 'preco']
