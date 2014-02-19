Title: Separando arquivos numerados
Date: 2012-10-06 07:26
Author: daniloshiga
Category: bash
Tags: quick, script, simple
Slug: separando-arquivos-numerados

Para separar por volta de 200 arquivos numeros, fiz um pequeno shell
script

Os arquivos estão nomeados como "001 - nome" até "194 - nome", esse
script separa cada 10 episódios em uma pasta, a variável "j" foi
necessária por  
causa do 0 no início da numeração.

    #!/bin/bash
    for i in {0..19}; do
        if [ $i -lt 10 ];
        then
            j="0";
        else
            j="";
        fi
        mkdir -p /caminho/de/destino/$j$i
        cp -v $j$i* /caminho/de/destino/$j$i
    done;

Apenas um exemplo de um pequeno script para resolver um problema
simples.
