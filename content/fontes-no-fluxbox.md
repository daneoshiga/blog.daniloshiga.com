Title: Fontes no Fluxbox
Date: 2012-06-20 23:37
Author: daniloshiga
Category: environment
Tags: environment, fluxbox
Slug: fontes-no-fluxbox

Fluxbox é um gerenciador de janelas para o linux extremamente leve, que
eu utilizo quando preciso focar os recursos da máquina em alguma outra
coisa.

O problema principal pra mim com o Fluxbox é que as fontes são
estranhamente renderizadas, fazendo com que eu acabe voltando para o
 gnome ou unity depois de usá-lo por um tempo.

Hoje encontrei uma solução aceitável para o problema, para isso, criei o
arquivo \~/.Xresources com o seguinte conteúdo:

` Xft.dpi: 96 Xft.antialias: true Xft.hinting: true Xft.rgba: rgb Xft.autohint: false Xft.hintstyle: hintslight Xft.lcdfilter: lcddefault`

 

reiniciei o lightdm e agora as fontes renderizadas no aplicativo estão
muito mais próximas (senão idênticas) ao que estou acostumado em outros
ambientes gráficos.

fonte: [Fixing ugly Qt fonts in Openbox, Fluxbox, etc. ][]

  [Fixing ugly Qt fonts in Openbox, Fluxbox, etc. ]: http://lovingthepenguin.blogspot.com.br/2011/07/fixing-ugly-qt-fonts-in-openbox-fluxbox.html
    "Fixing ugly Qt fonts in Openbox, Fluxbox, etc."
