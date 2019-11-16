from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('cliente/', include('cliente.urls')),
    path('servicos/', include('servico.urls')),
    path('accounts/', include('accounts.urls')),
]
