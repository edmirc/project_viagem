from collections.abc import Iterable
from typing import Any
from django.db import models
from django.conf import settings
import os
from .util.image import trataImagem


class Carros(models.Model):
    placa = models.CharField(name='placa', unique=True, max_length=7)
    modelo = models.CharField(name='modelo', max_length=150)

    def salveCarros(self, post: dict, acao: str) -> str:
        try:
            if acao == 'alterar':
                car = Carros.objects.get(id=post['id'])
            else:
                car = Carros()
            car.placa = post['placa']
            car.modelo = post['modelo']
            car.save()
            return f'Carros {car.placa}, {acao} com sucesso !!'
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

    def salveCidade(self, post: dict, acao: str) -> str:
        try:
            if acao == 'alterar':
                cid = Cidades.objects.get(id=post['id'])
            else:
                cid = Cidades()
            cid.nome = post['nome']
            cid.estado = post['estado']
            cid.save()
            return f'Cidade {cid.nome}, {acao} com sucesso!!'
        except:
            return 'Dados NÃO salvos!!!'
        
    def getCidade(self):
        try:
            return Cidades.objects.all().order_by('nome')
        except:
            return list()

class Pagamentos(models.Model):
    forma = models.CharField(name='forma', unique=True, max_length=50)

    def savePagamentos(self, post: dict, acao: str) -> str:
        print(post, acao)
        try:
            if acao == 'alterar':
                pag = Pagamentos.objects.get(id=post['id'])
            else:
                pag = Pagamentos()
            pag.forma = post['forma']
            pag.save()
            return f'Forma de pagamento {pag.forma}, {acao} com sucesso!!!'
        except:
            return 'Dados NÂO salvos!!'
    
    def getPagamentos(self):
        try:
            return Pagamentos.objects.all().order_by('forma')
        except:
            return list()

class Tipos(models.Model):
    tipo = models.CharField(name='tipo', max_length=50, unique=True)

    def saveTipos(self, post: dict, acao: str) -> str:
        try:
            if acao == 'alterar':
                tipoid = Tipos.objects.get(id=post['id'])
            else:
                tipoid = Tipos()
            tipoid.tipo = post['tipo']
            tipoid.save()
                
            return f'Tipos de despesa {tipoid.tipo}, {acao} com sucesso!!'
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

    def saveUsuarios(self, post: dict, acao: str) -> str:
        try:
            if acao == 'alterar':
                user = Usuario.objects.get(id=post['id'])
                if post['senha'] != '':
                    user.senha = post['senha']
            else:
                user = Usuario()
                user.senha = post['senha']
            user.usuario = post['nome']
            user.login = post['user']
            user.email = post['email']
            user.save()
            return f'Usuário {user.login}, {acao} com sucesso!!'
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

    def saveNomeViagem(self, post: dict, acao: str) -> str:
        try:
            if acao == 'alterar':
                nomev = NomeViagem.objects.get(id=post['id'])
            else:
                nomev = NomeViagem()
            nomev.nome = post['nome']
            nomev.datainicio = post['datai']
            nomev.datafinal = post['dataf']
            nomev.idcarro = Carros.objects.get(id=post['carro'])
            nomev.kminicial = post['kmvi']
            nomev.kmfinal = post['kmvf']
            nomev.usuario = Usuario.objects.get(id=post['user'])
            nomev.atividade = post['atividade']
            nomev.save()
            return f'Viagem {nomev.nome}, {acao} salvo com sucesso!!'
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

    def saveDespesa(self, post: dict, acao: str):
        bt = post['bt']
        if bt == '1':
            try:
                if acao == 'alterar':
                    dados = Despesas.objects.get(id = post['id'])
                    if post['imagem'] is not None:
                        self.confereNota(post['imagem'], dados.imagemnota)
                else:
                    dados = Despesas()
                dados.idnomeviagem = NomeViagem.objects.get(id=post['nome_viagem'])
                dados.data = post['data']
                dados.idtipo = Tipos.objects.get(id=post['tipo'])
                dados.qnt = post['qnt']
                dados.valor = post['valor']
                dados.nota = post['nota']
                dados.kminicial = post['kmi']
                dados.kmfinal = post['kmf']
                dados.kmrodado = post['kmr']
                dados.media = post['consumo']
                dados.idcidade = Cidades.objects.get(id=post['cidade'])
                dados.idpagamento = Pagamentos.objects.get(id=post['pg'])
                if post['imagem'] is not None : 
                    dados.imagemnota = post['imagem']
                dados.save()
                if post['imagem'] is not None: 
                    trataImagem(str(post['imagem']))
                if int(post['kmf']) > 0 and id is None:
                    viagem = NomeViagem.objects.get(id=post['nome_viagem']) 
                    viagem.kmfinal = post['kmf']
                    viagem.save()
                return f'Despesa {dados.idtipo.tipo}, {acao} com sucesso!!!'
            except:
                return 'Dados NÂO salvos!!!'
        elif str(bt) == '3':
            return 'Formulario limpo!!'
        else:
            return self.dropDespesa(post['id'])
    
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
    
    def relDespesas(self, post: dict) -> list:
        id = post['nomev']
        data = post['data']
        tipo = post['tipo']
        pg = post['pagamento']
        print(post)
        despesas = Despesas.objects.filter(idnomeviagem=id).order_by('data', 'idtipo')
        if tipo is None and data is None and pg is not None:
            despesas = despesas.filter(idpagamento = pg)
        elif data is not None and tipo is None and pg is None:
            despesas = despesas.filter(data = data)
        elif data is None and tipo is not None and pg is None:
            despesas = despesas.filter(idtipo = tipo)
        elif data is not None and tipo is not None and pg is None:
            despesas = despesas.filter(idtipo = tipo, data = data)
        elif data is not None and tipo is None and pg is not None:
            despesas = despesas.filter(data = data, idpagamento=pg)
        elif data is not None and tipo is not None and pg is not None:
            despesas = despesas.filter(data = data, idtipo = tipo, idpagamento=pg)
        elif data is None and tipo is not None and pg is not None:
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
    