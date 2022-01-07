// importar o módulo http
var http = require('http');

// criar o servidor
http.createServer(function(req, res){
    res.write('aprendendo node.js com o Ralf');
    res.end();
}).listen(8080);
