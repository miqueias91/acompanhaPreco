<?php
header('Access-Control-Allow-Origin: *');

$url = "https://www.casasbahia.com.br/Eletrodomesticos/GeladeiraeRefrigerador/1Porta/refrigerador-electrolux-rfe39-frost-free-com-porta-latas-e-gaveta-extra-fria-322l-branco-2408036.html";
?>
<!doctype html>
<html lang="pt-br">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    <script type="text/javascript">
      $( document ).ready(function() {

        $.ajax({
          url : "<?=$url?>",
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          crossDomain: true,
          contentType: 'application/json',
          cache: false,
          type: 'GET',
          dataType: 'json',
          
          beforeSend : function(){
            console.log("ENVIANDO...");
          }
        })
        .done(function(msg){
          console.log(msg);
        })
        .fail(function(jqXHR, textStatus, msg){
          console.log(msg);
        }); 
      });
    </script>
  </body>
</html>