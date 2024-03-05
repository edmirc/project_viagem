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
        document.getElementById('media').value = media.toFixed(2);
        document.getElementById('cidade').focus();
    };
    
};

function voltarAoTopo() {
    window.scrollBy(0, -window.innerHeight);
};

function despesa(km){
    var despesa = document.getElementById('tipo');
    var cidade = document.getElementById('cidade');
    var qnt = document.getElementById('qnt');
    if (despesa.value == '5'){
        forKM();
        forKMf();
        forKMr();
        forConsumo();
        document.getElementById("kmi").value = km;
    }else{
        clearKm()
        if (despesa.value == '4' || despesa.value == '7'){
            var qnt = document.getElementById('qnt'); 
            qnt.value = '0';
            qnt.readOnly = true;
        }else{
            qnt.value = '';
            qnt.readOnly = false;
        };
        cidade.value = '1';
    };
};

function forKM(){
    var divkmi = document.getElementById("divkmi");
    var labelkmi = document.createElement("label");
    var kmi = document.createElement("input");
    labelkmi.classList = "form-label";
    labelkmi.textContent = "KM Inicial";
    kmi.classList = "form-control";
    kmi.type = "number";
    kmi.name = "kmi";
    kmi.id = "kmi";
    divkmi.appendChild(labelkmi)
    divkmi.appendChild(kmi)
};

function forKMf(){
    var divkmf = document.getElementById("divkmf");
    var labkmf = document.createElement("label");
    var kmf = document.createElement("input");
    labkmf.classList = "form-label";
    labkmf.textContent = "KM Final";
    kmf.classList = "form-control";
    kmf.id = "kmf";
    kmf.name = "kmf";
    kmf.type = "number";
    kmf.addEventListener("change", somarkm)
    divkmf.appendChild(labkmf);
    divkmf.appendChild(kmf);
};

function forKMr(){
    var divkmr = document.getElementById("divkmr");
    var labkmr = document.createElement("label");
    var kmr = document.createElement("input");
    labkmr.classList = "form-label";
    labkmr.textContent = "Km Rodado";
    kmr.classList = "form-control";
    kmr.name = "kmr";
    kmr.id = "kmr";
    kmr.type = "number";
    kmr.readOnly = true;
    divkmr.appendChild(labkmr);
    divkmr.appendChild(kmr);
};

function forConsumo(){
    var divkmf = document.getElementById("divcons");
    var labcons = document.createElement("label");
    var cons = document.createElement("input");
    labcons.classList = "form-label";
    labcons.textContent = "Consumo";
    cons.classList = "form-control";
    cons.id = "media";
    cons.name = "media";
    cons.type = "number";
    cons.readOnly = true;
    divcons.appendChild(labcons);
    divcons.appendChild(cons);
};

function clearKm(){
    document.getElementById("divkmi").innerHTML = "";
    document.getElementById("divkmf").innerHTML = "";
    document.getElementById("divkmr").innerHTML = "";
    document.getElementById("divcons").innerHTML = "";
};

function alterDespesa(id, viagem, tipo, data, qnt, valor, nota, kmi, kmf, kmr, media, cid, pag){
    var data1 = data.split("/");
    var res  = data1[2] + '-' + data1[1] + '-' + data1[0];
    qnt = qnt.replace(',', '.')
    valor = valor.replace(',', '.')
    media = media.replace(',', '.')
    document.getElementById('id').value = id;
    document.getElementById('nome_viagem').value = viagem;
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


