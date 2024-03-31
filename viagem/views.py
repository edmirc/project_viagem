from typing import Any
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from .forms import *
from django.urls import reverse_lazy
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosView(FormView):
    template_name = 'dados.html'
    success_url = reverse_lazy('dados')
    form_class = DespesasForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        resget = NomeViagem().countAtividade()
        if '1' not in resget.keys():
            messages.success(self.request, resget['n'])
        else:
            context['nomev']= resget['1']
            context['tipos'] = Tipos().getTipos()
            context['cidade'] = Cidades().getCidade()
            context['pagamento'] = Pagamentos().getPagamentos()
            context['despesas'] = Despesas().getDespesas()
            context['km'] = Despesas().lastKm()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.stockExpenses()
        messages.success(self.request, res)
        return super().form_valid(form)
    
    def form_invalid(self, form: Any) -> HttpResponse:
        messages.error(self.request, 'Dados inválidos!!!')
        return super().form_invalid(form)


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


class RelatoriosView(FormView):
    template_name = 'relatorio.html'
    success_url = reverse_lazy('relatorio')
    form_class = RelatoriosForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        lista: list = list()
        context = super().get_context_data(**kwargs)
        context['nomeRel'] = NomeViagem().getNomeViagem()
        for i in Tipos().getTipos():
            lista.append(i.tipo)
        context['tipo'] =  lista
        lista = list()
        for i in Pagamentos().getPagamentos():
            lista.append(i.forma)
        context['pagamento'] = lista
        return  context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.resultRel()
        if res == '1':
            res = form.resultBtSend()
            if len(res[0]) == 0:
                messages.success(self.request, 'Sem dados para exibir!!')
                return super().form_valid(form)
            else:
                dados: dict = dict()
                dados['nomeRel'] = NomeViagem().getNomeViagem()
                dados['tipo'] =  Tipos().getTipos()
                dados['pagamento'] = Pagamentos().getPagamentos()
                dados['despesa'] = res[0]
                dados['total'] = res[1]
                dados['adiantamento'] = res[2]
                self.get_context_data(form=form, result = dados)
            return self.render_to_response(dados)
        else:
            res = form.resultBtExcell()
            return res


class ResumoView(FormView):
    template_name = 'resumo.html'
    success_url = reverse_lazy('resumo')
    form_class = ResumoForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['viagem']= NomeViagem().getNomeViagem()
        context['forma'] = Pagamentos().getPagamentos()
        return context
    
    def form_valid(self, form: Any) -> HttpResponse:
        res = form.summaryReport()
        dados = dict()
        dados['soma'] = res['soma']
        dados['viagem']= NomeViagem().getNomeViagem()
        dados['forma'] = Pagamentos().getPagamentos()
        dados['pg'] = res['pg']
        self.get_context_data(form=form, result=dados)
        return self.render_to_response(dados)

class LoginView(FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('login')
    form_class = LoginForm