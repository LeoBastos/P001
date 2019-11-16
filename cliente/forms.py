from django import forms

from servico.models import Servico
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'cidade', 'email', 'telefone', 'celular', 'cpf', 'cnpj']



