from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'celular')
    list_display_links = ('id', 'nome', 'email', 'celular')
    search_fields = ('name', 'email', 'telefone', 'celular')
    list_per_page = 5


admin.site.register(Cliente, ClienteAdmin)
