Title: Wordpress e temas padrão
Date: 2014-01-16 12:21
Author: daniloshiga
Category: meta
Tags: css, wordpress
Slug: wordpress-e-temas-padrao

A versão 3.8 do  wordpress está realmente diferente, o admin está com um
visual novo, e o tema padrão apresenta novo segue a mesma linha flat que
tem feito muito sucesso.

Gostei tanto do tema padrão que resolvi usá-lo para esse blog, só com
algumas pequenas mudanças, talvez eu "fuce" mais no decorrer do tempo,
mas está bem aceitável. O suficiente para que eu cancelasse os planos de
fazer algo baseado no temas [roots][].

No caso, as alterações que fiz no CSS foram as seguintes:

    :::css
    {.wrap:true .lang:css .decode:true}
    .entry-title {
    text-transform: none;
    }

    .site-content .entry-header,.site-content .entry-content,.site-content .entry-summary,.site-content .entry-meta,.page-content {
    margin: 0 auto;
    max-width: 674px;
    }

O primeiro para remover o estilo que deixa o título dos posts todo em
maiúsculo, e o segundo para aumentar um pouco a largura do espaço de
postagem.

  [roots]: http://roots.io/ "Roots"
