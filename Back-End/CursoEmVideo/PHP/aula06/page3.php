<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Variáveis Referenciadas</title>
</head>
<body>
    <h1>Teste Variáveis Referenciadas</h1>
    <div id="container">
        <?php
            $a = 3;
            $b = &$a;
            $b += 5;
            echo $a;
            echo "<br>";
            echo $b;
        ?>
    </div>
</body>
</html>