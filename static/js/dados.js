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
    var qnt = document.getElementById('qnt');
    if (despesa.value == '5'){
        forKM();
        forKMf();
        forKMr();
        forConsumo();
        document.getElementById("kmi").value = km;
        document.getElementById("divcidade").classList = "col-md-4";
        qnt.readOnly = false;
        qnt.value = ''
    }else{
        try{
            clearKm()
        }catch{
            
        }
        document.getElementById("divcidade").classList = "col-md-6";
        if (despesa.value == '4' || despesa.value == '7'){
            qnt.value = '0';
            qnt.readOnly = true;
        }else{
            qnt.value = '';
            qnt.readOnly = false;
        };
    };
};

function forKM(){
    var divkmi = document.createElement("div");
    divkmi.id = "divkmi"
    var labelkmi = document.createElement("label");
    var kmi = document.createElement("input");
    divkmi.classList  = "col-md-2";
    labelkmi.classList = "form-label";
    labelkmi.textContent = "KM Inicial";
    kmi.classList = "form-control";
    kmi.type = "number";
    kmi.name = "kmi";
    kmi.id = "kmi";
    kmi.required = true;
    divkmi.appendChild(labelkmi);
    divkmi.appendChild(kmi);
    var form = document.querySelector("#form");
    var referencia = document.querySelector("#divcidade");
    form.insertBefore(divkmi, referencia);

};

function forKMf(){
    var divkmf = document.createElement("div");
    divkmf.id = "divkmf";
    var labkmf = document.createElement("label");
    var kmf = document.createElement("input");
    divkmf.classList  = "col-md-2";
    labkmf.classList = "form-label";
    labkmf.textContent = "KM Final";
    kmf.classList = "form-control";
    kmf.id = "kmf";
    kmf.name = "kmf";
    kmf.type = "number";
    kmf.required = true;
    kmf.addEventListener("change", somarkm)
    divkmf.appendChild(labkmf);
    divkmf.appendChild(kmf);
    var form = document.querySelector("#form");
    var referencia = document.querySelector("#divcidade");
    form.insertBefore(divkmf, referencia);
};

function forKMr(){
    var divkmr = document.createElement("div");
    divkmr.id = "divkmr";
    var labkmr = document.createElement("label");
    var kmr = document.createElement("input");
    divkmr.classList  = "col-md-2";
    labkmr.classList = "form-label";
    labkmr.textContent = "Km Rodado";
    kmr.classList = "form-control";
    kmr.name = "kmr";
    kmr.id = "kmr";
    kmr.type = "number";
    kmr.readOnly = true;
    divkmr.appendChild(labkmr);
    divkmr.appendChild(kmr);
    var form = document.querySelector("#form");
    var referencia = document.querySelector("#divcidade");
    form.insertBefore(divkmr, referencia);
};

function forConsumo(){
    var divcons = document.createElement("div");
    divcons.id = "divcons";
    var labcons = document.createElement("label");
    var cons = document.createElement("input");
    divcons.classList  = "col-md-2";
    labcons.classList = "form-label";
    labcons.textContent = "Consumo";
    cons.classList = "form-control";
    cons.id = "media";
    cons.name = "media";
    cons.type = "number";
    cons.readOnly = true;
    divcons.appendChild(labcons);
    divcons.appendChild(cons);
    var form = document.querySelector("#form");
    var referencia = document.querySelector("#divcidade");
    form.insertBefore(divcons, referencia);
};

function clearKm(){
    document.getElementById("divkmi").remove();
    document.getElementById("divkmf").remove();
    document.getElementById("divkmr").remove();
    document.getElementById("divcons").remove();
};

function alterDespesa(id, viagem, tipo, data, qnt, valor, nota, kmi, kmf, kmr, media, cid, pag){
    var data1 = data.split("/");
    var res  = data1[2] + '-' + data1[1] + '-' + data1[0];
    var tipos = document.getElementById('tipo')
    qnt = qnt.replace(',', '.')
    valor = valor.replace(',', '.')
    media = media.replace(',', '.')
    document.getElementById('id').value = id;
    document.getElementById('nome_viagem').value = viagem;
    tipos.value = tipo;
    document.getElementById('data').value = res;
    document.getElementById('qnt').value = parseFloat(qnt);
    document.getElementById('valor').value = parseFloat(valor);
    document.getElementById('nota').value = nota;
    if (tipo == 5){
        despesa(0)
        document.getElementById('kmi').value = kmi;
        document.getElementById('kmf').value = kmf;
        document.getElementById('kmr').value = kmr;
        document.getElementById('media').value = parseFloat(media);
    };
    document.getElementById('cidade').value = cid;
    document.getElementById('pg').value = pag;
    document.getElementById('bt-del').disabled = false;
    voltarAoTopo();
};


