from django import forms
from .models import *


class CarrosForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    placa = forms.CharField(label='placa', max_length=7, strip=True)
    modelo = forms.CharField(label='modelo', max_length=50, strip=True)

    def stockCarros(self):
        dados:dict = dict()
        dados['id'] = self.cleaned_data['id']
        dados['placa'] = self.cleaned_data['placa'].upper()
        dados['modelo'] = self.cleaned_data['modelo'].title()
        checkplate = self.checkPlate(dados['placa'])
        if dados['id'] is None:
            if checkplate != '':
                return checkplate
            return Carros().salveCarros(dados, 'salvar')
        else:
            return Carros().salveCarros(dados, 'alterar')
    
    def checkPlate(self, plate:str) -> str:
            id =  Carros.objects.filter(placa=plate)
            try:
                id = id[0].id
                return  f'Carro {plate}, já cadastrado com o id {id}!!'
            except:
                return ""


class CidadesForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    nome = forms.CharField(label='nome', max_length=100, strip=True)
    estado = forms.CharField(label='estado', max_length=2, min_length=2, strip=True)

    def stockCidades(self) -> str:
        dados: dict = dict()
        dados['id'] = self.cleaned_data['id']
        dados['nome'] = self.cleaned_data['nome'].title()
        dados['estado'] = self.cleaned_data['estado'].upper()
        checkcity = self.checkCity(dados['nome'])
        if dados['id'] is None:
            if checkcity != '':
                return checkcity
            return Cidades().salveCidade(dados, 'salvar')
        else:
            return Cidades().salveCidade(dados, 'alterar')
    
    def checkCity(self, city:str) -> str:
        id = Cidades.objects.filter(nome=city)
        try:
            id = id[0].id
            return f'Cidade {city}, ja cadastrada com id {id}'
        except:
            return ''


class PagamentosForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    forma = forms.CharField(label='forma', max_length=50)

    def stockPagamento(self) -> str:
        dados: dict = dict()
        dados['id'] = self.cleaned_data['id']
        dados['forma'] = self.cleaned_data['forma'].title()
        checkPay = self.checkPay(dados['forma'])
        if dados['id'] is None:
            if checkPay != '':
                return checkPay
            return Pagamentos().savePagamentos(dados, 'salvar')
        else:
            return Pagamentos().savePagamentos(dados, 'alterar')

    def checkPay(self, pay: str) -> str:
        id = Pagamentos.objects.filter(forma=pay)
        try:
            id = id[0].id
            return f'Pagamento {pay}, já cadastrado com o id {id}!!!'
        except:
            return ''


class NomeViagemForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    nome = forms.CharField(label='nome', max_length=50)
    datai = forms.DateField(label='datai')
    dataf = forms.DateField(label='dataf')
    carro = forms.CharField(label='carro', max_length=7)
    kmvi = forms.IntegerField(label='kmi')
    kmvf = forms.IntegerField(label='kmf')
    user = forms.CharField(label='user', max_length=10)
    atividade = forms.BooleanField(label='atividade', required=False)

    def stockTripName(self):
        id = self.cleaned_data['id']
        self.cleaned_data['nome'] = self.cleaned_data['nome'].title()
        checkTrip = self.checkTripName(self.cleaned_data['nome'])
        if id is None:
            if checkTrip != '':
                return checkTrip
            return NomeViagem().saveNomeViagem(self.cleaned_data, 'salvar')
        else:
            return NomeViagem().saveNomeViagem(self.cleaned_data, 'alterar')
        
    def checkTripName(self, trip: str) -> str:
        id = NomeViagem.objects.filter(nome=trip)
        try:
            id = id[0].id
            return f'Viagem {trip}, já cadastrada com o id = {id}!!!'
        except:
            return ""
    

class TiposForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    tipo = forms.CharField(label='tipo', max_length=20)

    def stockType(self) -> str:
        id = self.cleaned_data['id']
        self.cleaned_data['tipo'] = self.cleaned_data['tipo'].title()
        checkType = self.checkType(self.cleaned_data['tipo'])
        if id is None:
            if checkType != '':
                return checkType
            return Tipos().saveTipos(self.cleaned_data, 'salvar')
        else:
            return Tipos().saveTipos(self.cleaned_data, 'alterar')
        
    def checkType(self, type: str) -> str:
        id = Tipos.objects.filter(tipo= type)
        try:
            id = id[0].id
            return f'Tipod de despesa {type}, já cadastrado com o id = {id}!!!'
        except:
            return ''


class UsuariosForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    nome = forms.CharField(label='nome', max_length=100)
    user = forms.CharField(label='user', max_length=50)
    email = forms.CharField(label='email', max_length=70)
    senha = forms.PasswordInput()

    def stockUser(self):
        print(self.cleaned_data)
