Title: gerar patch com pré-processamento do arquivo
Date: 2012-08-28 14:49
Author: daniloshiga
Category: bash
Tags: diff, redirect, sed
Slug: gerar-patch-com-pre-processamento-do-arquivo

Um exemplo de como gerar um patch de um arquivo mas antes fazendo algum
tipo de processamento, no caso, usando o sed para remover algumas linhas
do arquivo, por exemplo

`diff <(/bin/sed '/[regex]/d' arquivo.txt) <(/bin/sed '/[regex]/d' arquivo2.txt) > $patchfile`
