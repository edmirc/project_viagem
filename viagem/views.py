from django.shortcuts import render
from .models import *
from django.contrib import messages

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

def carros(request):
    if request.method == 'POST':
        res = Carros().salveCarros(request.POST)
        messages.success(request, res)
    context = {
        'carro': Carros().getCarros()
    }
    return render(request, 'carro.html', context)
    

def cidades(request):
    if request.method == 'POST':
        res = Cidades().salveCidade(request.POST)
        messages.success(request, res)
    context = {
        'cidade': Cidades().getCidade()
    }
    return render(request, 'cidade.html', context)

def nomeViagem(request):
    if request.method == 'POST':
        res = NomeViagem().saveNomeViagem(request.POST)
        messages.success(request, res)
    context = {
        'carro': Carros().getCarros(),
        'user': Usuario().getUsers(),
        'nomeviagem': NomeViagem().getNomeViagem()
    }
    return render(request, 'nome-viagem.html', context)

def pagamentos(request):
    if request.method == 'POST':
        res = Pagamentos().savePagamentos(request.POST)
        messages.success(request, res)
    context = {
        'pagamento': Pagamentos().getPagamentos()
    }
    return render(request, 'pagamento.html', context)

def tipos(request):
    if request.method == 'POST':
        res = Tipos().saveTipos(request)
        messages.success(request, res)
    context = {
        'tipo': Tipos().getTipos()
    }
    return render(request, 'tipo.html', context)

def usuarios(request):
    if request.method == 'POST':
        res = Usuario().saveUsuarios(request.POST)
        messages.success(request, res)
    context = {
        'usuario': Usuario().getUsers()
    }
    return render(request, 'usuario.html', context)

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