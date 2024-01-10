import xlwt
import datetime as dt
from django.conf import settings
from os import path
from viagem.models import NomeViagem
from io import BytesIO
from django.http import HttpResponse

def createExcell(dados: list) -> HttpResponse:
    nomes = ('id', 'Data', 'Despesa', 'qnt', 'valor', 'Nota', 'Km Inicial','Km Final', 'Km Rodado', 'media', 'Cidade', 'Pagamento')
    work = xlwt.Workbook(encoding='utf-8')
    sheets = work.add_sheet('viagem_1')
    sheets.write(0, 0, 'Data do relatório')
    via = dados[0][0].idnomeviagem
    sheets.write(0, 1, dt.datetime.now().strftime("%d/%m/%Y"))
    sheets.write(0, 3, 'Usuário')
    sheets.write(0, 4, via.usuario.login)
    sheets.write(2, 0, 'Viagem')
    sheets.write(2, 1, 'Carros')
    sheets.write(2, 2, 'km Rodados')
    sheets.write(2, 3, 'Dias')
    sheets.write(3, 0, via.nome)
    sheets.write(3, 1, via.idcarro.placa)
    sheets.write(3, 2, via.kmfinal - via.kminicial)
    sheets.write(3, 3, abs((via.datafinal-via.datainicio).days))
    linha = 6
    for l ,t in enumerate(nomes):
        sheets.write(5, l, t)
    for h, i in enumerate(dados[0]):
        sheets.write(h + linha, 0, i.id)
        sheets.write(h + linha, 1, convertData(i.data))
        sheets.write(h + linha, 2, i.idtipo.tipo)
        sheets.write(h + linha, 3, i.qnt)
        sheets.write(h + linha, 4, i.valor)
        sheets.write(h + linha, 5, i.nota)
        if i.kminicial > 0:
            sheets.write(h + linha, 6, i.kminicial)
            sheets.write(h + linha, 7, i.kmfinal)
            sheets.write(h + linha, 8, i.kmrodado)
            sheets.write(h + linha, 9, i.media)
        if i.idcidade.nome != 'Nenhuma': sheets.write(h + linha, 10, i.idcidade.nome)
        sheets.write(h + linha, 11, i.idpagamento.forma)

    caminho = path.join(settings.MEDIA_ROOT, 'excell/teste.xlm')
    buffer = BytesIO()
    work.save(buffer)
    buffer.seek(0)
    response = HttpResponse(
                                buffer.getvalue(),
                                content_type='application/vnd.ms-excel')
    response["Content-Disposition"] = f'attachment; filename="{via.nome}_{dt.datetime.now().strftime("%d-%m-%Y")}.xls"'
    return response


def convertData(data):
    return data.strftime('%d/%m/%Y')