from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.lista, name='lista'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('<int:cliente_id>', views.single, name='single'),


]