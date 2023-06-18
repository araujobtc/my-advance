function resultado(){
    var res = document.querySelector('#res')
    var nasc = document.querySelector('#txtano')
    var data = new Date()
    var ano = data.getFullYear()

    if (nasc.value.length == 0 || nasc.value > ano){
        res.innerHTML ='<p style="color: #8f0c04">Ano inválido!</p>'
    }
    else{
        var sex = document.getElementsByName('radsex')
        var idade = ano - Number(nasc.value)
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
       
        if (idade >=0 && idade <10){
            png = 'img/foto-bebe-'
        }
        else if (idade < 21){
            png = 'img/foto-jovem-'
        }
        else if (idade < 50){
            png = 'img/foto-adulto-'
        }
        else{
            png = 'img/foto-idoso-'
        } 

        if (sex[0].checked){
            png += 'm.png'
            res.innerHTML = `<p>Detectamos um homem com ${idade} anos</p>
                            <img src="${png}" alt="${png}">`
        }
        else if (sex[1].checked){
            png += 'f.png'
            res.innerHTML = `<p>Detectamos uma mulher com ${idade} anos</p>
                            <img src="${png}" alt="${png}">`
        }
        else{
            res.innerHTML ='<p style="color: #8f0c04">Selecione um sexo!</p>'
        }
    }
}