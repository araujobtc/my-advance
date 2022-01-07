// express
var express = require('express');

// BodyParser
var bodyParser = require('body-parser');

// App
var app = express();

// configurar o BodyParser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

// Rotas
app.get('/', function(req, res){
    res.sendFile(__dirname + '/formulario.html');
});

app.post('/receber', function(req, res){
    res.write('Nome informado:' + req.body.nome);
    res.end();
});

app.listen(8080);
