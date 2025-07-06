from django.contrib import admin
from django.urls import path
from fingestor import views
from usuario import views as usuario_views
from transacao import views as transacao_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('login/', usuario_views.logar, name = 'login' ),
    path('register/', usuario_views.register, name = 'register'),
    path('transacao/form', transacao_views.transacao_nova, name = 'transacao_form'),
    path('transacao/', transacao_views.transacao_lista, name = 'transacoes'),
    path("transacoes/<int:pk>/editar/", transacao_views.transacao_editar, name="transacao-editar"),
    path("transacoes/<int:pk>/excluir/", transacao_views.transacao_excluir, name="transacao-excluir"),
    path('perfil', usuario_views.perfil, name = 'perfil'),
    path("perfil/alterar-senha/", usuario_views.alterar_senha, name="alterar-senha"),
    path("relatorios/", transacao_views.relatorios, name="relatorios"),
    path ('logout', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path(
        "relatorios/despesas/<int:ano>/<int:mes>/",
        transacao_views.despesas_do_mes,
        name="despesas-mes",
    ),
]
