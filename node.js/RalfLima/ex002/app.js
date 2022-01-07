// importar arquivo de calculos

var calculos = require('./calculos')

// obter a função para multiplicar
var multiplicar = calculos.multiplicar;

//realizar um cálculo de multiplicação
console.log(multiplicar(5, 6))
