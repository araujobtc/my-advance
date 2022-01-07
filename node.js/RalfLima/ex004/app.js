// importar o módulo http
var http = require('http');

// criar o servidor
http.createServer(function(req, res){
    res.write('Utilizando o nodemon');
    res.end();
}).listen(8080);
