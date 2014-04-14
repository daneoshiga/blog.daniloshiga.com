Title: Pelican
Date: 2014-02-17
Author: daniloshiga
Tags: wordpress, static, python
Slug: pelican

É isso aí, wordpress é legal, tem um painel administrativo e tudo mais, mas está
na hora de ser [um dos caras legais][], resolvi trocar o wordpress por um
gerador de sites estático, e entre vários, escolhi o [Pelican][].

Pra mim, a grande vantagem é o tempo de carregamento, sem a necessidade de
processamento e acesso ao banco, o blog ficou bem mais rápido.

A grande maioria dos meus posts aqui acabaram sendo sobre o próprio blog,
técnicas mirabolantes para manter o wordpress atualizado e plugins bizarros para
conseguir postar usando o vim (bizarro mas legal).

Queria um tema simples, o mais minimalista possível, principalmente porque não
sou muito bom na parte de design. Então montei o layout usando o [Toast][], um
framework CSS bem simples, que o próprio autor considera como apenas framework
para facilitar a criação de wireframes, mas que eu gostei muito da simplicidade,
sem a necessidade de colocar algo enorme como um bootstrap (o código do Toast
tem apenas algumas regras bem simples.).

Para atingir essa simplicidade o mesmo não funciona no IE7, mas tudo bem, não
espero que ninguém acessando isso daqui esteja usando ele.

Considerei em colocar os comentários do Google Plus, gosto do modo como eles se
misturam com as postagens na rede social (de forma muito melhor do que a do
facebook, por exemplo), mas por padrão o widget do Google não é responsivo, além
de ser necessário ter conta para comentar.

E como o Pelican já tinha tudo pronto para uso do Disqus, resolvi utilizá-lo,
tinha trauma do mesmo pela lentidão que apresentava anos atrás, mas isso parece
ter se resolvido.

Outra coisa que aproveitei para fazer foi adicionar as tags semânticas do
[schema.org][], agora os posts tem definido corretamente autor, conteúdo e data
de postagem, o que já é um bom começo e que o Google já entende do que se trata
na hora de indexar.

Então é isso, não cheguei a fazer uma comparação muito exata, mas tenho certeza
que o blog está por volta de 3 vezes mais rápido para carregar, e aguentando uma
quantidade muito maior de visitas sem problemas, agora é fazer mais postagens,
se possível sem ser apenas sobre o próprio blog.


[um dos caras legais]: http://razius.com/articles/ditching-wordpress-and-becoming-one-of-the-cool-kids "Caras Legais"
[Pelican]: http://blog.getpelican.com/ "Pelican"
[Toast]: https://daneden.me/toast/ "Toast"
[schema.org]: http://schema.org "schema.org"
