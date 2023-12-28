function alterarNome(id, nome, carro, kmi, kmf,user, datai, dataf){

      // Preencher os campos de input com os dados da linh
    var partesi = datai.split("/");
    var partesf = dataf.split("/");
    var novaDatai = partesi[2] + "-" + partesi[1] + "-" + partesi[0];
    var novaDataf = partesf[2] + "-" + partesf[1] + "-" + partesf[0];

    document.getElementById('id').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('carro').value =  carro;
    document.getElementById('kmvi').value =  kmi;
    document.getElementById('kmvf').value =  kmf;
    document.getElementById('user').value =  user;
    document.getElementById('datai').value =  novaDatai;
    document.getElementById('dataf').value = novaDataf;
      // Adicione mais campos de input conforme necessário
    };


function alterCarro(id, placa, modelo){

    // Preencher os campos de input com os dados da linh
    document.getElementById('id').value = id;
    document.getElementById('placa').value = placa;
    document.getElementById('modelo').value = modelo;
    // Adicione mais campos de input conforme necessário
    };


function alterCidade(id, nome, estado){
    document.getElementById('id').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('estado').value = estado;
};


function alterTipo(id, tipo){
    document.getElementById('id').value = id;
    document.getElementById('tipo').value = tipo;
};


function alterPg(id, tipo){
    document.getElementById('id').value = id;
    document.getElementById('tipo').value = tipo;
};


function atividade(){
    var labe = document.getElementById('ativi');
    var inp = document.getElementById('atv');
    if (inp.checked){
        labe.textContent = 'Ativo';

    }else{
        labe.textContent = 'Inativo';
    };
};

function alterUser(id, nome, user, email){
    document.getElementById('id').value = id
    document.getElementById('nome').value = nome;
    document.getElementById('user').value = user;
    document.getElementById('email').value = email;
};

