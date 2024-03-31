


function tipoRelatorio(tipos, pagamentos){
    let tipo = document.getElementById("relatorio").value;
    dropElementos(tipos, pagamentos)
    let viagem = document.querySelector("#nomev");
    if (tipo != 1){
        viagem.required = false
        viagem.disabled = true
        viagem.value = ""
    };
    if (tipo == 1){
        viagem.required = true
        viagem.disabled = false
    }else if (tipo == 2){
        tipoData();
    }else if (tipo == 3){
        tipoPeriodo();
    }else if (tipo == 4){
        tema("Despesas")
        tipoTipo(tipos);
    }else if (tipo == 5){
        tema("Pagamentos")
        tipoTipo(pagamentos);
    }else if (tipo == 6){
        tipoPeriodo();
        tema("Despesas")
        tipoTipo(tipos);
    }else if (tipo == 7){
        tipoPeriodo();
        tema("Pagamentos")
        tipoTipo(pagamentos);
    };
}

function dropElementos(tipos, pagamentos){
    let data = document.getElementById("divData")
    let divInicio = document.getElementById("divInicio")
    let divFim = document.getElementById("divFinal")
    let divTema = document.getElementById("divTema")
    if (data && data.parentNode){
        data.parentNode.removeChild(data)
    };
    if (divInicio && divInicio.parentNode){
        divInicio.parentNode.removeChild(divInicio)
    };
    if (divFim && divFim.parentNode){
        divFim.parentNode.removeChild(divFim)
    };
    if (divTema && divTema.parentNode){
        divTema.parentNode.removeChild(divTema)
    };
    for (let i of tipos){
        let divTipo  = document.getElementById(i)
        if (divTipo && divTipo.parentNode){
            divTipo.parentNode.removeChild(divTipo)
        };
    };
    for (let i of pagamentos){
        let divPg  = document.getElementById(i)
        if (divPg && divPg.parentNode){
            divPg.parentNode.removeChild(divPg)
        };
    };
}

function tipoData(){
    let divData = document.createElement("div");
    let form = document.querySelector("#formRel");
    divData.classList = "col-md-4";
    divData.id = "divData"
    let lebalData = document.createElement("label");
    lebalData.classList = "form-label";
    lebalData.textContent = "Data";
    let inputData = document.createElement("input");
    inputData.type = "date";
    inputData.classList = "form-control"
    inputData.id = "data";
    inputData.name = "data";
    inputData.required = true;
    divData.appendChild(lebalData);
    divData.appendChild(inputData);
    let referencia = document.querySelector("#divBotoes");
    form.insertBefore(divData, referencia);
};

function tipoPeriodo(){
    let form = document.querySelector("#formRel");
    let referencia = document.querySelector("#divBotoes");
    let divInicio = document.createElement("div");
    divInicio.id = "divInicio";
    divInicio.classList = "col-md-6";
    let divFinal = document.createElement("div");
    divFinal.id = "divFinal";
    divFinal.classList = "col-md-6";
    let labelInicio = document.createElement("label");
    labelInicio.classList = "form-label";
    labelInicio.textContent = "Data de Inicio";
    let labelFinal = document.createElement("label");
    labelFinal.classList = "form-label";
    labelFinal.textContent = "Data do Fim";
    let inputInico = document.createElement("input");
    inputInico.classList = "form-control";
    inputInico.id = "dataInicio";
    inputInico.name = "dataInicio";
    inputInico.type = "date";
    inputInico.required = true;
    let inputFinal = document.createElement("input");
    inputFinal.classList = "form-control";
    inputFinal.id = "dataFinal";
    inputFinal.name = "dataFinal";
    inputFinal.type = "date";
    inputFinal.required = true;
    divInicio.appendChild(labelInicio);
    divInicio.appendChild(inputInico);
    divFinal.appendChild(labelFinal);
    divFinal.appendChild(inputFinal);
    form.insertBefore(divInicio, referencia);
    form.insertBefore(divFinal, referencia);
};

function tipoTipo(tipos){
    var cont = 1
    let referencia = document.querySelector("#divBotoes")
    let form = document.querySelector("#formRel")
    for (const item of tipos){
        let div = document.createElement("div")
        div.classList = "col-md-4"
        div.id = item
        let ul = document.createElement("ul")
        ul.classList = "list-group"
        let li = document.createElement("li")
        li.classList = "list-group-item"
        let input = document.createElement("input")
        let label = document.createElement("label")
        input.type = "radio"
        input.classList = "form-check-input me-1"
        input.name = "tipo"
        input.id = "radio"
        input.value = cont
        label.textContent = item
        label.classList = "form-check-label"
        cont = cont + 1
        li.appendChild(input)
        li.appendChild(label)
        ul.appendChild(li)
        div.appendChild(ul)
        form.insertBefore(div, referencia)
    }
};

function tema(tema){
    let referencia = document.querySelector("#divBotoes")
    let form = document.querySelector("#formRel")
    let divTema = document.createElement("div")
    divTema.id = "divTema"
    divTema.classList = "col-md-12"
    let titulo = document.createElement("h4")
    titulo.textContent = tema
    divTema.appendChild(titulo)
    form.insertBefore(divTema, referencia)
}
