from django.contrib import admin
from django.urls import path
from fingestor import views
from usuario import views as usuario_views
from transacao import views as transacao_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('login/', usuario_views.logar, name = 'login' ),
    path('register/', usuario_views.register, name = 'register'),
    path('transacao/form', transacao_views.transacao_nova, name = 'form_transacao'),
    path('transacao/', transacao_views.transacao_lista, name = 'transacoes'),
    path("transacoes/<int:pk>/editar/", transacao_views.transacao_editar, name="transacao-editar"),
    path("transacoes/<int:pk>/excluir/", transacao_views.transacao_excluir, name="transacao-excluir"),
]
