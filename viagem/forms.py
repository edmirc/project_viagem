from django import forms
from .models import *
from .util.excell import createExcell


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
    atividade = forms.BooleanField(label='labelatividade', required=False)

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
    senha = forms.CharField(label='senha', max_length=5, widget=forms.PasswordInput(),required=False)

    def stockUser(self) -> str:
        id = self.cleaned_data['id']
        self.cleaned_data['nome'] = str(self.cleaned_data['nome']).title()
        self.cleaned_data['email'] = str(self.cleaned_data['email']).lower()
        checkUser = self.checkUser(self.cleaned_data['user'])
        if id is None:
            if checkUser != '':
                return checkUser
            if self.cleaned_data['senha'] == "":
                return 'Senha inválida!!'
            return Usuario().saveUsuarios(self.cleaned_data, 'salvar')
        else:
            return Usuario().saveUsuarios(self.cleaned_data, 'alterar')

    def checkUser(self, user: str) -> str:
        id = Usuario.objects.filter(login = user)
        try:
            id = id[0].id
            return f'Login {user}, já cadastrado com o id = {id}!!'
        except:
            return ''


class RelatoriosForm(forms.Form):
    nomev = forms.CharField(label='nome', max_length=50)
    data = forms.DateField(label='data', required=False)
    tipo = forms.IntegerField(label='tipo', required=False)
    pagamento = forms.IntegerField(label='pagamento', required=False)
    bt = forms.CharField(label='bt')

    def resultRel(self) -> list:
        botao = self.cleaned_data['bt']
        return botao
    
    def resultBtSend(self) -> list:
        despesa: list = Despesas().relDespesas(self.cleaned_data)
        return despesa
    
    def resultBtExcell(self) -> list:
        despesa: list = Despesas().relDespesas(self.cleaned_data)
        return createExcell(despesa)
    

class DespesasForm(forms.Form):
    id = forms.IntegerField(label='id', required=False)
    nome_viagem = forms.CharField(label='nome_viagem')
    data = forms.DateField(label='data')
    tipo = forms.CharField(label='tipo')
    qnt = forms.DecimalField(label='qnt', max_digits=10, decimal_places=2)
    valor = forms.DecimalField(label='valor', max_digits=10, decimal_places=2)
    nota = forms.IntegerField(label='nota')
    kmi = forms.IntegerField(label='kmi')
    kmf = forms.IntegerField(label='kmf')
    kmr = forms.IntegerField(label='kmr')
    consumo = forms.DecimalField(label='consumo', decimal_places=2, max_digits=10)
    cidade = forms.CharField(label='cidade')
    pg = forms.CharField(label='pg')
    imagem = forms.FileField(label='imagem', required=False)
    bt = forms.CharField(label='bt')

    def stockExpenses(self):
        id =  self.cleaned_data['id']
        if id is None:
            return Despesas().saveDespesa(self.cleaned_data, 'salvar')
        else:
           return Despesas().saveDespesa(self.cleaned_data, 'alterar')
        

class ResumoForm(forms.Form):
    viagem = forms.CharField(label='viagem')

    def summaryReport(self) -> dict:
        dados: dict = dict()
        dados['soma'] = Despesas().resumoDespes(self.cleaned_data['viagem'])
        dados['pg'] = ''
        formas: dict = dict()
        formas['total'] = 'Total'
        for i in Pagamentos().getPagamentos():
            formas[i.forma] = 0.0 
        tipos = Tipos().getTipos()
        pg  = Despesas().resumoPagamento(self.cleaned_data['viagem'])
        lista1: list = list()
        for l,i in enumerate(tipos):
            lista: list = list()
            lista.append(i.tipo)
            soma = 0
            for k, m in enumerate(formas.keys()):
                if k > 0:
                    try:
                        pagamento = pg[l][i.tipo][m]
                        lista.append(pagamento)
                        soma += pagamento
                        soma1 = formas[m]
                        formas[m] = round(soma1 + float(pagamento),2)
                    except:
                        lista.append(0.0) 
            lista.append(soma)
            lista1.append(lista)
        lista1.append([h  for h in formas.values()])
        dados['pg'] = lista1 
        return dados
