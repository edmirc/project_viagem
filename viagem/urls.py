from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name='index'),
    path('Despesas/', dados, name='dados'),
    path('Carros/', carros, name='carro'),
    path('cidades/', cidades, name='cidade'),
    path('Viagem/', nomeViagem, name='nome-viagem'),
    path('pagamentos/', pagamentos, name='pagamento'),
    path('tipos-Despesa/', tipos, name= 'tipo'),
    path('usuarios/', usuarios, name='usuarios'),
    path('Viagem/Relatorios/', relatorios, name='relatorio'),
    path('Viagem/Relatorios/Resumo', resumo, name='resumo')
]
