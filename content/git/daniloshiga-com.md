Title: daniloshiga.com
Date: 2012-12-22 18:39
Author: daniloshiga
Tags: hosting, personal, web
Slug: daniloshiga-com

Depois de muito tempo, resolvi iniciar meu site pessoal, e ao invés de
criar algo com um design arrojado e completo logo no início, vou fazer o
inverso, adicionar os dados e os links mais relevantes primeiro, e
extender o site a partir daí.

A idéia é que o site seja feito das melhores práticas em
desenvolvimento, sem pressa, com atenção aos detalhes.

Por enquanto o que existe é apenas um html com links para os vários
lugares da internet onde existem mais informações sobre mim, o site pode
ser visitado [aqui][]

O repositório do mesmo está no [github][] e a implantação está seguindo
a mesma linha deste mesmo [blog][], porém bem mais simples, o conteúdo
do post-receive hook é apenas uma linha:

    #!/bin/bash 
    GIT_WORK_TREE=[caminho para pasta pública na hospedagem] git checkout -f 

Uma melhor prática já aplicada é o uso de [microdata][] para dar um
pouco de semantica ao site, além de ser uma boa prática de SEO.

  [aqui]: http://daniloshiga.com
  [github]: https://github.com/daneoshiga/daniloshiga.com
  [blog]: http://blog.daniloshiga.com/2012/04/11/desenvolvimento-e-implantacao-do-wordpress-usando-git/
  [microdata]: http://support.google.com/webmasters/bin/answer.py?hl=en&answer=176035
