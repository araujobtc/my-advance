<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Aritmética</title>
</head>
<body>
    <h1>Teste Operadores Aritméticos</h1>
    <div id="container">
        <?php
            $n1 = $_GET["a"];
            $n2 = $_GET["b"];
            
            echo "Valores recebidos: $n1 e $n2<br>";
            echo "<br>Soma: ", $n1 + $n2;
            echo "<br>Diferença: ", $n1 - $n2;
            echo "<br>Multiplicação: ", $n1 * $n2;
            echo "<br>Divisão: ", $n1 / $n2;
            echo "<br>Resto da divisão inteira: ", $n1 % $n2;
            echo "<br>Exponenciação: ", $n1 ** $n2;
            echo "<br>Média: ", ($n1 + $n2)/2;
        ?>
    </div>
</body>
</html>