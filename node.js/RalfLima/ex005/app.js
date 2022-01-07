// importar o express
var express = require('express')

// criando variavel para ter acesso as funconalidades do express
var app = express();

// rota
app.get('/', function(req, res){
    res.write('Utilizando o express');
    res.end();
});

// servidor
app.listen(8080);
