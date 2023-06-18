<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Operadores Aritméticos</title>
</head>
<body>
    <h1>Teste Funções Aritméticos</h1>
    <div id="container">
        <?php
            $x = $_GET["x"];
            $y = $_GET["y"];

            echo "Valores recebidos: $x e $y<br>";
            echo "<br>O valor absoluto de $x é ", abs($x);
            echo "<br>O valor absoluto de $y é ", abs($y);
            echo "<br>O valor de $x <sup>$y</sup> é ", pow($x, $y);
            echo "<br>A raiz quadrada de $x é ", sqrt($x);
            echo "<br>A raiz quadrada de $y é ",  sqrt($y);
            echo "<br>A parte inteiro da raiz quadrada de $y é ",  intval(sqrt($y));
            echo "<br>O valor arredondado de $x é ",  round($x);
            echo "<br>O valor arredondado de $y é ",  ceil($y);
            echo "<br>O valor arredondado da soma entre $x e $y é ",  floor($y);
            echo "<br>O valor de $x em moeda é R$", number_format($x, 2, ",", ".")
        ?>
    </div>
</body>
</html>