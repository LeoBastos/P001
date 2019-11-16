from django.urls import path
from . import views

urlpatterns = [
    path('', views.servico, name='servico'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('editar/<int:pk>', views.editar, name='editar'),
    path('<int:servico_id>', views.ver_servico, name='ver_servico'),
]