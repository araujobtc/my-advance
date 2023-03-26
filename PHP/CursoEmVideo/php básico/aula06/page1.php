<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Operadores de Atribuição</title>
</head>
<body>
    <h1>Teste Operadores de Atribuição</h1>
    <div id="container">
        <?php
            $preco = $_GET["a"];
            echo "O preço do produto é R$". number_format($preco, 2, ",", ".");
            $preco += $preco*0.1;
            echo "<br>Com 10% de aumento vai para R$". number_format($preco, 2, ",", ".");
        ?>
    </div>
</body>
</html>