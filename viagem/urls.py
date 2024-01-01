from django.urls import path
from .views import *


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('Despesas/', DadosView.as_view(), name='dados'),
    path('Carros/', CarrosView.as_view(), name='carro'),
    path('cidades/', CidadesView.as_view(), name='cidade'),
    path('Viagem/', NomeViagemView.as_view(), name='nome-viagem'),
    path('pagamentos/', PagamentosView.as_view(), name='pagamento'),
    path('tipos-Despesa/', TiposView.as_view(), name= 'tipo'),
    path('usuarios/', UsuariosView.as_view(), name='usuario'),
    path('Viagem/Relatorios/', RelatoriosView.as_view(), name='relatorio'),
    path('Viagem/Relatorios/Resumo', resumo, name='resumo')
]
