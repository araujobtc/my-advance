<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Variáveis</title>
</head>
<body>
    <h1>Teste de variáveis</h1>
    <div id="container">
        <?php
            $n = 20;
            $no = (string) "Isabelle";
            
            echo "Olá, meu nome é $no e tenho ".$n." anos.";
        ?>
    </div>
</body>
</html>