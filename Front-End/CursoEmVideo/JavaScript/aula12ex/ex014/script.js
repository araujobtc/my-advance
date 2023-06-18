var agora = new Date()
var hora = 0
var minutos = agora.getMinutes()
var img = document.querySelector('#foto')
var msg = document.querySelector('#msg')
var body = document.querySelector('body')

function carregar(){
    if (minutos<10) minutos = '0'+minutos
    if (hora<10) hora = '0'+hora
    msg.innerHTML =`<h2>Agora são ${hora}:${minutos}</h2>`

    if (hora >=20 || hora < 5){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/3e/11/5b/3e115bc78dd432515c2b0d1f60c0f4ad.jpg" alt="anoitecer">'
        document.body.style.background = '#0a0a14'
    }
    else if (hora < 8){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/24/ee/f5/24eef5e0b71428e2a3309b3e1f47c47d.jpg" alt="amanhecer">'
        document.body.style.background = '#516477'
    }
    else if(hora < 12){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/f4/59/ae/f459ae443e0082cea572303e13e3a9ee.jpg" alt="amanhecer">'
        document.body.style.background = '#5183a0'
    }
    else if (hora < 15){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/86/28/d4/8628d42dcfb36a027feaf43a390a3bc4.jpg" alt="meio-dia">'
        document.body.style.background = '#73adb8'
    }
    else if (hora < 17){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/74/82/92/748292d13a9b817eb134c7a719be7ff4.jpg" alt="entardecer">'
        document.body.style.background = '#dda463'
    }
    else if (hora < 20){
        img.innerHTML = '<img id="imagem" src="https://i.pinimg.com/564x/f9/8d/2e/f98d2efd794668a43570ad1bafd0e826.jpg" alt="entardecer">'
        document.body.style.background = '#3e4ea5'
    }
}
