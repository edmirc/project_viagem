from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name='index'),
    path('Despesas/', dados, name='dados'),
    path('Carros/', CarrosView.as_view(), name='carro'),
    path('cidades/', CidadesView.as_view(), name='cidade'),
    path('Viagem/', NomeViagemView.as_view(), name='nome-viagem'),
    path('pagamentos/', PagamentosView.as_view(), name='pagamento'),
    path('tipos-Despesa/', TiposView.as_view(), name= 'tipo'),
    path('usuarios/', UsuariosView.as_view(), name='usuario'),
    path('Viagem/Relatorios/', relatorios, name='relatorio'),
    path('Viagem/Relatorios/Resumo', resumo, name='resumo')
]
