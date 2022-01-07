// express e express-handlebars
var express = require('express');
var exphbs = require('express-handlebars');

// app
var app = express();

// Template
app.engine('handlebars', exphbs.engine({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.set('views', './views');

// rotas
app.get('/', function(req, res){
    var pessoas = [
        {"nome":"Isabelle", "idade":18},
        {"nome":"Rafaela", "idade":27},
        {"nome":"Douglas", "idade":22}
    ]

    res.render('index', {gostandoDeNode: false, dados:pessoas});
});

app.get('/sobre', function(req, res){
    res.render('about');
});

// servidor
app.listen(8080);
