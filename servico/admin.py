from django.contrib import admin
from .models import Servico


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'carro', 'placa', 'modelo', 'tipo', 'descricao', 'status')


admin.site.register(Servico, ServicoAdmin)