function somarkm(){
    var kmi = document.getElementById('kmi');
    var kmf = document.getElementById('kmf');
    var qnt = document.getElementById('qnt');
    var kmr = document.getElementById('kmr');
    if (qnt.value == ""){
        alert('Quantidade deve ser preenchida!!');
        kmf.value = "";
        qnt.focus();
    }else{
        kmr.value = parseInt(kmf.value) - parseInt(kmi.value);
        var media = parseFloat(kmr.value) / parseFloat(qnt.value)
        document.getElementById('consumo').value = media.toFixed(2);
        document.getElementById('cidade').focus();
    };
    
};

function voltarAoTopo() {
    window.scrollBy(0, -window.innerHeight);
};

function despesa(km){
    var despesa = document.getElementById('tipo');
    var kmi = document.getElementById('kmi');
    var kmf = document.getElementById('kmf');
    var kmr = document.getElementById('kmr');
    var consumo = document.getElementById('consumo');
    var cidade = document.getElementById('cidade');
    var qnt = document.getElementById('qnt');
    if (despesa.value == '5'){
        kmi.value = km;
        kmf.value = '';
        kmr.value = '';
        consumo.value = '';
        qnt.value = '';
        cidade.value = '';
        kmi.readOnly = false;
        kmf.readOnly = false;
        qnt.readOnly = false;
    }else{
        if (despesa.value == '4' || despesa.value == '7'){
            var qnt = document.getElementById('qnt'); 
            qnt.value = '0';
            qnt.readOnly = true;
        }else{
            qnt.value = '';
            qnt.readOnly = false;
        };
        kmi.value = 0;
        kmf.value = 0;
        kmr.value = 0;
        consumo.value = 0;
        cidade.value = '1';
        kmi.readOnly = true;
        kmf.readOnly = true;
    };
};

function alterDespesa(id, viagem, tipo, data, qnt, valor, nota, kmi, kmf, kmr, media, cid, pag){
    var data1 = data.split("/");
    var res  = data1[2] + '-' + data1[1] + '-' + data1[0];
    document.getElementById('id').value = id;
    document.getElementById('nome-viagem').value = viagem;
    document.getElementById('tipo').value = tipo;
    document.getElementById('data').value = res;
    document.getElementById('qnt').value = parseFloat(qnt);
    document.getElementById('valor').value = parseFloat(valor);
    document.getElementById('nota').value = nota;
    document.getElementById('kmi').value = kmi;
    document.getElementById('kmf').value = kmf;
    document.getElementById('kmr').value = kmr;
    document.getElementById('consumo').value = parseFloat(media);
    document.getElementById('cidade').value = cid;
    document.getElementById('pg').value = pag;
    document.getElementById('bt-del').disabled = false;
    voltarAoTopo();
};


