from collections.abc import Iterable
from django.db import models
from django.conf import settings
import os
from .image import trataImagem


class Carros(models.Model):
    placa = models.CharField(name='placa', unique=True, max_length=7)
    modelo = models.CharField(name='modelo', max_length=150)

    def salveCarros(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        plac: str = post['placa']
        model: str = post['modelo']
        plac = plac.upper()
        model = model.strip().title()
        try:
            if id != '':
                car = Carros.objects.get(id=id)
                acao = 'alterado'
            else:
                car = Carros()
            car.placa = plac
            car.modelo = model
            car.save()
            return f'Carros {plac}, {acao} com sucesso !!'
        except:
            return 'Dados NÃO salvos!!!'
    
    def getCarros(self):
        try:
            return Carros.objects.all()
        except:
            return list()
    
class Cidades(models.Model):
    nome = models.CharField(name='nome', unique=True ,max_length=100)
    estado = models.CharField(name='estado', max_length=2)

    def salveCidade(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome: str = post['nome']
        estado: str = post['estado']
        nome = nome.title().strip()
        estado = estado.upper().strip()
        testName = self.confirmCidade(nome)
        if testName > 0:
            return f'Cidade {nome}, já cadastrada!!'
        try:
            if id != '':
                cid = Cidades.objects.get(id=id)
                acao = 'alterado'
            else:
                cid = Cidades()
            cid.nome = nome
            cid.estado = estado
            cid.save()
            return f'Cidade {nome}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvos!!!'
    
    def confirmCidade(self, nome) -> int:
        cid = Cidades.objects.filter(nome = nome)
        try:
            id = cid[0].id
            print(id)
            if id == '' or id is None:
                return 0
            else:
                return id
        except:
            return 0
        
    def getCidade(self):
        try:
            return Cidades.objects.all()
        except:
            return list()

class Pagamentos(models.Model):
    forma = models.CharField(name='forma', unique=True, max_length=50)

    def savePagamentos(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        frm = post['tipo']
        frm = frm.strip().title()
        try:
            if id != '':
                pag = Pagamentos.objects.get(id=id)
                acao = 'alterado'
            else:
                pag = Pagamentos()
            pag.forma = frm
            pag.save()
            return f'Forma de pagamento {frm}, {acao} com sucesso!!!'
        except:
            return 'Dados NÂO salvos!!'
    
    def getPagamentos(self):
        try:
            return Pagamentos.objects.all().order_by('id')
        except:
            return list()

class Tipos(models.Model):
    tipo = models.CharField(name='tipo', max_length=50, unique=True)

    def saveTipos(self, request) -> str:
        acao = 'salvo'
        id = request.POST.get('id')
        tp = request.POST.get('tipo')
        tp = tp.strip().title()
        try:
            if id != '':
                tipoid = Tipos.objects.get(id=id)
                acao = 'alterado'
            else:
                tipoid = Tipos()
            tipoid.tipo = tp
            tipoid.save()
                
            return f'Tipos de despesa {tp}, {acao} com sucesso!!'
        except:
             return 'Dados NÂO salvos!!'
        
    def getTipos(self):
        try:
            return Tipos.objects.all().order_by('id')
        except:
            return list()

class Usuario(models.Model):
    nome = models.CharField(name='usuario', max_length=150)
    login = models.CharField(name= 'login', max_length=20)
    senha = models.CharField(name='senha', max_length=15)
    email = models.CharField(name='email', max_length=100)

    def saveUsuarios(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome = post['nome'].title().strip()
        login = post['user'].strip().lower()
        email = post['email'].strip().lower()
        senha = post['senha']
        try:
            if id != '':
                user = Usuario.objects.get(id=id)
                acao = 'alterado'
            else:
                user = Usuario()
            user.usuario = nome
            user.login = login
            user.email = email
            user.senha = senha
            user.save()
            return f'Usuário {login}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvo!!!'
    

    def getUsers(self):
        try:
            return Usuario.objects.all()
        except:
            return list()
        
class NomeViagem(models.Model):
    nome = models.CharField(name='nome', max_length=100)
    datainicio = models.DateField(name='datainicio')
    datafinal = models.DateField(name='datafinal')
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE, name='idcarro')
    kminicial = models.IntegerField(name='kminicial', default=0)
    kmfinal = models.IntegerField(name='kmfinal', default=0)
    usuario = models.ForeignKey(Usuario, name='usuario', on_delete=models.CASCADE)
    atividade = models.BooleanField(name='atividade')

    def saveNomeViagem(self, post: dict) -> str:
        acao = 'salvo'
        id = post['id']
        nome = post['nome']
        nome = nome.strip().title()
        datainicio = post['datai']
        datafim = post['dataf']
        car = post['carro']
        car = Carros.objects.get(id=car)
        kmi = post['kmvi']
        kmf = post['kmvf']
        usuario = Usuario.objects.get(id=post['user'])
        try:
            atv = post['atv']
        except KeyError:
            atv = 0
        try:
            if id != '':
                nomev = NomeViagem.objects.get(id=id)
                acao = 'alterado'
            else:
                nomev = NomeViagem()
            nomev.nome = nome
            nomev.datainicio = datainicio
            nomev.datafinal = datafim
            nomev.idcarro = car
            nomev.kminicial = kmi
            nomev.kmfinal = kmf
            nomev.usuario = usuario
            nomev.atividade = atv
            nomev.save()
            return f'Viagem {nome}, {acao} salvo com sucesso!!'
        except:
            return 'Dados NÂO salvos!!'
        
    def getNomeViagem(self):
        try:
            return NomeViagem.objects.all()
        except:
            return list()
        
    def getNomesAtivos(self):
        try:
            return NomeViagem.objects.filter(atividade=True)
        except:
            return list()
    
    def countAtividade(self) -> dict:
        atv = self.getNomeViagem()
        if atv == []:
            return 'Sem Viagens ativas!!!'
        else:
            res = atv.filter(atividade=True)
            res1 = res.count()
            if res1  == 0:
                return {'n': 'Não possue viagem ativa, cadastre uma viagem para iniciar!!!'}
            elif res1 > 1:
                return {'n': 'Muitas viagens ativas, desative viagens para continuar!!!'}
            else:    
                return {'1': [str(res[0].id), res[0].nome]}
    
    def alterKmFinal(id: int, kmfinal: int):
        viagem = NomeViagem.objects.get(id = id)
        viagem.kmfinal = kmfinal
        viagem.save()

class Despesas(models.Model):
    nomeviagem = models.ForeignKey(NomeViagem, name='idnomeviagem', on_delete=models.CASCADE)
    data = models.DateField(name='data')
    tipo = models.ForeignKey(Tipos, name='idtipo', on_delete=models.CASCADE)
    qnt = models.DecimalField(name='qnt',decimal_places=2, max_digits=10)
    valor = models.DecimalField(name='valor', decimal_places=2, max_digits=10)
    nota = models.IntegerField(name='nota', unique=True)
    kminicial = models.IntegerField(name='kminicial')
    kmfinal = models.IntegerField(name='kmfinal')
    kmrodado = models.IntegerField(name='kmrodado')
    media = models.DecimalField(name='media', decimal_places=2, max_digits=10)
    cidade = models.ForeignKey(Cidades, name='idcidade', on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamentos, name='idpagamento', on_delete=models.CASCADE)
    imagemnota = models.FileField(upload_to='notas', name='imagemnota', null=True, default='nada')

    def saveDespesa(self, post: dict, file:dict):
        bt = post['bt']
        id  = post['id']
        if str(bt) == '1':
            acao = 'salvo'
            viagem = NomeViagem.objects.get(id=post['nome-viagem'])
            data = post['data']
            tipo = Tipos.objects.get(id=post['tipo'])
            qnt = post['qnt']
            valor = post['valor']
            nota = post['nota']
            kmi = post['kmi']
            kmf = post['kmf']
            kmr = post['kmr']
            consumo = post['consumo']
            cidade = Cidades.objects.get(id=post['cidade'])
            pg = Pagamentos.objects.get(id=post['pg'])
            try:
                image = file['imagem']
            except:
                image = ''
            try:
                if id != '':
                    dados = Despesas.objects.get(id = id)
                    acao = 'Alterado'
                    self.confereNota(image, dados.imagemnota)
                else:
                    dados = Despesas()
                dados.idnomeviagem = viagem
                dados.data = data
                dados.idtipo = tipo
                dados.qnt = qnt
                dados.valor = valor
                dados.nota = nota
                dados.kminicial = kmi
                dados.kmfinal = kmf
                dados.kmrodado = kmr
                dados.media = consumo
                dados.idcidade = cidade
                dados.idpagamento = pg
                if image != "" : 
                    dados.imagemnota = image
                dados.save()
                if image != "" : 
                    image = trataImagem(str(image))
                if int(kmf) > 0 and id == "": 
                    viagem.kmfinal = kmf
                viagem.save()
                return f'Despesa {tipo.tipo}, {acao} com sucesso!!!'
            except:
                return 'Dados NÂO salvos!!!'
        elif str(bt) == '3':
            return 'Formulario limpo!!'
        else:
            return self.dropDespesa(id)
    
    def getDespesas(self):
        try:
            viagem = NomeViagem().getNomesAtivos()
            return Despesas.objects.all().filter(idnomeviagem=viagem[0].id).order_by('data', 'idtipo')
        except:
            return list()

    def dropDespesa(self, id):
        try:
            desp = Despesas.objects.get(id=id)
            image = desp.imagemnota
            image = str(image).replace('/','\\')
            os.remove(os.path.join(settings.MEDIA_ROOT, str(image)))
            desp.delete()
            return f'Despesa de ID = {id}, deletado com sucesso!!!'
        except:
            return 'Despesa NÂO deletada!!'
    
    def lastKm(self):
        viagem = NomeViagem().getNomesAtivos()
        vg = viagem[0].id
        dados = self.getDespesas()
        dados = dados.filter(idnomeviagem=vg, idtipo=5)
        dados = dados.aggregate(max_km=models.Max('kmfinal'))
        try: 
            return dados['max_km']
        except:
            vg = viagem[0].kminicial
            return vg
    
    def relDespesas(self, request) -> list:
        id = request.POST.get('nomev')
        data = request.POST.get('data')
        tipo = request.POST.get('tipo')
        pg = request.POST.get('pagamento')
    
        despesas = Despesas.objects.filter(idnomeviagem=id).order_by('data', 'idtipo')
        if tipo is None and data == '' and pg is not None:
            despesas = despesas.filter(idpagamento = pg)
        elif data != '' and tipo is None and pg is None:
            despesas = despesas.filter(data = data)
        elif data == '' and tipo is not None and pg is None:
            despesas = despesas.filter(idtipo = tipo)
        elif data != '' and tipo is not None and pg is None:
            despesas = despesas.filter(idtipo = tipo, data = data)
        elif data != "" and tipo is None and pg is not None:
            despesas = despesas.filter(data = data, idpagamento=pg)
        elif data != "" and tipo is not None and pg is not None:
            despesas = despesas.filter(data = data, idtipo = tipo, idpagamento=pg)
        elif data == "" and tipo is not None and pg is not None:
            despesas = despesas.filter(idtipo = tipo, idpagamento=pg)
        totalv = despesas.aggregate(total=models.Sum('valor'))
        adiantamento = despesas.filter(idtipo = 7)
        adiantamento = adiantamento.aggregate(adian = models.Sum('valor'))
        try:
            adiantamento = adiantamento['adian']
            total = float(totalv['total']) - float(adiantamento)
            return [despesas, round(total,2), adiantamento]
        except: 
            total = totalv['total']
            adiantamento = 0
        try:
           return [despesas, round(total,2), adiantamento]
        except:
            return [despesas, 0, 0] 

    def confereNota(self, ima, imagem):
        image = str(ima)
        try:
            imagem1 = str(imagem).split('/')[1]
        except:
            imagem1 = 'nada'
        if image != imagem1 and imagem1 != 'nada':
            imagem1 = imagem1.replace('/','\\')
            try:
                os.remove(os.path.join(settings.MEDIA_ROOT, str(imagem)))
            except:
                pass
    
    def resumoDespes(self, viagem):
        des = Despesas.objects.filter(idnomeviagem=viagem)
        des_soma = des.values('idtipo__tipo').annotate(soma_qnt = models.Sum('qnt') ,
                                                       soma_valor = models.Sum('valor'))
        for a, i in enumerate(des_soma):
            if float(i['soma_qnt']) != 0.00:
                valor = float(i['soma_valor'])
                qnt = float(i['soma_qnt'])
                media = valor / qnt
                des_soma[a]['media'] = round(media, 2)    
        return  des_soma
    
    def resumoPagamento(self, viagem):
        pag = Despesas.objects.filter(idnomeviagem=viagem)
        lista = list()
        for i in Tipos().getTipos():
            despesa = dict()
            pag_des = pag.filter(idtipo__tipo=i.tipo)
            pag_des = pag_des.values('idpagamento__forma').annotate(soma=models.Sum('valor'))
            despesa[i.tipo] = pag_des
            lista.append(despesa)
        return lista
    