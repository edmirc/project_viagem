from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.views.generic import FormView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.



def index(request):
    return render(request, 'index.html')

def dados(request):
    resget = NomeViagem().countAtividade()
    if '1' not in resget.keys():
        messages.success(request, resget['n'])
        context = {}
    else:
        if request.method == 'POST':
            res = Despesas().saveDespesa(request.POST, request.FILES)
            messages.success(request, res)
        kmfinal = Despesas().lastKm()
        context = {
            'nomev': resget['1'],
            'tipos': Tipos().getTipos(),
            'cidade': Cidades().getCidade(),
            'pagamento': Pagamentos().getPagamentos(),
            'despesas': Despesas().getDespesas(),
            'km': kmfinal
        }
    return render(request, 'dados.html', context)


class CarrosView(FormView):
    template_name = 'carro.html'
    form_class = CarrosForm
    success_url = reverse_lazy('carro')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['carro'] = Carros().getCarros()
        return context

    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockCarros()
        messages.success(self.request, res)
        return super().form_valid(form)


class CidadesView(FormView):
    template_name = 'cidade.html'
    success_url = reverse_lazy('cidade')
    form_class = CidadesForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cidade'] = Cidades().getCidade()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockCidades()
        messages.success(self.request, res)
        return super().form_valid(form)


class NomeViagemView(FormView):
    template_name = 'nome-viagem.html'
    form_class = NomeViagemForm
    success_url = reverse_lazy('nome-viagem')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['nomeviagem'] = NomeViagem().getNomeViagem()
        context['user'] = Usuario().getUsers()
        context['carro'] = Carros().getCarros()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockTripName()
        messages.success(self.request, res)
        return super().form_valid(form)


class PagamentosView(FormView):
    template_name = 'pagamento.html'
    success_url = reverse_lazy('pagamento')
    form_class = PagamentosForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pagamento'] = Pagamentos().getPagamentos()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockPagamento()
        messages.success(self.request, res)
        return super().form_valid(form)

class TiposView(FormView):
    template_name = 'tipo.html'
    success_url = reverse_lazy('tipo')
    form_class = TiposForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tipo'] = Tipos().getTipos()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockType()
        messages.success(self.request, res)
        return super().form_valid(form)

class UsuariosView(FormView):
    template_name = 'usuario.html'
    success_url = reverse_lazy('usuario')
    form_class = UsuariosForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['usuario'] = Usuario().getUsers()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockUser()
        messages.success(self.request, res)
        return super().form_valid(form)

def relatorios(request):
    if request.method == 'POST':
        despesa = Despesas().relDespesas(request)
        if len(despesa[0]) == 0:
            messages.success(request, "Sem dados para exibir!!")
    else:
        despesa = ['','', '']
    context = {
        'nomeRel': NomeViagem().getNomeViagem(),
        'tipo': Tipos().getTipos(),
        'despesa': despesa[0],
        'pagamento': Pagamentos().getPagamentos(),
        'total': despesa[1],
        'adiantamento': despesa[2]
    }
    return render(request, 'relatorio.html', context)

def resumo(request):
    context = dict()
    if request.method == 'POST':
        context['soma'] = Despesas().resumoDespes(request.POST.get('viagem'))
        context['pg'] = Despesas().resumoPagamento(request.POST.get('viagem'))
    context['viagem']= NomeViagem().getNomeViagem()
    context['forma'] = Pagamentos().getPagamentos()
    return render(request, 'resumo.html', context)